#LIBS---------------------------------------------------------------------

import os
import random
import time
from fpdf import FPDF

#PDF-----------------------------------------------------------------------

filename = "data.txt"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as file:
        raw_text = file.read()
else:
    raw_text = """roses are red,
    violets are blue,
    there is no file,
    here is a poem for you"""

raw_text = raw_text.replace("—", "-")

lines = raw_text.split("\n")
random_characters = ["♡", "•", "◦", "→", "←", "↑", "↓", "★", "☆", "◇", "◆", "○", "●"]

def make_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf")
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(0, 0, pdf.w, pdf.h, "F")
    pdf.set_text_color(89, 0, 153)
    pdf.set_font("DejaVu", size=10)
    pdf.set_char_spacing(1)
    pdf.multi_cell(0, 5, text=text, align= "L")
    pdf.output("poem.pdf")




#POETRY EDIT ---------------------------------------------------------------------------------------

output = ""

for _ in range(random.randint(50, 58)):
    spaces = " " * random.randint(0, 15)
    line = random.choice(lines).lower()
    words = line.split(" ")
    random.shuffle(words)

    if random.random() < 0.6:
        insert_char = random.randint(0, len(words))
        words.insert(insert_char, random.choice(random_characters))

    line = " ".join(words)
    final_line = spaces + line
    print(final_line)
    output += final_line + "\n"


make_pdf(output)