import os
from PIL import Image


def image_directories():
    current_working_directory = os.getcwd()
    return [
        os.path.join(current_working_directory, 'patterns/converted-html/assets/img'),
        os.path.join(current_working_directory, 'storage/images'),
        os.path.join(current_working_directory, 'di_website/static'),
        os.path.join(current_working_directory, 'assets/img')
    ]


def convert_to_webp(image_path):
    try:
        image = Image.open(image_path)
        if image_path.lower().endswith((".jpg", ".jpeg", ".png")):
            webp_path = os.path.splitext(image_path)[0] + ".webp"
            image.save(webp_path, "WebP")
    except Exception as e:
        print('Cannot convert {}: {}'.format(image_path, str(e)))


def convert_images_to_webp():
    directories = image_directories()
    for dir in directories:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):  # Add more extensions if required
                    image_path = os.path.join(root, file)
                    convert_to_webp(image_path)


convert_images_to_webp()
