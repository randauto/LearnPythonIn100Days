from PIL import Image

from resizeimage import resizeimage


with open("F:\G3Documents\MovePic\API\Sticker\Gif\Gif\Birthday\\test\\3.gif", 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_thumbnail(image, [150, 150], resample=Image.ANTIALIAS)
        cover.save('F:\G3Documents\MovePic\API\Sticker\Gif\Gif\Birthday\\2out.gif', image.format)
        cover.clo