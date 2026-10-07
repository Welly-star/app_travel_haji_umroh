import re
import os

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\main_nav_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Prepend theme extraction inside build
if "final theme = Theme.of(context);" not in content:
    content = content.replace("Widget build(BuildContext context) {", "Widget build(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")

content = content.replace("backgroundColor: AppColors.gold,", "backgroundColor: theme.gold,")
content = content.replace("foregroundColor: const Color(0xFF07382C),", "foregroundColor: isDark ? const Color(0xFF132A22) : const Color(0xFF07382C),")

content = content.replace("color: Colors.white,", "color: isDark ? const Color(0xFF11241C) : Colors.white,") # BottomAppBar color

content = content.replace(
    "Widget _buildNavItem(int index, IconData activeIcon, IconData inactiveIcon, String label) {",
    "Widget _buildNavItem(int index, IconData activeIcon, IconData inactiveIcon, String label, ThemeData theme) {"
)

content = content.replace(
    "_buildNavItem(0, Icons.home_rounded, Icons.home_outlined, 'Beranda'),",
    "_buildNavItem(0, Icons.home_rounded, Icons.home_outlined, 'Beranda', theme),"
)
content = content.replace(
    "_buildNavItem(1, Icons.menu_book_rounded, Icons.menu_book_outlined, 'Panduan'),",
    "_buildNavItem(1, Icons.menu_book_rounded, Icons.menu_book_outlined, 'Panduan', theme),"
)
content = content.replace(
    "_buildNavItem(2, Icons.flight_takeoff_rounded, Icons.flight_outlined, 'Jadwal'),",
    "_buildNavItem(2, Icons.flight_takeoff_rounded, Icons.flight_outlined, 'Jadwal', theme),"
)
content = content.replace(
    "_buildNavItem(3, Icons.location_on_rounded, Icons.location_on_outlined, 'Lokasi'),",
    "_buildNavItem(3, Icons.location_on_rounded, Icons.location_on_outlined, 'Lokasi', theme),"
)

content = content.replace("color: isSelected ? AppColors.primary : AppColors.textMuted,", "color: isSelected ? theme.colorScheme.primary : theme.textMuted,")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

