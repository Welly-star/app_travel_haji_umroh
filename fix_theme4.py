import os

screens_dir = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens'

def fix_const_line(file, line_number):
    path = os.path.join(screens_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if 'const' in lines[line_number - 1]:
        lines[line_number - 1] = lines[line_number - 1].replace("const", "")
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

fix_const_line('jadwal_penerbangan_screen.dart', 32)
fix_const_line('jadwal_penerbangan_screen.dart', 252)
fix_const_line('kontak_petugas_screen.dart', 38)
fix_const_line('lokasi_penting_screen.dart', 37)

print("Done")

