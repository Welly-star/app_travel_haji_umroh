import re

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("const Icon(Icons.support_agent_rounded, color: theme.cardTheme.color, size: 22)", "Icon(Icons.support_agent_rounded, color: Colors.white, size: 22)")
content = content.replace("Icon(Icons.person, color: theme.cardTheme.color, size: 20)", "Icon(Icons.person, color: Colors.white, size: 20)")
content = content.replace("const Icon(Icons.person, color: theme.cardTheme.color, size: 20)", "Icon(Icons.person, color: Colors.white, size: 20)")
content = content.replace("const Icon(Icons.flight_takeoff_rounded, color: theme.goldLight, size: 24)", "Icon(Icons.flight_takeoff_rounded, color: theme.goldLight, size: 24)")

# For unused isDark variables, they are at the top of several methods. Let's just remove them entirely and put them back only where needed.
# Since it's a bit tricky with string replace, let's just do a regex replace to remove 'final isDark = theme.isDark;' everywhere, then put it back where it's used.
content = re.sub(r' *final isDark = theme\.isDark;\n', '', content)

# But wait, it IS used in _buildDailyWisdomCard and _buildTopHeader!
# Let's restore it in the specific functions that actually use it.
if "isDark ?" in content:
    content = content.replace("Widget _buildTopHeader(BuildContext context) {\n    final theme = Theme.of(context);", "Widget _buildTopHeader(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    content = content.replace("Widget _buildDailyWisdomCard(BuildContext context) {\n    final theme = Theme.of(context);", "Widget _buildDailyWisdomCard(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")

# Also main nav might have unused import? No, it was home_screen.
content = content.replace("import '../main.dart';\n", "")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

