import os

screens_dir = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens'
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

    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'theme.' in line and 'const ' in line:
            lines[i] = line.replace('const ', '')

    content = '\n'.join(lines)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
