import json
import re

def split_camel_case(name):
    # Razdvaja riječi u camelCase ili PascalCase stringu
    return re.sub('([a-z])([A-Z])', r'\1 \2', name)

def process_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    results = []
    
    for feature in data['features']:
        name_2 = feature['properties']['NAME_2']
        
        # Provjeri ima li velikih slova unutar riječi (koja nisu prvo slovo)
        if re.search(r'(?<=[a-z])[A-Z]', name_2):
            split_name = split_camel_case(name_2)
            results.append((name_2, split_name))
    
    return results

# Primjer korištenja - odaberite jedan od načina za putanju
file_path = r'C:\Users\PC\Desktop\Vizualizacija\LokalniIzboriRH\public\cro_opcine.json'  # Raw string

separated_names = process_geojson(file_path)

for original, separated in separated_names:
    print(f"Original: {original} → Separirano: {separated}")