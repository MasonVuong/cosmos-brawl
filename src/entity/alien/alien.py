import pygame as pg
from src.state.alien import IdleState
from .projectile import Projectile

class Alien(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animations = {
            "idle": self.slice_sheet(
                "assets/sprites/alien/alien_idle.png", rows=2, cols=2
            ),
            "move": self.slice_sheet(
                "assets/sprites/alien/alien_idle.png", rows=2, cols=2
            ),
            "attack": self.slice_sheet(
                "assets/sprites/alien/alien_shoot.png", rows=2, cols=3
            ),
        }

        self.current_animation = "idle"
        self.frame_index = 0.0
        self.animation_finished = False

        self.image = self.animations[self.current_animation][0]
        self.rect = self.image.get_rect(center=(80, 40))

        self.state = IdleState(self)
        self.projectile = None
        self.jump_power = 0

    def slice_sheet(self, path, rows, cols, frames=-1):
        sheet = pg.image.load(path).convert_alpha()
        w, h = sheet.get_size()
        fw, fh = w // cols, h // rows

        i = 0
        animation = []
        for c in range(cols):
            for r in range(rows):
                animation.append(sheet.subsurface(pg.Rect(c * fw, r * fh, fw, fh)))
                if i != -1:
                    i += 1
                if i == frames:
                    return animation
        return animation

    def animate(self):
        if self.projectile != None:
            self.projectile.animate()

        frames = self.animations[self.current_animation]

        self.image = frames[int(self.frame_index)]

        self.frame_index += self.frame_speed

        if self.frame_index >= len(frames):
            self.frame_index = 0.0

        return self.frame_index


    def update(self):
        self.state.update(self.animate())
        self.rect.y += self.jump_power
        self.jump_power += .2
        if self.rect.bottom > 85:
            self.rect.bottom = 85

    def handle_input(self, e):
        self.state.handle_input(e)