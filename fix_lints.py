import re
import os
import subprocess

file_path = '/Users/thanglee/shopify/MISENtest-0304/markdownexport/sections/product-information.liquid'
assets_dir = '/Users/thanglee/shopify/MISENtest-0304/markdownexport/Sculptique-nonLIQUID/assets'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the backslashes in asset_url filters
content = re.sub(r'src="\{\{\s*\\\'(.*?)\\\'\s*\|\s*asset_url\s*\}\}"', r'src="{{ \'\1\' | asset_url }}"', content)

# Replace ui-avatars.com with embedded svg
def replace_avatar(match):
    name = match.group(1)
    svg = f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="12" fill="#E2E8F0"/><text x="12" y="16" font-family="Arial" font-size="12" font-weight="bold" fill="#4A5568" text-anchor="middle">{name}</text></svg>'
    return svg

content = re.sub(r'<img src="https://ui-avatars.com/api/\?name=([A-Z])&background=random"\s*/>', replace_avatar, content)

def process_img(match):
    tag = match.group(0)
    if 'width=' in tag and 'height=' in tag:
        return tag
    
    src_match = re.search(r'src="\{\{\s*\'([^\']+)\'\s*\|\s*asset_url\s*\}\}"', tag)
    if not src_match:
        return tag
    
    filename = src_match.group(1)
    full_path = os.path.join(assets_dir, filename)
    if os.path.exists(full_path):
        try:
            output = subprocess.check_output(['file', full_path]).decode('utf-8')
            dim_match = re.search(r'(\d+)\s*x\s*(\d+)', output)
            if dim_match:
                w, h = dim_match.groups()
                tag = tag.replace('<img', f'<img width="{w}" height="{h}"', 1)
        except:
            pass
    return tag

content = re.sub(r'<img\b[^>]*>', process_img, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied successfully.")
