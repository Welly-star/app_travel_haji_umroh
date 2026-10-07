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

    content = content.replace("final theme = Theme.of(context);\n", "")
    content = content.replace("Theme.of(context).", "theme.")
    content = content.replace("theme.", "Theme.of(context).")
    
    # We also use `Theme.of(context).of(context)`? No, `theme.` replaced to `Theme.of(context).`
    # Also, we might have `ThemeData Theme.of(context) = ...` if there were params. Let's fix that just in case.
    content = content.replace("ThemeData Theme.of(context)", "ThemeData theme")
    
    # Fix undefined primaryLight and color70
    content = content.replace("Theme.of(context).cardTheme.color70", "Colors.white70") 
    content = content.replace("Theme.of(context).primaryLight", "Theme.of(context).colorScheme.primary.withValues(alpha: 0.8)")
    
    # Fix the ThemeColors extension usage of `theme.isDark`
    # Wait, Theme.of(context).isDark requires the extension. Did we import the extension?
    # They should have `import '../theme/app_theme.dart';`
    if "import '../theme/app_theme.dart';" not in content:
        content = "import '../theme/app_theme.dart';\n" + content

    # Fix Invalid constant value
    # Regex to remove `const ` in front of `Widget(... Theme.of(context)...)`
    # Since regex is hard for nested parentheses, let's just strip `const ` from lines that contain `Theme.of(context)`
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'Theme.of(context)' in line and 'const ' in line:
            # We must be careful not to remove `const` from `const SizedBox()` if they are on the same line.
            # But it's safer to remove `const ` entirely from that line to fix the error.
            lines[i] = line.replace('const ', '')
            
    content = '\n'.join(lines)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
