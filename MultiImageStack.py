import glob
from PIL import Image
#Please Place all images in HW2 folder!

# Searching for images
img = glob.glob('*.png')
pictureObjects = []
pictures = []
newPicture = []
for n in img:
    pictureObjects.append(Image.open(n))# Creates image objects
for i in img:
    pictures.append(Image.open(i).getdata())

width, height = pictureObjects[0].size
# Making a new image
image = Image.new("RGB", (width, height), "white")



x = int(len(pictures)/2) + 1
print(x)
y = 0
for i in pictures[0]:
    pixelsInNewPicture = []
    for n in pictures:
        pixelsInNewPicture.append(n[y])
    pixelsInNewPicture.sort(key = lambda a:(a[0] + a[1] + a[2])/ 3)
    newPicture.append(pixelsInNewPicture[x])
    y += 1

image.putdata(newPicture)
image.save('finalImage.png')
