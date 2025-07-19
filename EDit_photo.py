from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open('car-967470_640.png') as pic_original:
    print('Зображення створено\nРозмір:', pic_original.size)
    print('Формат:', pic_original.mode)
    pic_original.show()


    pic_gray = pic_original.convert('L')
    pic_gray.save('car-967470_640.png')
    print('Зображення створене\nРозмір:', pic_gray.size)
    print('Формат:', pic_gray.format)
    print('Тип:', pic_gray.mode)
    pic_gray.show()


    pic_blured = pic_original.filter(ImageFilter.DETAIL)
    pic_blured.save('car-967470_640.png')
    pic_blured.show()

    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save('car-967470_640.png')
    pic_mirrow.show()


    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save('car-967470_640.png')
    pic_contrast.show()


