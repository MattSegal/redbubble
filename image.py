"""
makes an image

we can draw
    - arcs
    - bitmaps
    - chords
    - ellipses
    - lines
    - pie slices
    - points
    - polygon
    - rectangle
"""
from PIL import Image, ImageDraw

import consts
from sierpinski import sierpinski
from corn_chips import corn_chips
from fuzzer import fuzzer

def main():
    img = Image.new('RGBA', (consts.WIDTH, consts.HEIGHT), consts.WHITE)
    draw = ImageDraw.Draw(img)
    depth = 0
    corn_chips(draw)
    # fuzzer(draw)
    # img = img.rotate(180)
    img.save('test.png', 'PNG')

if __name__ == '__main__':
    main()
