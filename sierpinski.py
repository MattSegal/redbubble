"""
draws a sierpinski triangle
"""
import consts

MAX_DEPTH = 8

def sierpinski(draw):
    depth = 0
    draw_triangles(draw, depth, consts.START)

def draw_triangles(draw, depth, start):
    depth += 1
    color = consts.WHITE if depth % 2 > 0 else consts.BLACK
    length = consts.SIZE / 2**(depth - 1)
    left =  start
    right = (
        start[0] + length,
        start[1]
    )
    top = (
        start[0] + length / 2,
        start[1] + 1.5 * triangle_height(length)
    )
    draw.polygon((left, top, right), fill=color)
    if depth < MAX_DEPTH:
        # Left
        left_start = start
        draw_triangles(draw, depth, left_start)
        # Right
        right_start = (top[0], start[1])
        draw_triangles(draw, depth, right_start)
        # Top
        top_start = (
            start[0] + length / 2 / 2,
            start[1] + 1.5 * triangle_height(length / 2)
        )
        draw_triangles(draw, depth, top_start)


def triangle_height(length):
    return 3**0.5 * length / 2
