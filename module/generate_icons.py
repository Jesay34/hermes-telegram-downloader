"""Generate PWA icons for Telegram Downloader"""
from PIL import Image, ImageDraw
import os

# Icon design: blue gradient circle with white download arrow
def create_icon(size, maskable=False):
    """Create icon PNG
    
    maskable: if True, content is larger and centered for adaptive icons
    """
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate dimensions based on maskable flag
    if maskable:
        # Maskable icons need larger content in center
        margin = int(size * 0.15)
    else:
        margin = int(size * 0.1)
    
    # Draw background circle/squircle
    # Use a blue gradient effect by drawing multiple circles
    bg_color = (37, 99, 235)  # #2563eb
    if maskable:
        # For maskable, use full square with rounded corners
        radius = int(size * 0.15)
        draw.rounded_rectangle([margin, margin, size-margin, size-margin], 
                              radius=radius, fill=bg_color)
    else:
        # Regular icon: circle
        draw.ellipse([margin, margin, size-margin, size-margin], fill=bg_color)
    
    # Draw download arrow (white)
    arrow_color = (255, 255, 255)
    center_x = size // 2
    
    # Arrow dimensions
    if maskable:
        arrow_width = int(size * 0.08)
        arrow_height = int(size * 0.4)
        arrow_top = int(size * 0.35)
    else:
        arrow_width = int(size * 0.06)
        arrow_height = int(size * 0.35)
        arrow_top = int(size * 0.3)
    
    arrow_bottom = arrow_top + arrow_height
    
    # Vertical line of arrow
    draw.rectangle([center_x - arrow_width//2, arrow_top, 
                   center_x + arrow_width//2, arrow_bottom], 
                  fill=arrow_color)
    
    # Arrow head (triangle pointing down)
    head_width = int(size * 0.25) if maskable else int(size * 0.2)
    head_height = int(size * 0.15) if maskable else int(size * 0.12)
    
    draw.polygon([
        (center_x - head_width//2, arrow_bottom - head_height//2),
        (center_x + head_width//2, arrow_bottom - head_height//2),
        (center_x, arrow_bottom + head_height//2)
    ], fill=arrow_color)
    
    return img

# Generate icons
output_dir = os.path.join(os.path.dirname(__file__), 'static', 'icons')
os.makedirs(output_dir, exist_ok=True)

# Regular icons
for size in [192, 512]:
    icon = create_icon(size, maskable=False)
    icon.save(os.path.join(output_dir, f'icon-{size}.png'), 'PNG')
    print(f'Created icon-{size}.png')

# Maskable icons (larger, centered content)
for size in [192, 512]:
    icon = create_icon(size, maskable=True)
    icon.save(os.path.join(output_dir, f'icon-maskable-{size}.png'), 'PNG')
    print(f'Created icon-maskable-{size}.png')

# Apple touch icon (180x180)
icon = create_icon(180, maskable=False)
icon.save(os.path.join(output_dir, 'icon-180.png'), 'PNG')
print('Created icon-180.png')

print('All icons generated!')
