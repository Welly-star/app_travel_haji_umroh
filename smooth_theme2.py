import re

file_path = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\theme\app_theme.dart'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

theme_extension_code = '''
@immutable
class AppCustomColors extends ThemeExtension<AppCustomColors> {
  final Color gold;
  final Color goldLight;
  final Color goldDark;
  final Color cardBorder;
  final Color cardShadow;
  final Color textMuted;
  final Color success;
  final Color warning;
  final Color error;
  
  final Color fabForeground;
  final Color bottomNavBg;
  final Color wisdomCardBg;
  final Color chipBg;
  final Color chipText;
  final Color arabicBoxBg;
  final Color arabicText;
  final Color latinText;
  final Color tipsBg;

  const AppCustomColors({
    required this.gold,
    required this.goldLight,
    required this.goldDark,
    required this.cardBorder,
    required this.cardShadow,
    required this.textMuted,
    required this.success,
    required this.warning,
    required this.error,
    required this.fabForeground,
    required this.bottomNavBg,
    required this.wisdomCardBg,
    required this.chipBg,
    required this.chipText,
    required this.arabicBoxBg,
    required this.arabicText,
    required this.latinText,
    required this.tipsBg,
  });

  @override
  AppCustomColors copyWith({
    Color? gold,
    Color? goldLight,
    Color? goldDark,
    Color? cardBorder,
    Color? cardShadow,
    Color? textMuted,
    Color? success,
    Color? warning,
    Color? error,
    Color? fabForeground,
    Color? bottomNavBg,
    Color? wisdomCardBg,
    Color? chipBg,
    Color? chipText,
    Color? arabicBoxBg,
    Color? arabicText,
    Color? latinText,
    Color? tipsBg,
  }) {
    return AppCustomColors(
      gold: gold ?? this.gold,
      goldLight: goldLight ?? this.goldLight,
      goldDark: goldDark ?? this.goldDark,
      cardBorder: cardBorder ?? this.cardBorder,
      cardShadow: cardShadow ?? this.cardShadow,
      textMuted: textMuted ?? this.textMuted,
      success: success ?? this.success,
      warning: warning ?? this.warning,
      error: error ?? this.error,
      fabForeground: fabForeground ?? this.fabForeground,
      bottomNavBg: bottomNavBg ?? this.bottomNavBg,
      wisdomCardBg: wisdomCardBg ?? this.wisdomCardBg,
      chipBg: chipBg ?? this.chipBg,
      chipText: chipText ?? this.chipText,
      arabicBoxBg: arabicBoxBg ?? this.arabicBoxBg,
      arabicText: arabicText ?? this.arabicText,
      latinText: latinText ?? this.latinText,
      tipsBg: tipsBg ?? this.tipsBg,
    );
  }

  @override
  AppCustomColors lerp(ThemeExtension<AppCustomColors>? other, double t) {
    if (other is! AppCustomColors) {
      return this;
    }
    return AppCustomColors(
      gold: Color.lerp(gold, other.gold, t)!,
      goldLight: Color.lerp(goldLight, other.goldLight, t)!,
      goldDark: Color.lerp(goldDark, other.goldDark, t)!,
      cardBorder: Color.lerp(cardBorder, other.cardBorder, t)!,
      cardShadow: Color.lerp(cardShadow, other.cardShadow, t)!,
      textMuted: Color.lerp(textMuted, other.textMuted, t)!,
      success: Color.lerp(success, other.success, t)!,
      warning: Color.lerp(warning, other.warning, t)!,
      error: Color.lerp(error, other.error, t)!,
      fabForeground: Color.lerp(fabForeground, other.fabForeground, t)!,
      bottomNavBg: Color.lerp(bottomNavBg, other.bottomNavBg, t)!,
      wisdomCardBg: Color.lerp(wisdomCardBg, other.wisdomCardBg, t)!,
      chipBg: Color.lerp(chipBg, other.chipBg, t)!,
      chipText: Color.lerp(chipText, other.chipText, t)!,
      arabicBoxBg: Color.lerp(arabicBoxBg, other.arabicBoxBg, t)!,
      arabicText: Color.lerp(arabicText, other.arabicText, t)!,
      latinText: Color.lerp(latinText, other.latinText, t)!,
      tipsBg: Color.lerp(tipsBg, other.tipsBg, t)!,
    );
  }
}

final lightCustomColors = AppCustomColors(
  gold: AppColors.gold,
  goldLight: AppColors.goldLight,
  goldDark: AppColors.goldDark,
  cardBorder: const Color(0xFFE2ECE7),
  cardShadow: Colors.black.withValues(alpha: 0.04),
  textMuted: const Color(0xFF8FA39B),
  success: const Color(0xFF10B981),
  warning: const Color(0xFFF59E0B),
  error: const Color(0xFFEF4444),
  fabForeground: const Color(0xFF07382C),
  bottomNavBg: Colors.white,
  wisdomCardBg: const Color(0xFFFBF8EE),
  chipBg: const Color(0xFFEFF6F3),
  chipText: AppColors.primary,
  arabicBoxBg: const Color(0xFFF9FAF8),
  arabicText: const Color(0xFF132A22),
  latinText: const Color(0xFF07382C),
  tipsBg: const Color(0xFFF1F8F5),
);

final darkCustomColors = AppCustomColors(
  gold: AppColors.gold,
  goldLight: AppColors.goldLight,
  goldDark: AppColors.goldDark,
  cardBorder: const Color(0xFF264035),
  cardShadow: Colors.black.withValues(alpha: 0.3),
  textMuted: const Color(0xFF6B7F76),
  success: const Color(0xFF10B981),
  warning: const Color(0xFFF59E0B),
  error: const Color(0xFFEF4444),
  fabForeground: const Color(0xFF132A22),
  bottomNavBg: const Color(0xFF11241C),
  wisdomCardBg: const Color(0xFF182E25),
  chipBg: const Color(0xFF1A3328),
  chipText: AppColors.goldLight,
  arabicBoxBg: const Color(0xFF182E25),
  arabicText: const Color(0xFFF7E7B4),
  latinText: const Color(0xFFA5B8AF),
  tipsBg: const Color(0xFF1A3328),
);
'''

content = content.replace("class AppTheme {", theme_extension_code + "\nclass AppTheme {")
content = content.replace("elevatedButtonTheme: _elevatedButtonTheme,\n    );", "elevatedButtonTheme: _elevatedButtonTheme,\n      extensions: [lightCustomColors],\n    );", 1)
content = content.replace("elevatedButtonTheme: _elevatedButtonTheme,\n    );", "elevatedButtonTheme: _elevatedButtonTheme,\n      extensions: [darkCustomColors],\n    );", 1)

new_extension = '''extension ThemeColors on ThemeData {
  bool get isDark => brightness == Brightness.dark;
  
  AppCustomColors get _custom => extension<AppCustomColors>()!;
  
  Color get gold => _custom.gold;
  Color get goldLight => _custom.goldLight;
  Color get goldDark => _custom.goldDark;
  
  Color get cardBorder => _custom.cardBorder;
  Color get cardShadow => _custom.cardShadow;
  
  Color get primarySubtle => colorScheme.surfaceContainerHighest;
  Color get textPrimary => colorScheme.onSurface;
  Color get textSecondary => colorScheme.onSurfaceVariant;
  Color get textMuted => _custom.textMuted;
  
  Color get success => _custom.success;
  Color get warning => _custom.warning;
  Color get error => _custom.error;
  
  Color get fabForeground => _custom.fabForeground;
  Color get bottomNavBg => _custom.bottomNavBg;
  Color get wisdomCardBg => _custom.wisdomCardBg;
  Color get chipBg => _custom.chipBg;
  Color get chipText => _custom.chipText;
  Color get arabicBoxBg => _custom.arabicBoxBg;
  Color get arabicText => _custom.arabicText;
  Color get latinText => _custom.latinText;
  Color get tipsBg => _custom.tipsBg;
  
  LinearGradient get primaryGradient => isDark 
      ? const LinearGradient(colors: [Color(0xFF09291F), Color(0xFF041711)], begin: Alignment.topLeft, end: Alignment.bottomRight)
      : const LinearGradient(colors: [Color(0xFF0D5C46), Color(0xFF063A2C)], begin: Alignment.topLeft, end: Alignment.bottomRight);
}'''

content = re.sub(r'extension ThemeColors on ThemeData \{.*\}', new_extension, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

