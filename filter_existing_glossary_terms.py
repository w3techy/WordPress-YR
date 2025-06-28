import csv

print("Step 3: Filtering out terms already present in the glossary...")

# 1. Read popular terms
popular_terms_with_counts = []
try:
    with open("popular_terms_for_glossary.txt", "r") as f:
        for line in f:
            term = line.strip()
            # The count is not strictly needed for filtering, but preserving it might be useful
            # For now, just read the term. If counts are needed later, adjust reading.
            popular_terms_with_counts.append(term)
except FileNotFoundError:
    print("Error: popular_terms_for_glossary.txt not found. Please run the previous script first.")
    exit()

if not popular_terms_with_counts:
    print("No popular terms to process. Exiting.")
    exit()

print(f"Loaded {len(popular_terms_with_counts)} popular terms.")

# 2. Read existing glossary and extract English terms
existing_glossary_terms_en = set()
glossary_file_path = "--locale-yor-glossary.csv"
try:
    with open(glossary_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) # Skip header
        if header != ['en', 'yor', 'pos', 'description']:
            print(f"Warning: Glossary header is {header}, expected ['en', 'yor', 'pos', 'description']")

        for row in reader:
            if row and len(row) > 0:
                existing_glossary_terms_en.add(row[0].strip().lower())
except FileNotFoundError:
    print(f"Warning: Glossary file {glossary_file_path} not found. Proceeding without filtering.")
except Exception as e:
    print(f"Error reading glossary file {glossary_file_path}: {e}")

print(f"Loaded {len(existing_glossary_terms_en)} existing English terms from glossary: {existing_glossary_terms_en}")

# 3. Filter out existing terms
new_terms_to_translate = []
filtered_out_count = 0

# We only have terms in popular_terms_with_counts, not term-count pairs as before.
# The file popular_terms_for_glossary.txt was saved with one term per line.
for term in popular_terms_with_counts:
    if term.lower() not in existing_glossary_terms_en:
        new_terms_to_translate.append(term)
    else:
        filtered_out_count += 1

# Sort the new terms alphabetically for consistent output
new_terms_to_translate.sort()

# 4. Save the new, unique terms to a file
output_file_path = "new_terms_to_translate.txt"
with open(output_file_path, "w") as f:
    for term in new_terms_to_translate:
        f.write(f"{term}\n")

print(f"\nFiltered out {filtered_out_count} terms already in the glossary.")
print(f"{len(new_terms_to_translate)} new terms remain to be translated.")
print(f"New terms saved to {output_file_path}.")
print("\nStep 3 complete: Existing glossary terms filtered out.")
