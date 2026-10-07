import re
import os

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens\home_screen.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure to import main.dart for themeNotifier
if "import '../main.dart';" not in content:
    content = content.replace("import '../theme/app_theme.dart';", "import '../theme/app_theme.dart';\nimport '../main.dart';")

# Prepend theme extraction inside build
if "final theme = Theme.of(context);" not in content:
    content = content.replace("Widget build(BuildContext context) {", "Widget build(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    
    # We also need theme extraction in other methods where we will use `isDark` or `theme`
    content = content.replace("Widget _buildTopHeader(BuildContext context) {", "Widget _buildTopHeader(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    content = content.replace("Widget _buildPrayerTimeCard(BuildContext context) {", "Widget _buildPrayerTimeCard(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    content = content.replace("Widget _buildDepartureCountdownCard(BuildContext context) {", "Widget _buildDepartureCountdownCard(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    content = content.replace("Widget _buildQuickServicesGrid(BuildContext context) {", "Widget _buildQuickServicesGrid(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    content = content.replace("Widget _buildPackagesCarousel(BuildContext context) {", "Widget _buildPackagesCarousel(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    content = content.replace("Widget _buildFeaturedMutawwifCard(BuildContext context) {", "Widget _buildFeaturedMutawwifCard(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")
    
    # daily wisdom doesn't take context. We'll pass context
    content = content.replace("_buildDailyWisdomCard(),", "_buildDailyWisdomCard(context),")
    content = content.replace("Widget _buildDailyWisdomCard() {", "Widget _buildDailyWisdomCard(BuildContext context) {\n    final theme = Theme.of(context);\n    final isDark = theme.isDark;")

# Now string replacements for AppColors -> theme properties
content = content.replace("backgroundColor: AppColors.background,", "backgroundColor: theme.scaffoldBackgroundColor,")
content = content.replace("color: AppColors.textPrimary,", "color: theme.textPrimary,")
content = content.replace("color: AppColors.textSecondary,", "color: theme.textSecondary,")
content = content.replace("color: AppColors.textMuted", "color: theme.textMuted")
content = content.replace("color: AppColors.primaryLight,", "color: isDark ? theme.goldLight : AppColors.primaryLight,")
content = content.replace("AppColors.primaryGradient", "theme.primaryGradient")
content = content.replace("color: AppColors.goldLight,", "color: theme.goldLight,")
content = content.replace("color: AppColors.goldDark,", "color: theme.goldDark,")
content = content.replace("color: AppColors.gold,", "color: theme.gold,")
content = content.replace("color: AppColors.primarySubtle,", "color: theme.primarySubtle,")
content = content.replace("color: AppColors.primary,", "color: theme.colorScheme.primary,")
content = content.replace("color: AppColors.primary.", "color: theme.colorScheme.primary.")
content = content.replace("AppColors.primary.withValues", "theme.colorScheme.primary.withValues")
content = content.replace("color: AppColors.gold.withValues", "color: theme.gold.withValues")
content = content.replace("border: Border.all(color: AppColors.gold.withValues", "border: Border.all(color: theme.gold.withValues")

content = content.replace("color: Colors.white,", "color: theme.cardTheme.color,")
content = content.replace("border: Border.all(color: const Color(0xFFE5EEEA)),", "border: Border.all(color: theme.cardBorder),")
content = content.replace("border: Border.all(color: const Color(0xFFE4EDE8)),", "border: Border.all(color: theme.cardBorder),")
content = content.replace("color: Colors.black.withValues(alpha: 0.06),", "color: theme.cardShadow,")
content = content.replace("color: Colors.black.withValues(alpha: 0.04),", "color: theme.cardShadow,")
content = content.replace("color: Colors.black.withValues(alpha: 0.03),", "color: theme.cardShadow,")
content = content.replace("color: const Color(0xFFEDF2EF)", "color: theme.cardBorder")

# Update Prayer Time Item colors
content = content.replace("color: isNext ? Colors.white : AppColors.textSecondary,", "color: isNext ? Colors.white : theme.textSecondary,")
content = content.replace("color: isNext ? AppColors.goldLight : AppColors.textPrimary,", "color: isNext ? theme.goldLight : theme.textPrimary,")
content = content.replace("color: isNext ? AppColors.primary : Colors.transparent,", "color: isNext ? theme.colorScheme.primary : Colors.transparent,")

# Quick Services Box Background
content = content.replace("color: Colors.white,", "color: theme.cardTheme.color,") # replaced twice maybe, but fine

# Carousel package card border
content = content.replace("color: pkg.isPopular ? AppColors.gold : const Color(0xFFE4EDE8),", "color: pkg.isPopular ? theme.gold : theme.cardBorder,")
content = content.replace("backgroundColor: AppColors.primary,", "backgroundColor: theme.colorScheme.primary,")

# Featured mutawwif
content = content.replace("color: AppColors.primarySubtle,", "color: theme.primarySubtle,")
content = content.replace("backgroundColor: AppColors.primarySubtle,", "backgroundColor: theme.primarySubtle,")

# Wisdom Card
content = content.replace("color: const Color(0xFFFBF8EE),", "color: isDark ? const Color(0xFF182E25) : const Color(0xFFFBF8EE),")
content = content.replace("color: AppColors.gold.withValues(alpha: 0.3)", "color: theme.gold.withValues(alpha: 0.3)")


# Insert dark mode toggle in the Top Header Actions
target_actions = '''                  Container(
                    width: 38,
                    height: 38,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      border: Border.all(color: AppColors.gold, width: 1.5),
                      color: Colors.white.withValues(alpha: 0.2),
                    ),
                    child: const Center(
                      child: Icon(Icons.person, color: Colors.white, size: 20),
                    ),
                  ),'''
                  
replacement_actions = '''                  // Dark mode toggle
                  ValueListenableBuilder<ThemeMode>(
                    valueListenable: themeNotifier,
                    builder: (context, currentMode, _) {
                      final isDarkMode = currentMode == ThemeMode.dark || (currentMode == ThemeMode.system && isDark);
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
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      border: Border.all(color: theme.gold, width: 1.5),
                      color: Colors.white.withValues(alpha: 0.2),
                    ),
                    child: const Center(
                      child: Icon(Icons.person, color: Colors.white, size: 20),
                    ),
                  ),'''

content = content.replace(target_actions, replacement_actions)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

