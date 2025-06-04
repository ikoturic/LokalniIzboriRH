import os
import re

# Korijenski direktorij
root_dir = r'C:\Users\PC\Desktop\Vizualizacija\Lokalni izbori RH\public\rezultati'

# Zamjene znakova
replacements = {
    'ƒ': 'č',
    'å': 'ć',
    'º': 'ž'
}

# Funkcija za zamjenu znakova u stringu
def replace_chars(text):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Provjera je li naziv datoteke valjan za Windows
def is_valid_filename(name):
    return not bool(re.search(r'[<>:"/\\|?*]', name))

# Glavni prolaz kroz datoteke
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.csv'):
            # Zamjena u nazivu datoteke
            new_filename = replace_chars(filename)
            old_path = os.path.join(dirpath, filename)
            new_path = os.path.join(dirpath, new_filename)

            # Preimenovanje ako je potrebno
            if new_filename != filename:
                if not is_valid_filename(new_filename):
                    print(f"Neispravan naziv datoteke: {new_filename}")
                    continue
                if os.path.exists(new_path):
                    print(f"Preskočeno (već postoji): {new_filename}")
                    continue
                try:
                    os.rename(old_path, new_path)
                    print(f"Preimenovano: {filename} -> {new_filename}")
                except Exception as e:
                    print(f"Greška kod preimenovanja {filename}: {e}")
                    continue
            else:
                new_path = old_path  # Ako nema preimenovanja, koristi staru putanju

            # Čitanje, zamjena i zapis sadržaja
            try:
                with open(new_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                new_content = replace_chars(content)
                if new_content != content:
                    with open(new_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Zamijenjeni znakovi unutar datoteke: {new_filename}")
            except Exception as e:
                print(f"Greška kod čitanja/zapisa u {new_filename}: {e}")
