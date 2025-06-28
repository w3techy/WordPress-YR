import csv
import io

existing_glossary_content = """en,yor,pos,description
Link,Ìlujá,noun,
Website,Ìkànnì,noun,
WordPress,WordPress,noun,"Please use WordPress as WordPress's translation on any place it is mentioned"
"""

new_translations_content = """en,yor,pos,description
100th,[Yoruba for: 100th],noun,
100th release,[yor:100th] Ìtújáde,noun,
100th release gutenberg,[yor:100th] Ìtújáde [yor:gutenberg],noun,
20th,[Yoruba for: 20th],noun,
3rd,[Yoruba for: 3rd],noun,
3rd-party,[Yoruba for: 3rd-party],noun,
3rd-party website,[yor:3rd-party] [yor:website],noun,
3rd-party website please,[yor:3rd-party] [yor:website] Jọ̀wọ́,noun,
5-minute,[Yoruba for: 5-minute],noun,
5th,[Yoruba for: 5th],noun,
7-day,[Yoruba for: 7-day],noun,
7-day retention,[yor:7-day] [yor:retention],noun,
7-day retention period,[yor:7-day] [yor:retention] [yor:period],noun,
a-z,[Yoruba for: a-z],noun,
a-z numbers,[yor:a-z] [yor:numbers],noun,
aa,[Yoruba for: aa],noun,
aa atag,[yor:aa] [yor:atag],noun,
aa atag conformance,[yor:aa] [yor:atag] [yor:conformance],noun,
ability,[Yoruba for: ability],noun,
able,[Yoruba for: able],noun,
able crop,[yor:able] [yor:crop],noun,
able crop image,[yor:able] [yor:crop] Àwòrán,noun,
able edit,[yor:able] Ṣàtúnṣe,noun,
able edit posts,[yor:able] Ṣàtúnṣe Àwọn àtẹ̀jáde,noun,
able quickly,[yor:able] [yor:quickly],noun,
able quickly easily,[yor:able] [yor:quickly] [yor:easily],noun,
able write,[yor:able] [yor:write],noun,
able write without,[yor:able] [yor:write] [yor:without],noun,
abstract,[Yoruba for: abstract],noun,
accept,[Yoruba for: accept],noun,
accept declaration,[yor:accept] [yor:declaration],noun,
accept declaration request,[yor:accept] [yor:declaration] [yor:request],noun,
acceptance,[Yoruba for: acceptance],noun,
acceptance change,[yor:acceptance] [yor:change],noun,
accepted,[Yoruba for: accepted],noun,
accepting,[Yoruba for: accepting],noun,
accepting plugins,[yor:accepting] Àwọn Plugin,noun,
accepting plugins nature,[yor:accepting] Àwọn Plugin [yor:nature],noun,
accepts,[Yoruba for: accepts],noun,
accepts csv,[yor:accepts] [yor:csv],noun,
accepts csv list,[yor:accepts] [yor:csv] Àtòjọ,noun,
access,[Yoruba for: access],noun,
access account,[yor:access] [yor:account],noun,
access block,[yor:access] Àkójọpọ̀,noun,
access block document,[yor:access] Àkójọpọ̀ [yor:document],noun,
access common,[yor:access] [yor:common],noun,
access common commands,[yor:access] [yor:common] [yor:commands],noun,
access content,[yor:access] Àkóónú,noun,
access content data,[yor:access] Àkóónú Dátà,noun,
access control,[yor:access] [yor:control],noun,
access data,[yor:access] Dátà,noun,
access details,[yor:access] [yor:details],noun,
access font,[yor:access] Fọ́ntì,noun,
access google,[yor:access] [yor:google],noun,
access google fonts,[yor:access] [yor:google] [yor:fonts],noun,
access granted,[yor:access] [yor:granted],noun,
access granted currentusername,[yor:access] [yor:granted] [yor:currentusername],noun,
access web,[yor:access] [yor:web],noun,
access web presence,[yor:access] [yor:web] [yor:presence],noun,
access website,[yor:access] [yor:website],noun,
access website administrators,[yor:access] [yor:website] [yor:administrators],noun,
access wordpress,[yor:access] [yor:wordpress],noun,
accessibility,[Yoruba for: accessibility],noun,
accessibility coding,[yor:accessibility] [yor:coding],noun,
accessibility coding standards,[yor:accessibility] [yor:coding] [yor:standards],noun,
accessibility expertise,[yor:accessibility] [yor:expertise],noun,
accessibility expertise across,[yor:accessibility] [yor:expertise] [yor:across],noun,
accessibility guidelines,[yor:accessibility] [yor:guidelines],noun,
accessibility guidelines wcag,[yor:accessibility] [yor:guidelines] [yor:wcag],noun,
accessibility handbook,[yor:accessibility] [yor:handbook],noun,
accessibility handbook page,[yor:accessibility] [yor:handbook] Ojúewé,noun,
accessibility improvements,[yor:accessibility] [yor:improvements],noun,
accessibility issue,[yor:accessibility] [yor:issue],noun,
accessibility issue encountered,[yor:accessibility] [yor:issue] [yor:encountered],noun,
accessibility list,[yor:accessibility] Àtòjọ,noun,
accessibility mistakes,[yor:accessibility] [yor:mistakes],noun,
accessibility mistakes without,[yor:accessibility] [yor:mistakes] [yor:without],noun,
accessibility performance,[yor:accessibility] [yor:performance],noun,
accessibility performance security,[yor:accessibility] [yor:performance] [yor:security],noun,
accessibility team,[yor:accessibility] [yor:team],noun,
accessibility wordpress,[yor:accessibility] [yor:wordpress],noun,
accessibility wordpress core,[yor:accessibility] [yor:wordpress] [yor:core],noun,
accessible,[Yoruba for: accessible],noun,
accessible content,[yor:accessible] Àkóónú,noun,
accessible content assist,[yor:accessible] Àkóónú [yor:assist],noun,
accessible encourages,[yor:accessible] [yor:encourages],noun,
accessible encourages creation,[yor:accessible] [yor:encourages] [yor:creation],noun,
accessing,[Yoruba for: accessing],noun,
accordance,[Yoruba for: accordance],noun,
accordance privacy,[yor:accordance] [yor:privacy],noun,
accordance privacy statement,[yor:accordance] [yor:privacy] [yor:statement],noun,
account,[Yoruba for: account],noun,
account activated,[yor:account] [yor:activated],noun,
account contribute,[yor:account] [yor:contribute],noun,
account deletion,[yor:account] [yor:deletion],noun,
account first,[yor:account] [yor:first],noun,
account please,[yor:account] Jọ̀wọ́,noun,
account please log,[yor:account] Jọ̀wọ́ [yor:log],noun,
account recommended,[yor:account] [yor:recommended],noun,
account recommended log,[yor:account] [yor:recommended] [yor:log],noun,
account relevant,[yor:account] [yor:relevant],noun,
account relevant personal,[yor:account] [yor:relevant] [yor:personal],noun,
account request,[yor:account] [yor:request],noun,
account supported,[yor:account] [yor:supported],noun,
account supported following,[yor:account] [yor:supported] [yor:following],noun,
account username,[yor:account] [yor:username],noun,
account username instead,[yor:account] [yor:username] [yor:instead],noun,
accounts,[Yoruba for: accounts],noun,
accounts submitted,[yor:accounts] [yor:submitted],noun,
accounts submitted information,[yor:accounts] [yor:submitted] Ìsọfúnni,noun,
acid,[Yoruba for: acid],noun,
acid green,[yor:acid] [yor:green],noun,
across,[Yoruba for: across],noun,
across ecosystem,[yor:across] [yor:ecosystem],noun,
across multiple,[yor:across] [yor:multiple],noun,
across project,[yor:across] [yor:project],noun,
across project improve,[yor:across] [yor:project] [yor:improve],noun,
across site,Ìkànnì,noun,
across sites,[yor:across] [yor:sites],noun,
across web,[yor:across] [yor:web],noun,
across wordpress,[yor:across] WordPress,noun,
action,[Yoruba for: action],noun,
action confirmed,[yor:action] [yor:confirmed],noun,
action undone,[yor:action] [yor:undone],noun,
actions,[Yoruba for: actions],noun,
activate,[Yoruba for: activate],noun,
activate plugins,[yor:activate] Àwọn Plugin,noun,
activate receive,[yor:activate] [yor:receive],noun,
activate receive another,[yor:activate] [yor:receive] [yor:another],noun,
activate save,[yor:activate] [yor:save],noun,
activate site,Ìkànnì,noun,
activated,[Yoruba for: activated],noun,
activating,[Yoruba for: activating],noun,
activation,[Yoruba for: activation],noun,
active,[Yoruba for: active],noun,
active feature,[yor:active] [yor:feature],noun,
active feature work,[yor:active] [yor:feature] [yor:work],noun,
active theme,Àkòrí,noun,
actively,[Yoruba for: actively],noun,
actively maintained,[yor:actively] [yor:maintained],noun,
activities,[Yoruba for: activities],noun,
activities like,[yor:activities] Fẹ́ràn,noun,
activities like purchasing,[yor:activities] Fẹ́ràn [yor:purchasing],noun,
activity,[Yoruba for: activity],noun,
actually,[Yoruba for: actually],noun,
actually appreciate,[yor:actually] [yor:appreciate],noun,
actually appreciate use,[yor:actually] [yor:appreciate] Lò,noun,
actually viewing,[yor:actually] [yor:viewing],noun,
actually viewing content,[yor:actually] [yor:viewing] Àkóónú,noun,
adams,[Yoruba for: adams],noun,
add,Fi Kún,noun,
add alt,Fi Kún [yor:alt],noun,
add alt text,Fi Kún [yor:alt] Ọ̀rọ̀,noun,
add audio,Fi Kún [yor:audio],noun,
add audio playlist,Fi Kún [yor:audio] [yor:playlist],noun,
add block,Fi Kún Àkójọpọ̀,noun,
add category,Fi Kún [yor:category],noun,
add color,Fi Kún [yor:color],noun,
add complex,Fi Kún [yor:complex],noun,
add complex galleries,Fi Kún [yor:complex] [yor:galleries],noun,
add cross-locale,Fi Kún [yor:cross-locale],noun,
add cross-locale pte,Fi Kún [yor:cross-locale] [yor:pte],noun,
add css,Fi Kún [yor:css],noun,
add css customize,Fi Kún [yor:css] [yor:customize],noun,
add custom,Fi Kún Àdáni,noun,
add custom code,Fi Kún Àdáni Kóòdù,noun,
add edit,Fi Kún Ṣàtúnṣe,noun,
add edit content,Fi Kún Ṣàtúnṣe Àkóónú,noun,
add gallery,Fi Kún [yor:gallery],noun,
add image,Fi Kún Àwòrán,noun,
add image upload,Fi Kún Àwòrán [yor:upload],noun,
add items,Fi Kún Àwọn nǹkan,noun,
add lines,Fi Kún [yor:lines],noun,
add lines code,Fi Kún [yor:lines] Kóòdù,noun,
add link,Fi Kún [yor:link],noun,
add media,Fi Kún [yor:media],noun,
add menu,Fi Kún Àkójọ Àṣàyàn,noun,
add menu items,Fi Kún Àkójọ Àṣàyàn Àwọn nǹkan,noun,
add navigation,Fi Kún Ìtọ́sọ́nà,noun,
add navigation menu,Fi Kún Ìtọ́sọ́nà Àkójọ Àṣàyàn,noun,
add new,Fi Kún Tuntun,noun,
add new comments,Fi Kún Tuntun Àwọn àríwísí,noun,
add new page,Fi Kún Tuntun Ojúewé,noun,
add new support,Fi Kún Tuntun Ìtìlẹ́yìn,noun,
add new term,Fi Kún Tuntun [yor:term],noun,
add page,Fi Kún Ojúewé,noun,
add pattern,Fi Kún Àpẹẹrẹ,noun,
add post,Fi Kún Àtẹ̀jáde,noun,
add remove,Fi Kún [yor:remove],noun,
add required,Fi Kún [yor:required],noun,
add shadow,Fi Kún [yor:shadow],noun,
add submenu,Fi Kún [yor:submenu],noun,
add template,Fi Kún Àdàkọ,noun,
add text,Fi Kún Ọ̀rọ̀,noun,
add text blocks,Fi Kún Ọ̀rọ̀ Àwọn àkójọpọ̀,noun,
add video,Fi Kún [yor:video],noun,
add video playlist,Fi Kún [yor:video] [yor:playlist],noun,
add website,Fi Kún [yor:website],noun,
add website add,Fi Kún [yor:website] Fi Kún,noun,
add widget,Fi Kún Widget,noun,
"""

# Use io.StringIO to treat the string data like a file
existing_csvfile = io.StringIO(existing_glossary_content)
new_translations_csvfile = io.StringIO(new_translations_content)

# --- 1. Read existing main glossary ---
existing_glossary_entries = []
existing_english_terms = set()
fieldnames = ['en', 'yor', 'pos', 'description']

reader = csv.DictReader(existing_csvfile)
if reader.fieldnames:
    fieldnames = reader.fieldnames
for row in reader:
    if row and 'en' in row and row['en']:
        existing_glossary_entries.append(row)
        existing_english_terms.add(row['en'].strip().lower())

# --- 2. Read the subset of new (placeholder) translations ---
new_translated_terms = []
reader_new = csv.DictReader(new_translations_csvfile)
for row in reader_new:
    new_translated_terms.append(row)

# --- 3. Combine glossary entries ---
combined_glossary_dict = {row['en'].strip().lower(): row for row in existing_glossary_entries if 'en' in row and row['en']}

for new_term_row in new_translated_terms:
    en_term = new_term_row.get('en','').strip()
    if not en_term:
        continue

    # Add new terms or overwrite existing ones if the English term matches.
    # This will use the placeholder translations from the subset for new and existing 'en' terms.
    combined_glossary_dict[en_term.lower()] = {
        'en': en_term,
        'yor': new_term_row.get('yor', f"[Yoruba for: {en_term}]"),
        'pos': new_term_row.get('pos', 'noun'),
        'description': new_term_row.get('description', '')
    }

final_glossary_list = list(combined_glossary_dict.values())

# --- 4. Sort the combined list alphabetically by the English term ---
final_glossary_list.sort(key=lambda x: x.get('en', '').strip().lower() if x.get('en') else '')

# --- 5. Prepare the CSV content for overwrite_file_with_block ---
output_csv_io = io.StringIO()
writer = csv.DictWriter(output_csv_io, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
writer.writeheader()
writer.writerows(final_glossary_list)
final_csv_content = output_csv_io.getvalue()
output_csv_io.close()

# Print the final CSV content to be used by the tool
# The actual tool call will be done by the agent in the next step.
print("---FINAL CSV CONTENT---")
print(final_csv_content)
print("---END FINAL CSV CONTENT---")
