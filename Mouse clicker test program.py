import pygame # type: ignore
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Red to Green Screen')

# Set colors
red = (255, 0, 0)
green = (0, 255, 0)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check mouse button
    if pygame.mouse.get_pressed()[0]:
        screen.fill(green)
    else:
        screen.fill(red)

    # Update the display
    pygame.display.flip()
