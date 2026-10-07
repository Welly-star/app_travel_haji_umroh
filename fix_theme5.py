import os

def remove_const_before(file, line_number):
    path = os.path.join(r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens', file)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # search backwards from line_number - 1 for 'const '
    for i in range(line_number - 1, max(-1, line_number - 10), -1):
        if 'const ' in lines[i]:
            lines[i] = lines[i].replace('const ', '')
            break

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

remove_const_before('kontak_petugas_screen.dart', 38)
remove_const_before('lokasi_penting_screen.dart', 37)

print("Done")

