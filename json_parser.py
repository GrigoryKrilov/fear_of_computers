import json

pah_json = '/Users/ilpech/luckydog/Stats_version_1_seas_20_21.json'
with open(pah_json, 'r') as file:
    json_data = json.load(file)
print(json_data.keys())
print(json_data['matches'][0].keys())

