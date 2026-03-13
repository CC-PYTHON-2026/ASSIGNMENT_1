from ascii_magic import AsciiArt
from PIL import Image, ImageOps

img = Image.open('K_Black.png')
ImageOps.invert(img.convert('RGB')).save('K_Inverted.png')

my_art = AsciiArt.from_image('K_Inverted.png')
my_art.to_image_file('output.jpg', columns=120, char='k,a,z,i.a,r,s,h,#,!,@,^,%,$,*,&', full_color=True, back='#000000')

print("saved output.jpg")