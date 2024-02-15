#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

from .rustPaletteData import rust_palette


def hex_to_rgb(hex):
    """ Convert hexadecimal color to rgb """
    h = hex.lstrip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb


def rgb_to_hex(rgb):
    """ Convert rgb to hexadecimal color """
    return ("#%02x%02x%02x" % rgb).upper()


def closest_color(rgb):
    """ Find the closest color from the rust_palette file """
    r, g, b = rgb
    color_diffs = []
    for color in rust_palette:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
