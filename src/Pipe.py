"""
The pipe class - creates the pipes in the game
"""


import pygame
import random
import config

class Pipe:
    def __init__(self, x):
        self.x = x
        # Calculate a more balanced height for the pipes
        self.height = random.randint(config.PIPE_MIN_HEIGHT, config.PIPE_MAX_HEIGHT - config.PIPE_GAP_MAX)
        # Random vertical gap
        self.gap = random.randint(config.PIPE_GAP_MIN, config.PIPE_GAP_MAX)
        self.vel_x = -4
        self.passed = False

    @staticmethod
    def get_random_spacing():
        return random.randint(config.PIPE_SPACING_MIN, config.PIPE_SPACING_MAX)

    def move(self):
        self.x += self.vel_x

    def draw(self, screen):
        # Draw top pipe (flipped)
        screen.blit(pygame.transform.flip(config.PIPE_IMAGE, False, True), 
                   (self.x, self.height - config.PIPE_IMAGE.get_height()))
        # Draw bottom pipe (normal)
        screen.blit(config.PIPE_IMAGE, 
                   (self.x, self.height + self.gap))
