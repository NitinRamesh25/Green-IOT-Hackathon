import qrcode
import os


def generate(text, image_path, image_name):
    if not os.path.exists(image_path):
        os.mkdir(image_path)

    image = qrcode.make(text)
    image.save('{}/{}.jpg'.format(image_path, image_name))
