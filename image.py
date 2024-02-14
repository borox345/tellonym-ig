from PIL import Image, ImageFont, ImageDraw 
import textwrap

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                line, font=font, fill=text_color)
        y_text += line_height

def generate_tell_image(text: str = 'Unkown', file_name: str = 'unkown'):
    W, H = (500, 400)
    medium_font = ImageFont.truetype(r'assets/fonts/Roboto-Medium.ttf', 20)
    bold_font = ImageFont.truetype(r'assets/fonts/Roboto-Bold.ttf', 20)
    black_font = ImageFont.truetype(r'assets/fonts/Roboto-Black.ttf', 20)

    img  = Image.new( mode = "RGB", size = (W, H), color = (26, 34, 45) )

    tellonym_logo = Image.open('assets/img/tellonym-logo.jpg').resize((150, 25))
    #https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
    img.paste(tellonym_logo, (175, 25))

    # Text
    text_color = (200, 200, 200)
    draw_multiple_line_text(img, text, medium_font, text_color, 120)


    img.save(f'{file_name}.jpg')