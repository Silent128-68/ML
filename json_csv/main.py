import json
import csv

with open('constellations.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

fields = ['Star Name', 'Brightness', 'Constellation', 'Latin Name', 'Abbreviation', 'Area']

stars = []
for constellation in data['constellations']:
    for star in constellation['brightest_stars']:
        stars.append({
            'Star Name': star['name'],
            'Brightness': star['brightness'],
            'Constellation': constellation['name'],
            'Latin Name': constellation['name'],
            'Abbreviation': constellation['abbreviation'],
            'Area': constellation['area']
        })
stars.sort(key=lambda x: x['Brightness'])

with open('stars.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(stars)

print("CSV-файл stars.csv успешно создан.")
