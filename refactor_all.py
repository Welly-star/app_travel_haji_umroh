import os

screens_dir = r'c:\Users\user\Downloads\app_travel_haji_umroh-main\app_travel_haji_umroh-main\lib\screens'
files_to_refactor = [
    'digital_tasbih_screen.dart', 
    'formulir_pendaftaran_screen.dart', 
    'jadwal_penerbangan_screen.dart', 
    'kontak_petugas_screen.dart', 
    'lokasi_penting_screen.dart'
]

for file in files_to_refactor:
    path = os.path.join(screens_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Prepend theme extraction inside build if not present
    if "final theme = Theme.of(context);" not in content:
        content = content.replace("Widget build(BuildContext context) {", "Widget build(BuildContext context) {\n    final theme = Theme.of(context);")

    # Add other build functions
    content = content.replace("Widget _buildStep(BuildContext context,", "Widget _buildStep(BuildContext context,")
    
    # Generic replacements
    content = content.replace("AppColors.background", "theme.scaffoldBackgroundColor")
    content = content.replace("AppColors.textPrimary", "theme.textPrimary")
    content = content.replace("AppColors.textSecondary", "theme.textSecondary")
    content = content.replace("AppColors.textMuted", "theme.textMuted")
    content = content.replace("AppColors.primaryLight", "theme.primaryLight") # Wait, is primaryLight in theme? No. We can use theme.colorScheme.primary.withOpacity or something. Let's add primaryLight to ThemeColors extension.
    # We will add primaryLight to theme later. Let's just use theme.colorScheme.primary
    content = content.replace("AppColors.primaryLight", "theme.colorScheme.primary")
    content = content.replace("AppColors.primaryGradient", "theme.primaryGradient")
    content = content.replace("AppColors.goldLight", "theme.goldLight")
    content = content.replace("AppColors.goldDark", "theme.goldDark")
    content = content.replace("AppColors.gold", "theme.gold")
    content = content.replace("AppColors.primarySubtle", "theme.primarySubtle")
    content = content.replace("AppColors.primary", "theme.colorScheme.primary")
    
    content = content.replace("color: Colors.white", "color: theme.cardTheme.color")
    # specifically for cards
    content = content.replace("color: const Color(0xFFE5EEEA)", "color: theme.cardBorder")
    content = content.replace("color: const Color(0xFFE4EDE8)", "color: theme.cardBorder")
    content = content.replace("color: Colors.black.withValues(alpha: 0.06)", "color: theme.cardShadow")
    content = content.replace("color: Colors.black.withValues(alpha: 0.04)", "color: theme.cardShadow")
    content = content.replace("color: Colors.black.withValues(alpha: 0.03)", "color: theme.cardShadow")
    content = content.replace("color: Colors.black.withValues(alpha: 0.05)", "color: theme.cardShadow")
    content = content.replace("const Color(0xFFEDF2EF)", "theme.cardBorder")
    content = content.replace("const Color(0xFFE2ECE7)", "theme.cardBorder")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")

