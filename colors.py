"""
The ColorWheel allows us to work with colors using
Hue/Saturation/Value (HSV)  and then convert it to
Red/Green/Blue (RGB) for rendering
HSV: 0 ≤ H < 2PI, 0 ≤ S ≤ 1 and 0 ≤ V ≤ 1:
RGB: 0 ≤ R, G, B ≤ 255
"""
import math


class ColorWheel:
    def __init__(self, hue, sat, val):
        self.hue = hue
        self.sat = sat
        self.val = val

    def rotate(self, angle):
        """Rotate hue in radians"""
        self.hue = (2 * math.pi + self.hue + angle) % (2 * math.pi)

    def as_rgb(self):
        """Converts HSV to RGB"""
        # 1 - calculate inscrutable intermediate values
        h = self.hue / (math.pi / 3)
        c = self.val * self.sat
        x = c * (1 - math.fabs(h % 2 - 1))
        o = self.val - c

        # 2 - smash them together
        idx = math.floor(h)
        vals = get_hue_prime(x, c, idx)
        vals = [color + o for color in vals]
        return tuple([round(255 * color) for color in vals])


def get_hue_prime(x, c, idx):
    """No idea what this does, and I don't care"""
    lookup = [
      [c, x, 0],
      [x, c, 0],
      [0, c, x],
      [0, x, c],
      [x, 0, c],
      [c, 0, x],
      [0, 0, 0],
    ]
    return lookup[idx]
