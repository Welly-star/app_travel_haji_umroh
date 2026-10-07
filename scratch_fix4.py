import re

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''                  Container(
                    width: 38,
                    height: 38,
                    decoration: BoxDecoration('''
replacement = '''                  // Dark mode toggle
                  ValueListenableBuilder<ThemeMode>(
                    valueListenable: themeNotifier,
                    builder: (context, currentMode, _) {
                      final isDarkMode = currentMode == ThemeMode.dark || (currentMode == ThemeMode.system && Theme.of(context).isDark);
                      return IconButton(
                        onPressed: () {
                          themeNotifier.value = isDarkMode ? ThemeMode.light : ThemeMode.dark;
                        },
                        icon: Icon(isDarkMode ? Icons.light_mode_rounded : Icons.dark_mode_rounded, color: Colors.white, size: 22),
                        tooltip: 'Ganti Tema',
                      );
                    },
                  ),
                  Container(
                    width: 38,
                    height: 38,
                    decoration: BoxDecoration('''
content = content.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

