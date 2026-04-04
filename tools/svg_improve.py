# This script inserts a white rectangle into all SVG files in subdirectories of '../img'
# to improve visibility when displayed on dark backgrounds.
# It checks if the rectangle already exists to avoid duplicate insertions.
# The rectangle is defined with 100% width and height, filled with white and with a transparent stroke.



import re
import os

def insert_rectangle(file : str):
    rect = '<rect *width="100%" *height="100%" *fill="white" *stroke="transparent"/>'

    with open(file, 'r') as f:
        content = f.read()
    if re.search(rect, content):
        print(f"File '{file}' already contains the rectangle. Skipping.")
        return

    # Find the position to insert the rectangle (after the opening <svg> tag)
    insert_pos = re.search("<svg[^>]*>", content).end()

    # Define the rectangle element
    rectangle = '''
    <!-- Inserted rectangle to improve visibility -->
    <rect width="100%" height="100%" fill="white" stroke="transparent"/>
    '''

    # Insert the rectangle into the SVG content
    new_content = content[:insert_pos] + rectangle + content[insert_pos:]

    # Write the modified content back to the file
    with open(file, 'w') as f:
        f.write(new_content)

    print(f"File '{file}' was successfully written.")

if __name__ == "__main__":
    for r, d, fs in os.walk('../img'):
        for f in fs:
            if f.endswith('.svg'):
                insert_rectangle(os.path.join(r, f))