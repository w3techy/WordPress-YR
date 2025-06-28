import polib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
import string
import re

# Ensure NLTK resources are available
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords', quiet=True)
try:
    word_tokenize("test")
except LookupError:
    nltk.download('punkt', quiet=True)

# Load unique msgids from the file
print("Step 2: Identifying common terms (threshold: >= 2 occurrences)...")
unique_msgids = []
try:
    with open("unique_msgids.txt", "r") as f:
        unique_msgids = [line.strip() for line in f]
except FileNotFoundError:
    print("Error: unique_msgids.txt not found. Please run the extraction script first.")
    exit()

if not unique_msgids:
    print("No unique msgids to process. Exiting.")
    exit()

print(f"Loaded {len(unique_msgids)} unique msgids.")

stop_words = set(stopwords.words('english'))
# Extended punctuation to catch more cases, including specific Unicode quotes
punctuation_chars = string.punctuation + "’“”—…“”‘’•●"

# Function to preprocess text
def preprocess_text(text):
    # Remove URLs
    text = re.sub(r'http[s]?://\S+', '', text)
    # Remove placeholders like %s, %1$s, %2$d, %1$d, %2$s etc.
    # This regex handles variations like %s, %d, %1$s, %2$d, %1$s, etc.
    text = re.sub(r'%(\d+\$)?([sd])', '', text)
    # Remove HTML-like tags
    text = re.sub(r'<[^>]+>', '', text)
    # Tokenize
    tokens = word_tokenize(text.lower())

    processed_tokens = []
    for token in tokens:
        # Remove leading/trailing punctuation from token
        cleaned_token = token.strip(punctuation_chars)
        if (cleaned_token and # Ensure token is not empty after stripping
            cleaned_token not in stop_words and
            cleaned_token not in punctuation_chars and # Check again after strip
            len(cleaned_token) > 1 and
            not cleaned_token.isdigit() and
            not re.fullmatch(r'[\W\d_]+', cleaned_token) and # Ignore tokens that are only non-alphanumeric
            re.search(r'[a-zA-Z]', cleaned_token)): # Ensure token contains at least one letter
            processed_tokens.append(cleaned_token)

    return processed_tokens

# --- N-gram generation and frequency counting ---
term_document_frequency = Counter()

# For 1-grams (single words)
for msgid in unique_msgids:
    tokens = preprocess_text(msgid)
    unique_terms_in_msgid = set(tokens)
    for term in unique_terms_in_msgid:
        term_document_frequency[term] += 1

# For 2-grams
for msgid in unique_msgids:
    tokens = preprocess_text(msgid)
    if len(tokens) >= 2:
        two_grams = [" ".join(gram) for gram in ngrams(tokens, 2)]
        unique_2_grams_in_msgid = set(two_grams)
        for gram2 in unique_2_grams_in_msgid:
            term_document_frequency[gram2] += 1

# For 3-grams
for msgid in unique_msgids:
    tokens = preprocess_text(msgid)
    if len(tokens) >= 3:
        three_grams = [" ".join(gram) for gram in ngrams(tokens, 3)]
        unique_3_grams_in_msgid = set(three_grams)
        for gram3 in unique_3_grams_in_msgid:
            term_document_frequency[gram3] += 1

# --- Filter popular terms ---
threshold_count = 2  # New threshold: appears 2 or more times

popular_terms_for_glossary = []
for term, count in term_document_frequency.items():
    if count >= threshold_count:
        # Additional check to ensure term is not empty or just symbols after potential stripping in n-gram joining
        stripped_term = term.strip()
        if stripped_term and re.search(r'[a-zA-Z]', stripped_term): # Ensure it has at least one letter
             popular_terms_for_glossary.append((stripped_term, count))


# Sort popular terms by frequency (descending), then alphabetically for tie-breaking
popular_terms_for_glossary.sort(key=lambda x: (-x[1], x[0]))

print(f"\nFound {len(popular_terms_for_glossary)} popular terms (appearing in at least {threshold_count} unique msgids):")
# Limiting print output for brevity if the list is very long
limit_print = 1000
for i, (term, count) in enumerate(popular_terms_for_glossary):
    if i < limit_print:
        print(f"- \"{term}\" (appears in {count} msgids)")
    elif i == limit_print:
        print(f"... and {len(popular_terms_for_glossary) - limit_print} more terms.")
        break

# Save popular terms to a file
with open("popular_terms_for_glossary.txt", "w") as f:
    for term, count in popular_terms_for_glossary:
        f.write(f"{term}\n")

print(f"\nStep 2 complete: {len(popular_terms_for_glossary)} popular terms identified and saved to popular_terms_for_glossary.txt.")
