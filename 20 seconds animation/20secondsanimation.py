import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Task Performance Finals')

texture1 = pygame.image.load('texture1.jpg')
texture2 = pygame.image.load('texture2.jpg')

object1_pos = [-200, -200]
object2_pos = [400, 400]

speed1 = 2
speed2 = 1

duration = 20000

# Main game loop
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update object positions
    object1_pos[0] += speed1
    object2_pos[0] -= speed2 

    # Boundaries
    object1_pos[0] = object1_pos[0] % (width + texture1.get_width())
    object2_pos[0] = object2_pos[0] % (width + texture2.get_width())

    screen.fill((255, 255, 255))

    # Repitition
    for i in range(-(width + texture1.get_width()), width + texture1.get_width(), texture1.get_width()):
        screen.blit(texture1, (object1_pos[0] + i, object1_pos[1]))

    for i in range(-(width + texture2.get_width()), width + texture2.get_width(), texture2.get_width()):
        screen.blit(texture2, (object2_pos[0] + i, object2_pos[1]))

    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if current_time - start_time >= duration:
        pygame.quit()
        sys.exit()

    # FPS
    clock.tick(120)
