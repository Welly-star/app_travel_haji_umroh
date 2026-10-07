import os
import re

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

    # Fix the import
    content = content.replace("app_Theme.of(context).dart", "app_theme.dart")
    
    # Fix the cardTheme colors
    content = content.replace("Theme.of(context).cardTheme.color60", "Colors.white60")
    content = content.replace("Theme.of(context).cardTheme.color24", "Colors.white24")
    
    # Fix the nullable value issue
    content = content.replace("Theme.of(context).cardTheme.color.withValues", "(Theme.of(context).cardTheme.color ?? Colors.white).withValues")
    content = content.replace("Theme.of(context).colorScheme.primary.withValues", "Theme.of(context).colorScheme.primary.withValues") # Wait, is primary nullable? No.
    
    # Fix primaryDark
    content = content.replace("Theme.of(context).colorScheme.primaryDark", "Theme.of(context).colorScheme.primary")
    
    # Still some const_eval_method_invocation. Remove 'const ' on those lines again.
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'Theme.of(context)' in line and 'const ' in line:
            lines[i] = line.replace('const ', '')

    content = '\n'.join(lines)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")

