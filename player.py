import pygame
from config import *
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN

class Player:
    def __init__(self, x, y, idle_frames, up_frames, right_frames, left_frames, down_frames):
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.current_frame = 0
        self.frame_delay = 5
        self.frame_count = 0
        self.idle_frames = idle_frames
        self.up_frames = up_frames
        self.right_frames = right_frames
        self.left_frames = left_frames
        self.down_frames = down_frames
        self.current_frames = idle_frames

    def update(self, keys):
        new_player_pos = self.rect.copy()
        if keys[K_LEFT]:
            new_player_pos.x -= PLAYER_SPEED
            self.current_frames = self.left_frames
        elif keys[K_RIGHT]:
            new_player_pos.x += PLAYER_SPEED
            self.current_frames = self.right_frames
        elif keys[K_UP]:
            new_player_pos.y -= PLAYER_SPEED
            self.current_frames = self.up_frames
        elif keys[K_DOWN]:
            new_player_pos.y += PLAYER_SPEED
            self.current_frames = self.down_frames
        else:
            self.current_frames = self.idle_frames

        self.rect = new_player_pos
        self.animate()

    def animate(self):
        self.frame_count += 1
        if self.frame_count >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.current_frames)
            self.frame_count = 0

    def render(self, window, camera):
        player_pos = self.rect.move(-camera.x, -camera.y)
        zoomed_frame = pygame.transform.scale(self.current_frames[self.current_frame], (int(PLAYER_WIDTH * ZOOM_FACTOR), int(PLAYER_HEIGHT * ZOOM_FACTOR)))
        window.blit(zoomed_frame, player_pos.topleft)

    def load_sprites():
        sprite_sheet = pygame.image.load(PLAYER_SPRITE_SHEET).convert_alpha()
        idle_frames = [sprite_sheet.subsurface(pygame.Rect(i * PLAYER_WIDTH, PLAYER_HEIGHT*0, PLAYER_WIDTH, PLAYER_HEIGHT)) for i in range(8)]
        up_frames = [sprite_sheet.subsurface(pygame.Rect(i * PLAYER_WIDTH, PLAYER_HEIGHT*5, PLAYER_WIDTH, PLAYER_HEIGHT)) for i in range(8)]
        right_frames = [sprite_sheet.subsurface(pygame.Rect(i * PLAYER_WIDTH, PLAYER_HEIGHT*6, PLAYER_WIDTH, PLAYER_HEIGHT)) for i in range(8)]
        left_frames = [sprite_sheet.subsurface(pygame.Rect(i * PLAYER_WIDTH, PLAYER_HEIGHT*7, PLAYER_WIDTH, PLAYER_HEIGHT)) for i in range(8)]
        down_frames = [sprite_sheet.subsurface(pygame.Rect(i * PLAYER_WIDTH, PLAYER_HEIGHT*4, PLAYER_WIDTH, PLAYER_HEIGHT)) for i in range(8)]

        return idle_frames, up_frames, right_frames, left_frames, down_frames