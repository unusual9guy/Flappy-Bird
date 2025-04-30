"""
The Score class - 
1. Loads all the sprites 
2. Creates the Menu
3. Keeps track of the score
"""


import pygame
import sys
import config
import math
import Bird

class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0

    def draw(self, screen):
        # Convert score to string to handle each digit
        score_str = str(self.score)
        total_width = 0
        
        # Calculate total width of all numbers to center them
        for digit in score_str:
            total_width += config.NUMBERS[int(digit)].get_width()
        
        # Start x position (centered)
        x = (config.SCREEN_WIDTH - total_width) // 2
        y = 50  # Distance from top of screen

        # Draw each digit using regular (large) numbers for in-game score
        for digit in score_str:
            num_image = config.NUMBERS[int(digit)]
            screen.blit(num_image, (x, y))
            x += num_image.get_width()

    def update(self, bird, pipes):
        for pipe in pipes:
            if pipe.x + config.PIPE_IMAGE.get_width() < bird.x and not pipe.passed:
                self.score += 1
                pipe.passed = True
                if config.POINT_SOUND:
                    config.POINT_SOUND.play()

def get_medal(score):
    if score >= 40:
        return config.PLATINUM_MEDAL
    elif score >= 30:
        return config.GOLD_MEDAL
    elif score >= 20:
        return config.SILVER_MEDAL
    elif score >= 10:
        return config.BRONZE_MEDAL
    return None

def draw_small_number(screen, number_str, x, y, right_align=False):
    # Calculate total width if right-aligned
    if right_align:
        total_width = sum(config.SMALL_NUMBERS[int(digit)].get_width() for digit in number_str)
        x -= total_width
    
    # Draw each digit
    for digit in number_str:
        num_image = config.SMALL_NUMBERS[int(digit)]
        screen.blit(num_image, (x, y))
        x += num_image.get_width()

def draw_score_panel(screen, score, high_score):
    # Position the score panel
    panel_x = (config.SCREEN_WIDTH - config.SCORE_PANEL.get_width()) // 2
    panel_y = config.SCREEN_HEIGHT // 2 - 50
    
    # Draw the panel
    screen.blit(config.SCORE_PANEL, (panel_x, panel_y))
    
    # Draw medal if earned
    medal = get_medal(score)
    if medal:
        medal_x = panel_x + 28
        medal_y = panel_y + 44
        screen.blit(medal, (medal_x, medal_y))
    
    # Draw current score using small numbers (more right-aligned)
    score_str = str(score)
    score_x = panel_x + config.SCORE_PANEL.get_width() - 25  # Adjusted x position
    score_y = panel_y + 37
    draw_small_number(screen, score_str, score_x, score_y, right_align=True)
    
    # Draw best score using small numbers (more right-aligned)
    best_str = str(high_score)
    best_x = panel_x + config.SCORE_PANEL.get_width() - 25  # Adjusted x position
    best_y = panel_y + 77
    draw_small_number(screen, best_str, best_x, best_y, right_align=True)

def show_menu_screen():
    current_bird_type = 0
    bird = Bird.Bird(current_bird_type)
    base_x = 0
    
    # Add these variables for bird hover animation
    hover_time = 0
    hover_speed = 0.05
    original_y = bird.y
    hover_range = 20  # How many pixels up and down the bird will move
    
    # Add font for bird type display
    font = pygame.font.Font(None, 36)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if config.SWOOSH_SOUND:
                        config.SWOOSH_SOUND.play()
                    return current_bird_type
                elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    if config.SWOOSH_SOUND:
                        config.SWOOSH_SOUND.play()
                    current_bird_type = (current_bird_type - 1 if event.key == pygame.K_LEFT else current_bird_type + 1) % len(config.BIRD_TYPES)
                    bird.change_bird_type(current_bird_type)

        # Update hover animation
        hover_time += hover_speed
        bird.y = original_y + math.sin(hover_time) * hover_range
        
        # Only update animation, not position
        bird.animation_counter += 1
        if bird.animation_counter >= bird.animation_speed:
            bird.animation_counter = 0
            bird.animation_index = (bird.animation_index + 1) % len(bird.animation_frames)
            bird.current_image = bird.animation_frames[bird.animation_index]

        base_x = (base_x - 4) % config.BASE_IMAGE.get_width()

        # Draw menu screen
        config.SCREEN.blit(config.BACKGROUND_IMAGE, (0, 0))
        
        # Draw welcome message
        message_x = (config.SCREEN_WIDTH - config.MESSAGE_IMAGE.get_width()) // 2
        message_y = (config.SCREEN_HEIGHT - config.MESSAGE_IMAGE.get_height()) // 2 - 100
        config.SCREEN.blit(config.MESSAGE_IMAGE, (message_x, message_y))
        
        # Draw bird selection text
        bird_text = font.render(f"< {config.BIRD_TYPES[current_bird_type]['name']} Bird >", True, (255, 255, 255))
        text_rect = bird_text.get_rect(center=(config.SCREEN_WIDTH/2, config.SCREEN_HEIGHT - 150))
        config.SCREEN.blit(bird_text, text_rect)
        
        # Draw bird
        bird.draw(config.SCREEN)
        
        # Draw base
        config.SCREEN.blit(config.BASE_IMAGE, (base_x, config.SCREEN_HEIGHT - config.BASE_HEIGHT))
        config.SCREEN.blit(config.BASE_IMAGE, (base_x + config.BASE_IMAGE.get_width(), config.SCREEN_HEIGHT - config.BASE_HEIGHT))
        config.SCREEN.blit(config.BASE_IMAGE, (base_x - config.BASE_IMAGE.get_width(), config.SCREEN_HEIGHT - config.BASE_HEIGHT))

        pygame.display.update()
        config.CLOCK.tick(config.FPS)