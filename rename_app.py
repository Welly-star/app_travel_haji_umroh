import os

def update_android_manifest():
    path = "android/app/src/main/AndroidManifest.xml"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace('android:label="app_travel_haji_umroh"', 'android:label="Travel Haji"')
    content = content.replace('android:label="app_travel_haji"', 'android:label="Travel Haji"')
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def update_ios_plist():
    path = "ios/Runner/Info.plist"
    if not os.path.exists(path): return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Replace CFBundleName and CFBundleDisplayName
    content = content.replace('<key>CFBundleDisplayName</key>\n\t<string>app_travel_haji_umroh</string>', '<key>CFBundleDisplayName</key>\n\t<string>Travel Haji</string>')
    content = content.replace('<key>CFBundleDisplayName</key>\n\t<string>app_travel_haji</string>', '<key>CFBundleDisplayName</key>\n\t<string>Travel Haji</string>')
    
    content = content.replace('<key>CFBundleName</key>\n\t<string>app_travel_haji_umroh</string>', '<key>CFBundleName</key>\n\t<string>Travel Haji</string>')
    content = content.replace('<key>CFBundleName</key>\n\t<string>app_travel_haji</string>', '<key>CFBundleName</key>\n\t<string>Travel Haji</string>')
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    update_android_manifest()
    update_ios_plist()

