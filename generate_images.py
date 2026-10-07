import os
from PIL import Image, ImageDraw, ImageFont

def create_images():
    os.makedirs('assets', exist_ok=True)
    
    # Create simple solid background icon
    icon = Image.new('RGB', (1024, 1024), color='#0D5C46')
    draw = ImageDraw.Draw(icon)
    # Draw a simple gold circle or something
    draw.ellipse((256, 256, 768, 768), outline='#D4AF37', width=40)
    icon.save('assets/icon.png')
    
    # Foreground icon with transparent bg
    fg = Image.new('RGBA', (1024, 1024), color=(0, 0, 0, 0))
    draw_fg = ImageDraw.Draw(fg)
    draw_fg.ellipse((256, 256, 768, 768), outline='#D4AF37', width=40)
    fg.save('assets/icon_foreground.png')
    
    # Splash screen
    splash = Image.new('RGB', (1024, 1024), color='#0D5C46')
    draw_splash = ImageDraw.Draw(splash)
    draw_splash.ellipse((384, 384, 640, 640), outline='#D4AF37', width=20)
    splash.save('assets/splash.png')

if __name__ == "__main__":
    create_images()

