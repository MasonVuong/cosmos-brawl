import pygame as pg; pg.init()

class Projectile(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation = self.slice_sheet("assets/sprites/alien/alien_projectile.png", 2, 2, 3)
        self.image = self.animation[0]
        self.frame_index = 0.0
        self.frame_speed = 0.1
        self.rect = self.image.get_rect(center=(x, y))

    def slice_sheet(self, path, rows, cols, frames):
        sheet = pg.image.load(path).convert_alpha()
        w, h = sheet.get_size()
        fw, fh = w // cols, h // rows
        i = 0
        animation = []
        for c in range(cols):
            for r in range(rows):
                animation.append(sheet.subsurface(pg.Rect(c * fw, r * fh, fw, fh)))
                i += 1
                if i == frames:
                    return animation

    def animate(self):
        self.image = self.animation[int(self.frame_index)]

        self.frame_index += self.frame_speed
        if self.frame_index > 2:
            self.frame_index = 2
        self.rect.x += 2