import cairo
import math

W, H = SIZE = 1920, 1080

class Arc:
    def __init__(self, r, limits=(0, math.pi * 2), tm=1.0, pos=(0, 0),
        line_width=1):
        self.r = r
        self.tm = tm
        self.limits = limits
        self.pos = pos
        self.line_width = line_width

    def draw_in(self, ctx):
        x, y = self.pos
        linewidth = ctx.get_line_width()
        ctx.set_source_rgb(255, 255, 255)
        ctx.set_line_width(self.line_width / W)
        ctx.arc(x, y, self.r, *self.limits)
        ctx.set_line_width(linewidth)

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, W, W)
ctx = cairo.Context(surface)
ctx.scale(W, W)

arc = Arc(40 / W, limits=(0, math.pi), tm=0.5, pos=(400 / W, 400 / W))
arc.draw_in(ctx)

surface.write_to_png('aja.png')

