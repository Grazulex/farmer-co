import pygame
import random
from settings import *
from pytmx.util_pygame import load_pygame
from support import *
from timer import Timer

class Cow(pygame.sprite.Sprite):
    def __init__(self, pos, group, color):
        super().__init__(group)

        self.color = color
        self.import_assets()
        ## status attributes randomize between right_idle and left_idle
        self.status = f'right_idle' if random.choice([True, False]) else f'left_idle'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.color][self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['main']

        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 10

        # autonomous movement attributes
        self.move_timer = Timer(10000)  # Change direction every second
        self.move_timer.start()

    def import_assets(self):
        brown_cow = pygame.image.load('../graphics/cow/Brown_cow_animations.png').convert_alpha()
        pink_cow = pygame.image.load('../graphics/cow/Pink_cow_animations.png').convert_alpha()
        light_cow = pygame.image.load('../graphics/cow/Light_cow_animations.png').convert_alpha()
        purple_cow = pygame.image.load('../graphics/cow/Purple_cow_animations.png').convert_alpha()
        green_cow = pygame.image.load('../graphics/cow/Green_cow_animations.png').convert_alpha()

        self.animations = {
            'brown': {
                'right_idle': [brown_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)) for i in range(3)],
                'right_walk': [brown_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)) for i in range(8)],
                'right_jump': [brown_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)) for i in range(7)],
                'right_pause': [brown_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)) for i in range(3)],
                'right_sleep': [brown_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)) for i in range(4)],
                'right_eat': [brown_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)) for i in range(7)],
                'right_grass': [brown_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)) for i in range(4)],
                'right_love': [brown_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)) for i in range(6)],
                'left_idle': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)), True, False) for i in range(3)],
                'left_walk': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)), True, False) for i in range(8)],
                'left_jump': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)), True, False) for i in range(7)],
                'left_pause': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)), True, False) for i in range(3)],
                'left_sleep': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)), True, False) for i in range(4)],
                'left_eat': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)), True, False) for i in range(7)],
                'left_grass': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)), True, False) for i in range(4)],
                'left_love': [pygame.transform.flip(brown_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)), True, False) for i in range(6)],

            },
            'pink': {
                'right_idle': [pink_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)) for i in range(3)],
                'right_walk': [pink_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)) for i in range(8)],
                'right_jump': [pink_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)) for i in range(7)],
                'right_pause': [pink_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)) for i in range(3)],
                'right_sleep': [pink_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)) for i in range(4)],
                'right_eat': [pink_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)) for i in range(7)],
                'right_grass': [pink_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)) for i in range(4)],
                'right_love': [pink_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)) for i in range(6)],
                'left_idle': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)), True, False) for i in range(3)],
                'left_walk': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)), True, False) for i in range(8)],
                'left_jump': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)), True, False) for i in range(7)],
                'left_pause': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)), True, False) for i in range(3)],
                'left_sleep': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)), True, False) for i in range(4)],
                'left_eat': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)), True, False) for i in range(7)],
                'left_grass': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)), True, False) for i in range(4)],
                'left_love': [pygame.transform.flip(pink_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)), True, False) for i in range(6)],
            },
            'light': {
                'right_idle': [light_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)) for i in range(3)],
                'right_walk': [light_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)) for i in range(8)],
                'right_jump': [light_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)) for i in range(7)],
                'right_pause': [light_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)) for i in range(3)],
                'right_sleep': [light_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)) for i in range(4)],
                'right_eat': [light_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)) for i in range(7)],
                'right_grass': [light_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)) for i in range(4)],
                'right_love': [light_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)) for i in range(6)],
                'left_idle': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)), True, False) for i in range(3)],
                'left_walk': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)), True, False) for i in range(8)],
                'left_jump': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)), True, False) for i in range(7)],
                'left_pause': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)), True, False) for i in range(3)],
                'left_sleep': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)), True, False) for i in range(4)],
                'left_eat': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)), True, False) for i in range(7)],
                'left_grass': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)), True, False) for i in range(4)],
                'left_love': [pygame.transform.flip(light_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)), True, False) for i in range(6)],
            },
            'purple': {
                'right_idle': [purple_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)) for i in range(3)],
                'right_walk': [purple_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)) for i in range(8)],
                'right_jump': [purple_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)) for i in range(7)],
                'right_pause': [purple_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)) for i in range(3)],
                'right_sleep': [purple_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)) for i in range(4)],
                'right_eat': [purple_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)) for i in range(7)],
                'right_grass': [purple_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)) for i in range(4)],
                'right_love': [purple_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)) for i in range(6)],
                'left_idle': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)), True, False) for i in range(3)],
                'left_walk': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)), True, False) for i in range(8)],
                'left_jump': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)), True, False) for i in range(7)],
                'left_pause': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)), True, False) for i in range(3)],
                'left_sleep': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)), True, False) for i in range(4)],
                'left_eat': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)), True, False) for i in range(7)],
                'left_grass': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)), True, False) for i in range(4)],
                'left_love': [pygame.transform.flip(purple_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)), True, False) for i in range(6)],
            },
            'green': {
                'right_idle': [green_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)) for i in range(3)],
                'right_walk': [green_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)) for i in range(8)],
                'right_jump': [green_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)) for i in range(7)],
                'right_pause': [green_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)) for i in range(3)],
                'right_sleep': [green_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)) for i in range(4)],
                'right_eat': [green_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)) for i in range(7)],
                'right_grass': [green_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)) for i in range(4)],
                'right_love': [green_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)) for i in range(6)],
                'left_idle': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*0, 32, 32)), True, False) for i in range(3)],
                'left_walk': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*1, 32, 32)), True, False) for i in range(8)],
                'left_jump': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*2, 32, 32)), True, False) for i in range(7)],
                'left_pause': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*3, 32, 32)), True, False) for i in range(3)],
                'left_sleep': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*4, 32, 32)), True, False) for i in range(4)],
                'left_eat': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*5, 32, 32)), True, False) for i in range(7)],
                'left_grass': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*6, 32, 32)), True, False) for i in range(4)],
                'left_love': [pygame.transform.flip(green_cow.subsurface(pygame.Rect(i * 32, 32*7, 32, 32)), True, False) for i in range(6)],
            }
        }

    def animate(self, dt):
        self.frame_index += 0.02  # Reduce animation speed
        if self.frame_index >= len(self.animations[self.color][self.status]):
            self.frame_index = 0

        self.image = self.animations[self.color][self.status][int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 4, self.image.get_height() * 4))

    def move(self, dt):
        if self.move_timer.is_finished():
            if self.direction.magnitude() > 0:
                self.direction = self.direction.normalize()

            self.direction.x = random.choice([-1, 0, 1])
            self.direction.y = random.choice([-1, 0, 1])
            self.move_timer.start()

            # Randomly choose an idle animation
            if self.direction.x == 0 and self.direction.y == 0:
                idle_animations = ['pause', 'sleep', 'eat', 'grass', 'jump', 'idle']
                chosen_idle = random.choice(idle_animations)
                self.status = f'right_{chosen_idle}' if self.status.startswith('right') else f'left_{chosen_idle}'
            else:
                # Update animation status based on direction
                if self.direction.x > 0:
                    self.status = 'right_walk'
                elif self.direction.x < 0:
                    self.status = 'left_walk'   
                elif self.direction.x == 0:
                    if self.direction.y != 0:
                        self.status = 'right_walk' if self.status.startswith('right') else 'left_walk'
                    else:
                        self.status = 'right_idle' if self.status.startswith('right') else 'left_idle'

            # check if cow is out of bounds
            if self.rect.left < 0:
                self.direction.x = 1
            if self.rect.right > SCREEN_WIDTH:
                self.direction.x = -1
            if self.rect.top < 0:
                self.direction.y = 1
            if self.rect.bottom > SCREEN_HEIGHT:
                self.direction.y = -1

        # Update position only if the cow is supposed to move
        if self.direction.x != 0 or self.direction.y != 0:
            self.pos += self.direction * self.speed * dt
            self.rect.center = self.pos

    def update(self, dt):
        self.move(dt)
        self.animate(dt)


class Timer:

    def __init__(self, duration):

        self.duration = duration

        self.start_time = None



    def start(self):

        self.start_time = pygame.time.get_ticks()



    def is_finished(self):

        if self.start_time is None:

            return False

        return pygame.time.get_ticks() - self.start_time >= self.duration
