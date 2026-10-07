import os
import re

screens_dir = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens'

# Fix duplicate imports
files = [
    'digital_tasbih_screen.dart', 
    'formulir_pendaftaran_screen.dart', 
    'jadwal_penerbangan_screen.dart', 
    'kontak_petugas_screen.dart', 
    'lokasi_penting_screen.dart',
    'landing_page.dart',
    'login_page.dart'
]

for file in files:
    path = os.path.join(screens_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the first occurrence of import if there are two
    if content.count("import '../theme/app_theme.dart';") > 1:
        content = content.replace("import '../theme/app_theme.dart';\n", "", 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix const issues manually on those lines
def fix_const_line(file, line_number):
    path = os.path.join(screens_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines[line_number - 1] = lines[line_number - 1].replace("const", "")
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

fix_const_line('jadwal_penerbangan_screen.dart', 33)
fix_const_line('jadwal_penerbangan_screen.dart', 253)
fix_const_line('kontak_petugas_screen.dart', 39)
fix_const_line('lokasi_penting_screen.dart', 38)

print("Done")

