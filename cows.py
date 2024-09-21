import pygame
import random
from config import *

class BrownCow:
    def __init__(self, x, y, brown_cow_frames, right_brown_cow_frames):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.current_frame = 0
        self.frame_delay = 5
        self.frame_count = 0
        self.brown_cow_frames = brown_cow_frames
        self.right_brown_cow_frames = right_brown_cow_frames
        self.direction = 'left'  # Initial direction
        self.move_timer = 0
        self.move_duration = random.randint(90, 240)  # Duration to move in one direction

    def animate(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.brown_cow_frames)
            self.frame_count = 0

    def move_randomly(self):
        speed = BROWN_COW_SPEED  # Increase speed
        if self.move_timer <= 0:
            self.dx = random.choice([-speed, speed])
            self.dy = random.choice([-speed, speed])
            self.move_duration = random.randint(30, 60)  # New duration to move in one direction
            self.move_timer = self.move_duration
            self.direction = 'right' if self.dx > 0 else 'left'
        else:
            self.move_timer -= 1

        self.rect.x += self.dx
        self.rect.y += self.dy

    def render(self, window, camera):
        self.move_randomly()
        self.animate()
        cow_pos = self.rect.move(-camera.x, -camera.y)
        if self.direction == 'right':
            zoomed_frame = pygame.transform.scale(self.right_brown_cow_frames[self.current_frame], (int(32 * ZOOM_FACTOR), int(32 * ZOOM_FACTOR)))
        else:
            zoomed_frame = pygame.transform.flip(
                pygame.transform.scale(self.right_brown_cow_frames[self.current_frame], (int(32 * ZOOM_FACTOR), int(32 * ZOOM_FACTOR))),
                True, False
            )
        window.blit(zoomed_frame, cow_pos.topleft)

    def load_sprites():
        brown_cow_sprite_sheet = pygame.image.load(BROWN_COW_SPRITE_SHEET).convert_alpha()
        pink_cow_sprite_sheet = pygame.image.load(PINK_COW_SPRITE_SHEET).convert_alpha()
        brown_cow_frames = [brown_cow_sprite_sheet.subsurface(pygame.Rect(i * BROWN_COW_WIDTH, BROWN_COW_HEIGHT*0, BROWN_COW_WIDTH, BROWN_COW_HEIGHT)) for i in range(3)]
        right_brown_cow_frames = [brown_cow_sprite_sheet.subsurface(pygame.Rect(i * BROWN_COW_WIDTH, BROWN_COW_HEIGHT*1, BROWN_COW_WIDTH, BROWN_COW_HEIGHT)) for i in range(3)]

        pink_cow_frames = [pink_cow_sprite_sheet.subsurface(pygame.Rect(i * PINK_COW_WIDTH, PINK_COW_HEIGHT*0, PINK_COW_WIDTH,PINK_COW_HEIGHT)) for i in range(3)]
        right_pink_cow_frames = [pink_cow_sprite_sheet.subsurface(pygame.Rect(i * PINK_COW_WIDTH, PINK_COW_HEIGHT*1, PINK_COW_WIDTH,PINK_COW_HEIGHT)) for i in range(3)]

        return brown_cow_frames, right_brown_cow_frames, pink_cow_frames, right_pink_cow_frames

class PinkCow(BrownCow):
    def render(self, window, camera):
        self.move_randomly()
        self.animate()
        cow_pos = self.rect.move(-camera.x, -camera.y)
        if self.direction == 'right':
            zoomed_frame = pygame.transform.scale(self.right_brown_cow_frames[self.current_frame], (int(32 * ZOOM_FACTOR), int(32 * ZOOM_FACTOR)))
        else:
            zoomed_frame = pygame.transform.flip(
                pygame.transform.scale(self.brown_cow_frames[self.current_frame], (int(32 * ZOOM_FACTOR), int(32 * ZOOM_FACTOR))),
                True, False
            )
        window.blit(zoomed_frame, cow_pos.topleft)
