import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Game settings
gravity = 0.6
bird_movement = 0
bird_jump = -10
pipe_speed = 4
pipe_gap = 150

# Load assets
bird = pygame.Rect(100, screen_height // 2, 30, 30)
bird_image = pygame.Surface((30, 30))
bird_image.fill(BLUE)

# Pipes
pipe_width = 70
pipe_height = random.randint(200, 400)
pipe_x = screen_width
pipe_color = (0, 255, 0)

# Font
font = pygame.font.Font(None, 36)

# Game Variables
score = 0
game_active = True

# Function to check collisions
def check_collision(pipes):
    for pipe in pipes:
        if bird.colliderect(pipe):
            return False
    if bird.top <= 0 or bird.bottom >= screen_height:
        return False
    return True

# Main game loop
clock = pygame.time.Clock()
running = True
pipes = []
while running:
    screen.fill(WHITE)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = bird_jump
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipes.clear()
                bird.center = (100, screen_height // 2)
                bird_movement = 0
                score = 0

    if game_active:
        # Bird
        bird_movement += gravity
        bird.y += bird_movement
        screen.blit(bird_image, bird)

        # Pipes
        pipe_x -= pipe_speed
        if pipe_x <= -pipe_width:
            pipe_x = screen_width
            pipe_height = random.randint(200, 400)
            score += 1

        # Draw pipes
        pipe_top = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        pipe_bottom = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap)
        pygame.draw.rect(screen, pipe_color, pipe_top)
        pygame.draw.rect(screen, pipe_color, pipe_bottom)

        pipes = [pipe_top, pipe_bottom]

        # Collision Check
        game_active = check_collision(pipes)

        # Score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    else:
        # Game Over Screen
        game_over_text = font.render(f"Game Over! Score: {score}", True, BLACK)
        screen.blit(game_over_text, (screen_width // 4, screen_height // 2))

    pygame.display.update()
    clock.tick(60)

# Quit pygame
pygame.quit()