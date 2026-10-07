import re

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all isDark with theme.isDark
content = content.replace("isDark ?", "theme.isDark ?")
content = content.replace("isDark)", "theme.isDark)")

# Remove unused final isDark
content = re.sub(r' *final isDark = theme\.isDark;\n', '', content)

# Fix const Center
content = content.replace("const Center(\n              child: Icon(Icons.flight_takeoff_rounded, color: theme.goldLight, size: 24),\n            )", "Center(\n              child: Icon(Icons.flight_takeoff_rounded, color: theme.goldLight, size: 24),\n            )")
content = content.replace("const Center(\n                      child: Icon(Icons.person, color: Colors.white, size: 20),\n                    )", "Center(\n                      child: Icon(Icons.person, color: Colors.white, size: 20),\n                    )")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

