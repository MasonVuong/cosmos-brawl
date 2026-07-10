import pygame as pg

class MoveState:
    def __init__(self, player):
        print("Alien: MoveState")
        self.player = player

    def update(self):
        keys = pg.key.get_pressed()
        moved = False
        
        if keys[pg.K_w]: self.player.rect.y -= 1; moved = True
        if keys[pg.K_a]: self.player.rect.x -= 1; moved = True
        if keys[pg.K_s]: self.player.rect.y += 1; moved = True
        if keys[pg.K_d]: self.player.rect.x += 1; moved = True
            
        if not moved:
            # Local relative import breaks the circular dependency loop
            from .idle_state import IdleState
            self.player.state = IdleState(self.player)