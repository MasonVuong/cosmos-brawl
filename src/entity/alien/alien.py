import pygame as pg
from src.state.alien import IdleState

class Alien(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # 1. Load the entire 2x2 sprite sheet
        # Make sure this path accurately points to where you saved 'alien_idle.png'
        self.spritesheet = pg.image.load("assets/sprites/alien/alien_idle.png").convert_alpha()
        
        # 2. Slice the grid into a list of 4 individual frames
        self.frames = self.slice_grid_frames(rows=2, cols=2)
        
        # 3. Set up animation tracking variables
        self.frame_index = 0.0
        self.animation_speed = 0.1  # Increase to speed up, decrease to slow down
        
        # Establish the initial image and collision rect
        self.image = self.frames[int(self.frame_index)]
        self.rect = self.image.get_rect(center=(80, 40))
        
        self.state = IdleState(self)

    def slice_grid_frames(self, rows, cols):
        """Divides a grid sprite sheet evenly into a list of single frame surfaces."""
        sheet_w, sheet_h = self.spritesheet.get_size()
        frame_w = sheet_w // cols
        frame_h = sheet_h // rows
        
        frames = []
        for row in range(rows):
            for col in range(cols):
                x = col * frame_w
                y = row * frame_h
                # subsurface() cuts out a precise rectangular portion of the sheet
                frame_surface = self.spritesheet.subsurface(pg.Rect(x, y, frame_w, frame_h))
                frames.append(frame_surface)
        return frames

    def animate(self):
        """Advances the frame index over time and updates the active image."""
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0.0  # Loop back to the first frame
            
        # Convert float index to integer to grab the current surface frame
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        # 1. Run the animation timer
        self.animate()
        
        # 2. Check inputs and movement via your State Pattern
        self.state.update()