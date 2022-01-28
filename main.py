from os import walk
from mytoken import genius_token
import lyricsgenius as lg
import re
from PIL import Image, ImageFont, ImageDraw
import requests


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
    original = Image.open(f'./input/{img_file}')

    basewidth = 300
    wpercent = (basewidth/float(original.size[0]))
    hsize = int((float(original.size[1])*float(wpercent)))
    original = original.resize((basewidth,hsize), Image.ANTIALIAS)
    original.save(f'./output/resize_{img_file}.png'.replace('.jpg', ''))

    dim = original.size
    width, height = dim
    dim2 = (dim[0] * char_width, dim[1] * char_height)
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
            draw.text((char_width * w, char_height * h), current_text[text_counter], original.getpixel((w, h)), font=font)
            text_counter += 1
    
    output_name = f'./output/{img_file}'.replace('.jpg', '').replace('.png', '') + '.png'
    image.save(output_name)
    print('wrote image to:')
    print(output_name)

    file_counter += 1
