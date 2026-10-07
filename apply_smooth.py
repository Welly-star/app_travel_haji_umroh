import re

# Update main_nav_screen.dart
file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\main_nav_screen.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("foregroundColor: theme.isDark ? const Color(0xFF132A22) : const Color(0xFF07382C),", "foregroundColor: theme.fabForeground,")
content = content.replace("color: theme.isDark ? const Color(0xFF11241C) : Colors.white,", "color: theme.bottomNavBg,")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update home_screen.dart
file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("color: theme.isDark ? const Color(0xFF182E25) : const Color(0xFFFBF8EE),", "color: theme.wisdomCardBg,")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update panduan_ibadah_screen.dart
file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\panduan_ibadah_screen.dart'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("color: theme.isDark ? const Color(0xFF1A3328) : const Color(0xFFEFF6F3),", "color: theme.chipBg,")
content = content.replace("color: theme.isDark ? theme.goldLight : theme.colorScheme.primary,", "color: theme.chipText,")
content = content.replace("color: theme.isDark ? const Color(0xFF182E25) : const Color(0xFFF9FAF8),", "color: theme.arabicBoxBg,")
content = content.replace("color: theme.isDark ? const Color(0xFFF7E7B4) : const Color(0xFF132A22),", "color: theme.arabicText,")
content = content.replace("color: theme.isDark ? const Color(0xFFA5B8AF) : const Color(0xFF07382C),", "color: theme.latinText,")
content = content.replace("color: theme.isDark ? const Color(0xFF1A3328) : const Color(0xFFF1F8F5),", "color: theme.tipsBg,")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

