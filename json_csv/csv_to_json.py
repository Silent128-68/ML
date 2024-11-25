import csv
import json
from collections import defaultdict

constellations = defaultdict(lambda: {"brightest_stars": []})

with open('stars.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        constellation_name = row['Constellation']
        if 'Latin Name' not in constellations[constellation_name]:
            constellations[constellation_name].update({
                "name": row['Latin Name'],
                "abbreviation": row['Abbreviation'],
                "area": int(row['Area']),
                "neighboring_constellations": []  # Эта информация недоступна в CSV
            })
        constellations[constellation_name]["brightest_stars"].append({
            "name": row['Star Name'],
            "brightness": float(row['Brightness'])
        })

restored_data = {"constellations": list(constellations.values())}

with open('restored_constellations.json', 'w', encoding='utf-8') as json_file:
    json.dump(restored_data, json_file, indent=4, ensure_ascii=False, sort_keys=True)

print("JSON-файл restored_constellations.json успешно создан.")
