import polib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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

# Define PO file paths
po_files = [
    "meta-plugins-v3-yor.po",
    "meta-rosetta-yor.po",
    "meta-wordpress-org-yor (2).po",
    "meta-wordpress-org-yor.po",
    "wp-dev-yor.po"
]

all_msgids = []

# 1. Extract all msgid strings from the .po files
print("Step 1: Extracting msgid strings...")
for po_file_path in po_files:
    try:
        po = polib.pofile(po_file_path)
        for entry in po:
            if entry.msgid:
                all_msgids.append(entry.msgid)
        print(f"Processed {po_file_path}, found {len(po)} entries.")
    except Exception as e:
        print(f"Error processing {po_file_path}: {e}")

if not all_msgids:
    print("No msgids found. Exiting.")
    exit()

unique_msgids = sorted(list(set(all_msgids)))
print(f"\nTotal unique msgids found: {len(unique_msgids)}")

# Store unique_msgids to a file for the next step (optional, but good for large data)
with open("unique_msgids.txt", "w") as f:
    for msgid in unique_msgids:
        f.write(msgid + "\n")

print("\nStep 1 complete: All msgid strings have been extracted and unique ones saved to unique_msgids.txt.")
