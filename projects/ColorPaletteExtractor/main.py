from PIL import Image
from numpy import array

img = Image.open("assets/qr.png")

img_data = array(img)

colors = {}

for row in img_data:
    for r, g, b, a in row:
        colors[(r, g, b, a)] = colors.get((r, g, b, a), 0) + 1

top_colors = sorted(colors.items())[:10]

print("These are the top 10 most used colors:")

for (r, g, b, a), _ in top_colors:
    print(r, g, b)
