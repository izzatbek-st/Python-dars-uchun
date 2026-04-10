from PIL import Image

img = Image.open("fon.jpg")
newimg = img.resize((900,900))
img.show()

print(newimg.size)
newimg.save("fon-razmer-o'zga.jpg") 