from src.entity.alien.projectile import Projectile

class AttackState:
    def __init__(self, player):
        self.player = player
        self.player.frame_index = 0
        self.player.current_animation = "attack"
        self.player.frame_speed = .15

    def handle_input(self, e):
        pass

    def update(self, frame):
        if frame == 0:
            from .idle_state import IdleState

            self.player.state = IdleState(self.player)
        if int(frame) == 3:
            self.player.projectile = Projectile(self.player.rect.x + 28, self.player.rect.y + 18)
            