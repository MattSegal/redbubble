"""
Randomly fuzz the edges of the image
"""
from random import random

import consts
from colors import ColorWheel

NUM_COLS = 140
SIZE = consts.WIDTH / NUM_COLS

distribution = (
    [0.9] * 2 +
    [0.8] * 3 +
    [0.7] * 3 +
    [0.6] * 3 +
    [0.5] * 2 +
    [0.4] * 2 +
    [0.3] * 2
)

def fuzzer(draw):
    height = 0
    while height * SIZE < consts.HEIGHT:
        # Draw the current row
        count = 0
        for probability in distribution:
            if random() < probability:
                blank_square(draw, height, count)

            if random() < probability:
                blank_square(draw, height, NUM_COLS - 1 - count)

            count += 1

        # Increment height
        height += 1

    count = 0
    for probability in distribution:
        for i in range(NUM_COLS):
            if random() < probability:
                blank_square(draw, count, i)

            if random() < probability:
                blank_square(draw, height - count, i)

        count += 1


def blank_square(draw, row, col):
    x0 = SIZE * col
    y0 = SIZE * row
    x1 = x0 + SIZE
    y1 = y0 + SIZE
    draw.rectangle((x0, y0, x1, y1), fill=(0, 0, 0, 0))
