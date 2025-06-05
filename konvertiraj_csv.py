import os

def convert_csv_folder_to_utf8(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".csv"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, mode='r', encoding='windows-1250') as infile:
                        content = infile.read()
                    with open(full_path, mode='w', encoding='utf-8') as outfile:
                        outfile.write(content)
                    print(f"✅ Konvertirano: {full_path}")
                except Exception as e:
                    print(f"❌ Greška kod: {full_path} → {e}")

# Putanja do tvoje mape s CSV datotekama
folder_path = r"C:\Users\PC\Desktop\Vizualizacija\LokalniIzboriRH\public\rezultati"
convert_csv_folder_to_utf8(folder_path)
