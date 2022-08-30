import csv
import json

filename = "deck.csv"

final_data = []
with open(filename) as fp:
    reader = csv.reader(fp, delimiter=",")
    next(reader, None)
    for row in reader:
        dict_to_add = {
            "type": row[1],
            "prompt": row[0],
            "minPlayersRequired": row[4]
        }
        if row[1] == "Rule":
            dict_to_add["terminationText"] = row[3]
        final_data.append(dict_to_add)
    #data_read = [row for row in reader]
print(final_data)
with open('caliente.json', 'w') as f:
    json.dump(final_data, f)