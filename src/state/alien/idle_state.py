import pygame as pg

class IdleState:
    def __init__(self, player):
        print("Alien: IdleState")
        self.player = player

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_a] or keys[pg.K_s] or keys[pg.K_d]:
            # Local relative import breaks the circular dependency loop
            from .move_state import MoveState
            self.player.state = MoveState(self.player)