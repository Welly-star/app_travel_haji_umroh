import yaml

def update_pubspec():
    with open("pubspec.yaml", "r") as f:
        lines = f.readlines()
        
    # Find assets section and replace with just - assets/
    new_lines = []
    in_assets = False
    for line in lines:
        if line.strip().startswith('assets:'):
            in_assets = True
            new_lines.append(line)
            new_lines.append('    - assets/\n')
            continue
        if in_assets:
            if line.strip().startswith('- assets/'):
                continue # Skip specific assets
            if not line.startswith(' ') and line.strip() != '':
                in_assets = False
        if not in_assets:
            new_lines.append(line)
            
    # Append configs
    config = """
flutter_launcher_icons:
  android: true
  ios: true
  image_path: "assets/icon.png"
  adaptive_icon_background: "#0D5C46"
  adaptive_icon_foreground: "assets/icon_foreground.png"

flutter_native_splash:
  color: "#0D5C46"
  image: "assets/splash.png"
  android: true
  ios: true
  android_12:
    image: "assets/splash.png"
    icon_background_color: "#0D5C46"
"""
    new_lines.append(config)
    
    with open("pubspec.yaml", "w") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    update_pubspec()

