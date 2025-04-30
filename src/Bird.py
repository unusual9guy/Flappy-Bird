"""
The Bird class
1. Detects collision
2. Handles the movement of the bird
3. Handles the audio files 
"""


import pygame
import config

class Bird:
    def __init__(self, bird_type=0):
        self.x = 50
        self.y = config.SCREEN_HEIGHT // 2
        self.vel_y = 0
        self.gravity = 0.8
        self.bird_type = bird_type
        self.animation_frames = config.BIRD_TYPES[bird_type]['sprites']
        self.animation_index = 0
        self.animation_speed = 5
        self.animation_counter = 0
        self.current_image = self.animation_frames[self.animation_index]
        # Adjust the size of the collision box to your liking 
        self.rect = pygame.Rect(self.x, self.y, config.BIRD_WIDTH - 4, config.BIRD_HEIGHT - 4)  # Less reduction for tighter collision
        self.alive = True

    def move(self):
        if not self.alive:
            return

        self.vel_y += self.gravity
        self.y += self.vel_y
    
        self.rect.x = self.x + 2  # Slight offset to center the collision box
        self.rect.y = self.y + 2  # Slight offset to center the collision box
        
        # Wing animation
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.animation_counter = 0
            self.animation_index = (self.animation_index + 1) % len(self.animation_frames)
            self.current_image = self.animation_frames[self.animation_index]

    def jump(self):
        self.vel_y = -8
        if config.WING_SOUND:
            config.WING_SOUND.play()

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))

    def check_collision(self, pipes):
        # Ground collision
        if self.rect.bottom >= config.SCREEN_HEIGHT - config.BASE_HEIGHT:
            self.alive = False
            if config.HIT_SOUND:
                config.HIT_SOUND.play()
            if config.DIE_SOUND:
                config.DIE_SOUND.play()
            return True

        # Pipe collision 
        for pipe in pipes:
            # Collision boxes for pipes
            top_pipe = pygame.Rect(
                pipe.x - 2,
                0, 
                config.PIPE_IMAGE.get_width() + 4,
                pipe.height
            )
            
            bottom_pipe = pygame.Rect(
                pipe.x - 2,
                pipe.height + pipe.gap,
                config.PIPE_IMAGE.get_width() + 4,
                config.SCREEN_HEIGHT - (pipe.height + pipe.gap)
            )
            
            if self.rect.colliderect(top_pipe) or self.rect.colliderect(bottom_pipe):
                self.alive = False
                if config.HIT_SOUND:
                    config.HIT_SOUND.play()
                if config.DIE_SOUND:
                    config.DIE_SOUND.play()
                return True
        
        return False

    def change_bird_type(self, bird_type):
        self.bird_type = bird_type
        self.animation_frames = config.BIRD_TYPES[bird_type]['sprites']
        self.current_image = self.animation_frames[self.animation_index]
