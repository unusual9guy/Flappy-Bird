"""
The main file of the game with the main game loop
Run this file to play the game
"""


import pygame
import sys
import Score
import Pipe
import Bird
import config

# Initialize Pygame
pygame.init()


def main():
    high_score = 0  # Keep track of high score outside the game loop
    
    while True:
        # Show menu config.screen and get selected bird type
        selected_bird_type = Score.show_menu_screen()
        
        # Start game with selected bird
        bird = Bird.Bird(selected_bird_type)
        pipes = [Pipe.Pipe(config.SCREEN_WIDTH + i * Pipe.Pipe.get_random_spacing()) for i in range(3)]
        base_x = 0
        game_active = True
        score =     Score.Score()
        score.high_score = high_score  # Set the current high score

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if game_active:
                            bird.jump()
                        else:
                            if config.SWOOSH_SOUND:
                                config.SWOOSH_SOUND.play()
                            high_score = max(high_score, score.score)
                            break

            if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                break  # Break inner loop to return to menu

            if game_active:
                bird.move()
                for pipe in pipes:
                    pipe.move()
                    if pipe.x < -config.PIPE_IMAGE.get_width():
                        rightmost_x = max(p.x for p in pipes)
                        pipes.remove(pipe)
                        pipes.append(Pipe.Pipe(rightmost_x + Pipe.Pipe.get_random_spacing()))

                score.update(bird, pipes)

                if bird.check_collision(pipes):
                    game_active = False

                base_x = (base_x - 4) % config.BASE_IMAGE.get_width()

            # Draw everything
            config.SCREEN.blit(config.BACKGROUND_IMAGE, (0, 0))
            bird.draw(config.SCREEN)
            for pipe in pipes:
                pipe.draw(config.SCREEN)
            
            config.SCREEN.blit(config.BASE_IMAGE, (base_x, config.SCREEN_HEIGHT - config.BASE_HEIGHT))
            config.SCREEN.blit(config.BASE_IMAGE, (base_x + config.BASE_IMAGE.get_width(), config.SCREEN_HEIGHT - config.BASE_HEIGHT))
            config.SCREEN.blit(config.BASE_IMAGE, (base_x - config.BASE_IMAGE.get_width(), config.SCREEN_HEIGHT - config.BASE_HEIGHT))

            score.draw(config.SCREEN)

            if not game_active:
                # Update high score as soon as game ends
                high_score = max(high_score, score.score)
                
                # Draw game over image
                game_over_x = (config.SCREEN_WIDTH - config.GAME_OVER_IMAGE.get_width()) // 2
                game_over_y = config. SCREEN_HEIGHT // 3 - 50
                config.SCREEN.blit(config.GAME_OVER_IMAGE, (game_over_x, game_over_y))
                
                # Draw score panel with medal and scores
                Score.draw_score_panel(config.SCREEN, score.score, high_score)

            pygame.display.update()
            config.CLOCK.tick(config.FPS)

if __name__ == "__main__":
    main()