import pyocr
from PIL import Image
import cv2
import numpy as np

tools = pyocr.get_available_tools()
tool = tools[0]
photo = "static/images/image.jpeg"


def ocr(photo):
    img = Image.open(photo)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 2値化（100:２値化の閾値／画像を見て調整する）
    ret, thresh1 = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
    # ノイズ処理（モルフォロジー変換）
    kernel = np.ones((5, 5), np.uint8)
    img_after = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

    new_image = img_after.copy()
    if new_image.ndim == 2:
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(img_after, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(img_after, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)

    txt = tool.image_to_string(
        new_image,
        lang="jpn",
        builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
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


out = display(photo)
print(out)
