#ImageTrans

#The goal here is to change the background of Anousheh's images from white to the cream color used in my presetnation background 

from PIL import Image
from pathlib import Path

path = Path('Desktop/biomouse.png')

print(path)

img = Image.open(path)

img = img.convert("RGB")
d = img.getdata()
print(type(img))

new_image = []

#This is the range of pixels that you will want to replace. In this case, I am replacing "white" pixels. 
#You will need to change this to the range of RGB values you can expect. 
#The reason it is a range is that some images use pixels that are close but not quite the same. 
min = 238
max = 255
#these are the lines I added to try to solve the issue
colorRange = list()
for n in range(min, max+1):
    for o in range(min, max+1):
        for p in range(min, max+1):
            colorRange.append((n, o, p))
######################################################


for item in d:

    if item in colorRange:
        new_image.append((239, 235, 225))

    else:
        new_image.append(item)

img.putdata(new_image)

# x = image_trans(img)
im = img.save("Desktop/biomouse2.png")

