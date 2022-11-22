# これOCR用のpython
import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
tool = tools[0]


def ocr(photo):
    img = Image.open(photo)
    txt = tool.image_to_string(
        img, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
    )

    return txt


def save(text):
    with open("ex1.txt", "w") as f:
        f.write(str(text))
