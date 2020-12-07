from PIL import Image
import sys


def diffrence(original, output):
    original_img = Image.open(original)  # Gets information for public image
    output_img = Image.open(output)  # Gets information for private image
    times = 0

    for x in range(original_img.size[0]):
        for y in range(original_img.size[1]):
            if original_img.getpixel((x, y)) != output_img.getpixel((x, y)):
                times += 1
    print("\nAmount of diffrenct pixels: {0}/{1}".format(times, (original_img.size[0] * original_img.size[1])))


try:
    try:
        diffrence(sys.argv[1], sys.argv[2])

    except FileNotFoundError:
        print("One or both files does not exsist")

except IndexError:
    print("The right uses:")
    print("Python file.py encode img1 img2")
    print("Python file.py decode img")
