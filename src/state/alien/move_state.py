import pygame as pg

class MoveState:
    def __init__(self, player):
        self.player = player
        self.player.current_animation = "move"
        self.player.frame_speed = .1

    def handle_input(self, e):
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_j:
                from .attack_state import AttackState
                self.player.state = AttackState(self.player)
            if e.key == pg.K_SPACE:
                self.player.jump_power = -4

    def update(self, frame):
        keys = pg.key.get_pressed()

        moved = False
        """
        if keys[pg.K_w]:
            self.player.rect.y -= 1
            moved = True

        if keys[pg.K_s]:
            self.player.rect.y += 1
            moved = True
        """
        if keys[pg.K_a]:
            self.player.rect.x -= 1
            moved = True

        if keys[pg.K_d]:
            self.player.rect.x += 1
            moved = True

        if not moved:
            from .idle_state import IdleState

            self.player.state = IdleState(self.player)