from PIL import Image, ImageOps

def mirror_image(image_path):
    image = Image.open(image_path)
    mirrored_image = ImageOps.mirror(image)
    return mirrored_image

def grayscale_image(image_path):
    image = Image.open(image_path)
    grayscale_image = ImageOps.grayscale(image)
    return grayscale_image

def negative_image(image_path):
    image = Image.open(image_path).convert('RGB')
    negative_image = ImageOps.invert(image)
    return negative_image

def apply_operation(image_path, operation):
    if operation == 'mirror':
        return mirror_image(image_path)
    elif operation == 'grayscale':
        return grayscale_image(image_path)
    elif operation == 'negative':
        return negative_image(image_path)
    else:
        image = Image.open(image_path)
        return image

