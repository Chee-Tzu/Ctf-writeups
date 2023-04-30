from PIL import Image

# Open the image
image = Image.open('intro_to_c.png')

# Get the RGB values of each pixel
pixels = image.load()
width, height = image.size
rgb_values = []
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        rgb_values.append(f"RGB({r},{g},{b})")

# Write the RGB values to a file
with open('output.txt', 'w') as f:
    for rgb in rgb_values:
        f.write(rgb + '\n')