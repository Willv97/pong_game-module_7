# Pong Game

import pygame
import random

# Global variables
WIDTH = 800
HEIGHT = 400
FPS = 60

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Variables
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]
player_score = 0

# Define the paddle rectangle
paddle_rect = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 50, 10, 100)

# Function to handle collisions
def handle_collisions():
    global ball_speed, player_score

    # If the ball hits the top or bottom walls, reverse the y-direction
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # If the ball hits the player's paddle, reverse the x-direction and increase score
    if ball_pos[0] <= 10 and paddle_rect.collidepoint(ball_pos):
        ball_speed[0] = -ball_speed[0]
        player_score += 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Decision structure: If the ball goes off the screen, end the game
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH:
        running = False

    # Repetition structure: Draw the ball and paddle on the screen
    pygame.draw.circle(screen, WHITE, ball_pos, 10)
    pygame.draw.rect(screen, WHITE, paddle_rect)

    # Function call: Handle collisions
    handle_collisions()

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Game over
print("Game over! Your score:", player_score)

# End of the program
