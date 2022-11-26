import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
tool = tools[0]
# photo = "static/images/image.jpeg"


def ocr(photo):
    img = Image.open(photo)
    txt = tool.image_to_string(
        img,
        lang="jpn",
        builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
        # img, lang="jpn", builder=pyocr.builders.DigitBuilder()
    )
    return txt


def save(text):
    with open("ex1.txt", "w") as f:
        f.write(str(text))


def display(photo):
    distance = ocr(photo)
    save(distance)
    f = open("ex1.txt", "r", encoding="UTF-8")
    out = f.read()
    return out


# out = display(photo)
# print(out)
