import re

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 'const' issues
content = content.replace("const Icon(Icons.calendar_month_rounded, color: theme.goldLight, size: 14)", "Icon(Icons.calendar_month_rounded, color: theme.goldLight, size: 14)")
content = content.replace("const Icon(Icons.support_agent_rounded, color: Colors.white, size: 22)", "Icon(Icons.support_agent_rounded, color: Colors.white, size: 22)")
content = content.replace("const Icon(Icons.access_time_filled_rounded, color: theme.colorScheme.primary, size: 18)", "Icon(Icons.access_time_filled_rounded, color: theme.colorScheme.primary, size: 18)")
content = content.replace("const Icon(Icons.flight_takeoff_rounded, color: theme.goldLight, size: 24)", "Icon(Icons.flight_takeoff_rounded, color: theme.goldLight, size: 24)")
content = content.replace("const Icon(Icons.arrow_forward_ios_rounded, color: theme.goldLight, size: 16)", "Icon(Icons.arrow_forward_ios_rounded, color: theme.goldLight, size: 16)")
content = content.replace("const Icon(Icons.hotel_rounded, size: 14, color: theme.goldDark)", "Icon(Icons.hotel_rounded, size: 14, color: theme.goldDark)")
content = content.replace("const Icon(Icons.verified, color: theme.colorScheme.primary, size: 16)", "Icon(Icons.verified, color: theme.colorScheme.primary, size: 16)")
content = content.replace("const Icon(Icons.chat_bubble_outline_rounded, color: theme.colorScheme.primary, size: 18)", "Icon(Icons.chat_bubble_outline_rounded, color: theme.colorScheme.primary, size: 18)")
content = content.replace("const Icon(Icons.format_quote_rounded, color: theme.goldDark, size: 22)", "Icon(Icons.format_quote_rounded, color: theme.goldDark, size: 22)")
content = content.replace("const BoxDecoration(\n        gradient: theme.primaryGradient,", "BoxDecoration(\n        gradient: theme.primaryGradient,")
content = content.replace("const Icon(Icons.person, color: theme.colorScheme.primary, size: 36)", "Icon(Icons.person, color: theme.colorScheme.primary, size: 36)")
content = content.replace("color: isNext ? Colors.white : theme.textSecondary,", "color: isNext ? Colors.white : Theme.of(context).textSecondary,")
content = content.replace("color: isNext ? theme.goldLight : theme.textPrimary,", "color: isNext ? Theme.of(context).goldLight : Theme.of(context).textPrimary,")
content = content.replace("color: isNext ? theme.colorScheme.primary : Colors.transparent,", "color: isNext ? Theme.of(context).colorScheme.primary : Colors.transparent,")

# Pass context to buildPrayerItem
content = content.replace("_buildPrayerItem('Subuh', '04:32', false),", "_buildPrayerItem(context, 'Subuh', '04:32', false),")
content = content.replace("_buildPrayerItem('Dzuhur', '11:58', false),", "_buildPrayerItem(context, 'Dzuhur', '11:58', false),")
content = content.replace("_buildPrayerItem('Ashar', '15:20', true),", "_buildPrayerItem(context, 'Ashar', '15:20', true),")
content = content.replace("_buildPrayerItem('Maghrib', '18:05', false),", "_buildPrayerItem(context, 'Maghrib', '18:05', false),")
content = content.replace("_buildPrayerItem('Isya', '19:16', false),", "_buildPrayerItem(context, 'Isya', '19:16', false),")

content = content.replace("Widget _buildPrayerItem(String name, String time, bool isNext) {", "Widget _buildPrayerItem(BuildContext context, String name, String time, bool isNext) {")


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

