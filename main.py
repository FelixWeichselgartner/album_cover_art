from os import walk
from mytoken import genius_token
import lyricsgenius as lg
import re
from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageEnhance
import requests


def rescale_img(image, base):
    wpercent = (base / float(image.size[0]))
    hsize = int((float(image.size[1]) * float(wpercent)))
    return image.resize((base, hsize), Image.ANTIALIAS)


def darken_img(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    factor = 0.5
    return enhancer.enhance(factor)


def blur_img(image):
    im = image
    for i in range(3):
        im = im.filter(ImageFilter.MinFilter(7))
    for i in range(3):
        im = im.filter(ImageFilter.BLUR)
    return im


def brighten_pixel(px):
    r, g, b = px
    factor2 = 1.05
    r2 = int(factor2 * r)
    g2 = int(factor2 * g)
    b2 = int(factor2 * b)
    if r2 > 255:
        r2 = 255
    if g2 > 255:
        g2 = 255
    if b2 > 255:
        b2 = 255
    return (r2, g2, b2)


all_files = next(walk('./input/'), (None, None, []))[2]
filenames = list(filter(lambda x: '.jpg' in x or '.png' in x, all_files))
filenames.sort(key=lambda x: int(x[:2]))

genius = lg.Genius(genius_token)

songs = list()
with open('input/songs.txt') as song_list:
    songs = song_list.readlines()
for i in range(len(songs)):
    songs[i] = songs[i].replace('\n', '')
print(songs)
texts = list()

for song in songs:
    fail = True
    while fail:
        try:
            gsong = genius.search_song(song)
            fail = False
        except requests.exceptions.Timeout:
            fail = True
    raw_text = gsong.lyrics
    raw_text2 = re.sub("[\(\[].*?[\)\]]", "", raw_text[raw_text.find('\n') + 1:]).replace('\n', '').replace('Embed', ' ')
    while str.isdigit(raw_text2[-1]) or raw_text2[-1] == ' ':
        raw_text2 = raw_text2[:-2]
    text = raw_text2
    for i in range(10):
        text = text.replace('  ', '')
    texts.append(text)

char_width = 7
char_height = 7

file_counter = 0
for img_file in filenames:
    original_in_size = Image.open(f'./input/{img_file}')
    original = rescale_img(original_in_size, 300)
    #original.save(f'./output/resize_{img_file}.png'.replace('.jpg', ''))

    dim = original.size
    width, height = dim
    dim2 = (dim[0] * char_width, dim[1] * char_height)

    black_background = False
    image = None

    if not black_background:
        im = rescale_img(original_in_size, 300 * char_width)
        im = blur_img(im)
        image = darken_img(im, 0.65)
    else:
        brightness = 25
        image = Image.new('RGB', dim2, (brightness, brightness, brightness))

    draw = ImageDraw.Draw(image)
    font = font = ImageFont.truetype("/usr/share/fonts/truetype/gnu-free/FreeMono.ttf", 12, encoding="unic")
    current_text = texts[file_counter]
    text_counter = 0
    
    for h in range(height):
        for w in range(width):
            if text_counter >= len(current_text):
                text_counter = 0
            draw.text((char_width * w, char_height * h), 
                       current_text[text_counter], 
                       brighten_pixel(original.getpixel((w, h))), 
                       font=font)
            text_counter += 1
    
    output_name = f'./output/{img_file}'.replace('.jpg', '').replace('.png', '') + '.png'
    image.save(output_name)
    print('wrote image to:')
    print(output_name)

    file_counter += 1
