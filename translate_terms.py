import csv

print("Step 4: Translating new popular terms to Yoruba (first 200 terms - placeholder translations)...")

new_terms_to_translate = []
try:
    with open("new_terms_to_translate.txt", "r") as f:
        for line in f:
            new_terms_to_translate.append(line.strip())
except FileNotFoundError:
    print("Error: new_terms_to_translate.txt not found. Please run the filtering script first.")
    exit()

if not new_terms_to_translate:
    print("No new terms to translate. Exiting.")
    exit()

# Select a subset for initial translation (e.g., first 200)
subset_to_translate = new_terms_to_translate[:200]
print(f"Selected the first {len(subset_to_translate)} terms for placeholder translation.")

translated_terms = [] # List of tuples: (english_term, yoruba_translation_placeholder)

for term_en in subset_to_translate:
    # --- Placeholder Translation Logic ---
    # In a real scenario, this would involve an API call or a dictionary lookup.
    # For now, we create a placeholder.
    # Simple rule: if the term is multi-word, try to capitalize each word for the placeholder.
    # Otherwise, just use the term.

    yor_placeholder = f"[Yoruba for: {term_en}]"

    # For this exercise, let's try a slightly more "translated-looking" placeholder for some common words
    # This is purely illustrative and NOT real translation.
    simple_map = {
        "site": "Ìkànnì", # Already in glossary, but good for example if it weren't
        "block": "Àkójọpọ̀",
        "post": "Àtẹ̀jáde",
        "new": "Tuntun",
        "page": "Ojúewé",
        "content": "Àkóónú",
        "use": "Lò",
        "theme": "Àkòrí",
        "please": "Jọ̀wọ́",
        "image": "Àwòrán",
        "error": "Àṣìṣe",
        "user": "Olùlò",
        "add": "Fi Kún",
        "sorry": "Má Bínú",
        "template": "Àdàkọ",
        "plugin": "Plugin", # Often kept as is or with slight modification
        "email": "Email",
        "type": "Irú",
        "allowed": "Gbààyè",
        "blocks": "Àwọn àkójọpọ̀",
        "menu": "Àkójọ Àṣàyàn",
        "create": "Ṣẹ̀dá",
        "set": "Ṣètò",
        "posts": "Àwọn àtẹ̀jáde",
        "list": "Àtòjọ",
        "edit": "Ṣàtúnṣe",
        "name": "Orúkọ",
        "editor": "Olóòtú",
        "must": "Gbọ́dọ̀",
        "used": "Lílò",
        "text": "Ọ̀rọ̀",
        "file": "Fáìlì",
        "comment": "Àríwísí",
        "display": "Ìfihàn",
        "pattern": "Àpẹẹrẹ",
        "invalid": "Àìtọ́",
        "found": "Rí",
        "code": "Kóòdù",
        "password": "Ọ̀rọ̀ìpamọ́",
        "support": "Ìtìlẹ́yìn",
        "search": "Ìwáàdí",
        "may": "Lè",
        "plugins": "Àwọn Plugin",
        "wordpress.org": "WordPress.org", # Proper noun
        "url": "URL",
        "available": "Wà Fárà",
        "custom": "Àdáni",
        "users": "Àwọn olùlò",
        "address": "Àdírẹ́sì",
        "information": "Ìsọfúnni",
        "could": "Lè",
        "navigation": "Ìtọ́sọ́nà",
        "version": "Ẹ̀yà",
        "make": "Ṣe",
        "data": "Dátà",
        "open": "Ṣí",
        "title": "Àkọlé",
        "comments": "Àwọn àríwísí",
        "font": "Fọ́ntì",
        "view": "Ìwòran",
        "release": "Ìtújáde",
        "show": "Fi hàn",
        "id": "ID", # Often kept as is
        "like": "Fẹ́ràn",
        "items": "Àwọn nǹkan",
        "widget": "Widget" # Often kept as is
    }

    # Use the simple map if the term exists, otherwise the generic placeholder
    # For multi-word terms, this simple map won't work well without more logic.
    # This is just for a slightly better placeholder for this step.
    if term_en.lower() in simple_map:
        yor_placeholder = simple_map[term_en.lower()]
    else:
        # For multi-word terms, let's try to "translate" known parts if they are single words in our map
        parts = term_en.split(' ')
        if len(parts) > 1:
            translated_parts = [simple_map.get(part.lower(), f"[yor:{part}]") for part in parts]
            yor_placeholder = " ".join(translated_parts)
        # else, it remains the generic placeholder for unmapped single words

    translated_terms.append({'en': term_en, 'yor': yor_placeholder, 'pos': 'noun', 'description': ''})


# Save the subset of translated terms to a temporary CSV for review
output_csv_path = "translated_terms_subset_for_approval.csv"
with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['en', 'yor', 'pos', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(translated_terms)

print(f"\nGenerated placeholder translations for {len(subset_to_translate)} terms.")
print(f"These have been saved to '{output_csv_path}' for the next approval step.")
print("\nStep 4 complete: Placeholder translations generated for a subset of terms.")
