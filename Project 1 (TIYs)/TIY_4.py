import pygame
import sys

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket Game Screen")


rocket_image = pygame.image.load("images/rocketimage.png")
rocket_image = pygame.transform.scale(rocket_image, (90, 120))  
rocket_rect = rocket_image.get_rect()
rocket_rect.center = (screen_width // 2, screen_height // 2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rocket_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        rocket_rect.x += 5
    if keys[pygame.K_UP]:
        rocket_rect.y -= 5
    if keys[pygame.K_DOWN]:
        rocket_rect.y += 5

    rocket_rect.clamp_ip(screen.get_rect())


    screen.fill((0, 0, 255)) 

    screen.blit(rocket_image, rocket_rect)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()