import numpy as np
import pygame
from shapely.geometry import Polygon


def check_collision_and_containment(square_coords, pentagon_coords):
    square = Polygon(square_coords)
    pentagon = Polygon(pentagon_coords)

    # Check if square is within the pentagon
    is_within = pentagon.contains(square)

    # Check for boundary collision
    boundary_collision = square.intersects(pentagon.exterior)

    return is_within, boundary_collision


# Example coordinates
square_coords = np.array([(3, 1), (3, 2), (4, 2), (4, 1)])
pentagon_coords = [(0, 0), (4, 0), (5, 3), (2.5, 5), (0, 3)]

# Scale coordinates for better visualization
scale = 100
square_coords = [(x * scale, y * scale) for x, y in square_coords]
pentagon_coords = [(x * scale, y * scale) for x, y in pentagon_coords]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Polygon Collision Detection")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Check collision and containment
is_within, boundary_collision = check_collision_and_containment(square_coords, pentagon_coords)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    # Draw pentagon
    pygame.draw.polygon(screen, green if is_within else red, pentagon_coords, 2)

    # Draw square
    pygame.draw.polygon(screen, black, square_coords, 2)

    pygame.display.flip()

pygame.quit()
