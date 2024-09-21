import pygame
import pytmx
from pygame.locals import QUIT  # Importation de l'événement QUIT
from config import *
from player import Player
from cows import BrownCow, PinkCow

class Game:
    def __init__(self):
        [idle_frames, up_frames, right_frames, left_frames, down_frames] = Player.load_sprites()
        [brown_cow_frames, right_brown_cow_frames, pink_cow_frames, right_pink_cow_frames] = BrownCow.load_sprites()

        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        # Charger la carte
        self.map = pytmx.load_pygame('maps/level1.tmx')

        # Initialiser le joueur et les vaches avec les frames
        self.player = Player(PLAYER_START_X, PLAYER_START_Y, idle_frames, up_frames, right_frames, left_frames, down_frames)
        self.brown_cow = BrownCow(BROWN_COW_START_X, BROWN_COW_START_Y, brown_cow_frames, right_brown_cow_frames)
        self.pink_cow = PinkCow(PINK_COW_START_X, PINK_COW_START_Y, pink_cow_frames, right_pink_cow_frames)

        # Définir la caméra et l'horloge
        self.camera = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:  # Utilisation de l'événement QUIT correctement importé
                    pygame.quit()
                    sys.exit()

            self.player.update(keys)
            self.update_camera()

            # Effacer l'écran
            self.window.fill((0, 0, 0))

            # Rendu des éléments
            self.render()

            # Mettre à jour l'affichage
            pygame.display.update()

            # Régler la cadence de rafraîchissement
            self.clock.tick(60)

    def update_camera(self):
        self.camera.center = self.player.rect.center
        self.camera.x = max(0, min(self.camera.x, self.map.width * self.map.tilewidth * ZOOM_FACTOR - self.camera.width))
        self.camera.y = max(0, min(self.camera.y, self.map.height * self.map.tileheight * ZOOM_FACTOR - self.camera.height))

    def render(self):
        self.render_map()
        self.player.render(self.window, self.camera)
        self.brown_cow.render(self.window, self.camera)
        self.pink_cow.render(self.window, self.camera)

    def render_map(self):
        for layer_name in sorted(LAYERS, key=LAYERS.get):
            layer = self.map.get_layer_by_name(layer_name)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map.get_tile_image_by_gid(gid)
                    if tile:
                        # Zoom sur les tuiles
                        zoomed_tile = pygame.transform.scale(tile, (int(self.map.tilewidth * ZOOM_FACTOR), int(self.map.tileheight * ZOOM_FACTOR)))
                        # Positionner la tuile avec le décalage de la caméra
                        tile_x = x * self.map.tilewidth * ZOOM_FACTOR - self.camera.x
                        tile_y = y * self.map.tileheight * ZOOM_FACTOR - self.camera.y
                        self.window.blit(zoomed_tile, (round(tile_x), round(tile_y)))
