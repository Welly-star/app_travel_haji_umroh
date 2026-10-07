import 'dart:io';

def refactor_login_page():
    path = "lib/screens/login_page.dart"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replacements
    content = content.replace("backgroundColor: AppColors.background,", "backgroundColor: Theme.of(context).scaffoldBackgroundColor,")
    content = content.replace("color: Colors.white,", "color: Theme.of(context).cardTheme.color,")
    content = content.replace("unselectedLabelColor: AppColors.textSecondary,", "unselectedLabelColor: Theme.of(context).extension<AppCustomColors>()!.textMuted,")
    content = content.replace("color: AppColors.textPrimary,", "color: Theme.of(context).extension<AppCustomColors>()!.textPrimary ?? AppColors.textPrimary,")
    content = content.replace("color: AppColors.textSecondary", "color: Theme.of(context).extension<AppCustomColors>()!.textMuted")
    
    # We should just do a careful replace of colors based on theme.
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    refactor_login_page()

