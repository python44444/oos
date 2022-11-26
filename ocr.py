import pyocr
from PIL import Image
import cv2
import numpy as np

tools = pyocr.get_available_tools()
tool = tools[0]
photo = "static/images/image.jpeg"


def cv2pil(image):
    """OpenCV型 -> PIL型"""
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif new_image.shape[2] == 4:  # 透過
        new_image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    new_image = Image.fromarray(new_image)
    return new_image


def ocr(photo):
    img = cv2.imread(photo)

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("static/images/gray.jpeg", img_gray)

    img_reverse = 255 - img_gray
    cv2.imwrite("static/image/reverse.jpeg", img_reverse)

    # 2値化（100:２値化の閾値／画像を見て調整する）
    ret, thresh1 = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY)
    # ノイズ処理（モルフォロジー変換
    kernel = np.ones((2, 7), np.uint8)
    img_opening = cv2.dilate(thresh1, kernel)
    # img_opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)

    image = cv2pil(img_opening)
    image.save("static/images/pillow.jpeg")

    txt = tool.image_to_string(
        image, lang="jpn", builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
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
