import pygame as pg; pg.init()
import sys

# Clean absolute import thanks to your __init__.py files
from src.entity.alien.alien import Alien 

VIRTUAL_WIDTH = 160
VIRTUAL_HEIGHT = 90

info = pg.display.Info()
MONITOR_WIDTH = info.current_w
MONITOR_HEIGHT = info.current_h

SCALE = min(MONITOR_WIDTH / VIRTUAL_WIDTH, MONITOR_HEIGHT / VIRTUAL_HEIGHT)
SCALE_WIDTH = int(VIRTUAL_WIDTH * SCALE)
SCALE_HEIGHT = int(VIRTUAL_HEIGHT * SCALE)

DESTINATION_X = (MONITOR_WIDTH - SCALE_WIDTH) // 2
DESTINATION_Y = (MONITOR_HEIGHT - SCALE_HEIGHT) // 2

window = pg.display.set_mode((MONITOR_WIDTH, MONITOR_HEIGHT), pg.RESIZABLE)
canvas = pg.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
alien = Alien()
all_sprites.add(alien)

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

    # This ticks the alien's update() loop, which runs the current state's logic
    all_sprites.update()
    
    canvas.fill((255, 255, 255))
    all_sprites.draw(canvas)

    scaled_canvas = pg.transform.scale(canvas, (SCALE_WIDTH, SCALE_HEIGHT))
    window.blit(scaled_canvas, (DESTINATION_X, DESTINATION_Y))
    pg.display.flip()

    clock.tick(60)

pg.quit()
sys.exit()