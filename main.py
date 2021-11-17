from PIL import Image, ImageDraw, ImageFont


def xp_bar(percentage: float, level: int, save_path: str = "./xp_bar.png") -> None:
    # load the images
    img1 = Image.open('images/xp_bar_full.png')
    img2 = Image.open('images/xp_bar_empty.png')
    # get the size of the image
    width, height = img1.size
    # crop the image at the given percentage
    cropped_width = int(width*percentage)
    # crop the image
    img1 = img1.crop((0, 0, cropped_width, height))
    img2 = img2.crop((cropped_width, 0, width, height))
    # paste the cropped image on the other image
    new_image = Image.new('RGBA', (width, height), (0,0,0,0))
    new_image.paste(img1,(0,0))
    new_image.paste(img2,(cropped_width,0))
    # draw the number
    _draw_number(new_image, level, save_path)


def _draw_number(image: Image, number: int, save_path: str) -> None:
    # convert number to string
    number = str(number)
    # load the font
    font = ImageFont.truetype("fonts/minecraft_font.ttf", size=14)
    # get the size of the text
    text_size = font.getsize(number)
    # calculate the position of the text
    text_x = (image.width - text_size[0]) / 2
    text_y = (image.height - text_size[1]) / 2 -7
    # draw the text on the image
    draw = ImageDraw.Draw(image)
    draw.text((text_x+2, text_y+2), number, font=font, fill=(32, 64, 0))
    draw.text((text_x, text_y), number, font=font, fill=(127, 255, 0))
    # save the image
    image.save(save_path)