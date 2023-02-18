from PIL import Image


def main():
    im = Image.open("1219391.jpg")
    print(im.format, im.size, im.mode)
    im.show()


if __name__ == '__main__':
    main()
