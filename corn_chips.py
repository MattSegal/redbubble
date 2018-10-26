"""
corn chips!
"""
import consts
from colors import ColorWheel

NUM_COLS = 140
SIZE = consts.WIDTH / NUM_COLS

# Rules used to generate cellular automata
RULES = [
    [0, 1, 1, 1, 1, 0, 0, 0],    # Rule 30
    [0, 1, 1, 1, 1, 1, 1, 0],    # Rule 126
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],   # Cool space pyramid thing
]
RULE = RULES[-1]

def corn_chips(draw):
    color_wheel = ColorWheel(3, 0.8, 0.8)
    height = 0
    row = [0 for _ in range(NUM_COLS)]
    row[10] = row[39] = 1

    while height * SIZE < consts.HEIGHT:
        color_wheel.rotate(0.015)
        # Draw the current row
        for i in range(NUM_COLS):
            if row[i] == 1:
                x0 = SIZE * i
                y0 = SIZE * height
                x1 = x0 + SIZE
                y1 = y0 + SIZE
                draw.rectangle((x0, y0, x1, y1), fill=color_wheel.as_rgb())

        # Calculate the next row from the current row
        # Ignore the left and right edges
        new_row = [0]
        for i in range(1, NUM_COLS -1):
            left = row[i - 1]
            middle = row[i]
            right = row[i + 1]
            index = 4 * left + 2 * middle + 1 * right
            new_row.append(RULE[index])

        new_row.append(0)
        row = new_row

        # Increment height
        height += 1
