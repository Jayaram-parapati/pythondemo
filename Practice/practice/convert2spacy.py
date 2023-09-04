import spacy
import json
from spacy.tokens import DocBin
import itertools
import sys

# if len(sys.argv) > 1:
#     filename = sys.argv[1]

training_data_json_file = f"c:\\Users\\anand.adapa\\Desktop\\resumes 50\\newproject_db.output_data.json"
training_data_json = []
empty_tds = []
training_data = []


with open(training_data_json_file,"r", encoding="utf-8") as op:
    training_data_json = json.load(op)

training_data_len = len(training_data_json)


if training_data_len < 50:
    print(f"⚠ Insufficient Data. Please prepare atleast 50 records. provided {training_data_len} records only")
    exit(0)

for td in training_data_json:
    text = td["text"]
    entities = td["entities"]
    
    # text = td["data"]["text"]
    # entities = [[tdv["value"]["start"],tdv["value"]["end"],tdv["value"]["text"]] for tdv in td["annotations"][0]["result"]]
    

    if len(entities)==0: #means no entities marked
        empty_tds.append(text)
        continue

    #remove duplicates from list of entities
    entities.sort()
    unique_entities = [ent for ent,_ in itertools.groupby(entities) ]
    training_data.append((text, unique_entities))

# print(training_data)

nlp = spacy.blank("en")
db = DocBin()
skipped = 0
total = 0 

for text,entities in training_data:
    doc = nlp.make_doc(text)
    valid_ents = []
    try:
        for start, end, label in entities:
            span = doc.char_span(start,end,label=label,alignment_mode="contract")
            total += 1
            if span is None:# or span.text.startswith(" ") or span.text.endswith(" ") :
                print(f"⚠  Skipping Entity : {text[0:30]}...")
                skipped += 1
            else:
                valid_ents.append(span)
        doc.ents = valid_ents
        db.add(doc)
    except Exception as ex:
        print("⚠ ", ex)
        skipped += 1

# db.to_disk(f"data/{filename}.spacy")

print("✨ Results:")
print(f"Total Training Data : {training_data_len}")
print(f"Empty TDs : {len(empty_tds)}")
print(f"Failed to Convert : {skipped} / {total} = {skipped/total*100} %")


# python -m spacy train config.cfg --paths.train ./data/nabi.spacy --paths.dev ./data/dhanaveera.spacy





