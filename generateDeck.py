import csv
import json

filename = "deck.csv"

final_data = []
with open(filename) as fp:
    reader = csv.reader(fp, delimiter=",")
    next(reader, None)
    for row in reader:
        try:
            dict_to_add = {
                "type": row[1],
                "prompt": row[0],
                "minPlayersRequired": int(row[4])
            }
            if row[1] == "Rule":
                dict_to_add["terminationText"] = row[3]
            final_data.append(dict_to_add)
        except Exception as e:
            print("ERROR: Could not add prompt for some reasons")

with open('caliente.json', 'w') as f:
    json.dump(final_data, f)
    print("Done!")