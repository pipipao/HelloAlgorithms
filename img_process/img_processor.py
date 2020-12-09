from PIL import Image


def testProcessImg():
    img = Image.open('../imgs/mainpic.jpg')
    k = 5
    x, y = img.size
    img.show()
    newImg = img.resize((x, y), Image.NEAREST)
    newImg.show()
    newImg.save('../imgs/resize.jpg','JPEG',qulity=1)
    nail = img.thumbnail((x, y))
    img.show()
    img.save('../imgs/nail.jpg','JPEG',quality=20)


if __name__ == '__main__':
    testProcessImg()
