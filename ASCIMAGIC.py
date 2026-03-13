from ascii_magic import AsciiArt
from PIL import Image, ImageOps
import random
import os

# load poetry
filename = "data.txt"
if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        raw_text = f.read()
else:
    raw_text = "roses are red violets are blue"

words = raw_text.lower().split()

# invert image
img = Image.open('K_Black.png')
img = ImageOps.invert(img.convert('RGB'))
img.save('K_Inverted.png')

# generate frames
frames = []
column_steps = list(range(5, 120, 5))

for i, cols in enumerate(column_steps):
    random_chars = list(set(" ".join(random.sample(words, min(10, len(words))))))
    random_chars = [c for c in random_chars if c.strip()]
    char_string = "".join(random_chars[:8])

    my_art = AsciiArt.from_image('K_Inverted.png')
    my_art.to_image_file(
        f'frame_{i}.jpg',
        columns=cols,
        char=char_string,
        full_color=True,
        back='#000000'
    )
    frames.append(Image.open(f'frame_{i}.jpg'))
    print(f"frame {i} — columns: {cols} — chars: {char_string}")

# resize and save gif
size = frames[-1].size
frames = [f.resize(size, Image.NEAREST) for f in frames]

frames[0].save(
    'stopmotion.gif',
    save_all=True,
    append_images=frames[1:],
    duration=80,
    loop=0
)

print("saved stopmotion.gif")