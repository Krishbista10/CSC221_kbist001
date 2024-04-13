import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Space Shooter")

GREEN = (0, 255, 0)  
WHITE = (255, 255, 255)  

clock = pygame.time.Clock()

ship_image = pygame.image.load("images/shipimage.png")
ship_image = pygame.transform.scale(ship_image, (70, 70))
ship_rect = ship_image.get_rect()
ship_y = screen_height // 2 - ship_rect.height // 2
ship_speed = 5

bullet_width = 10
bullet_height = 5
bullet_speed = 7
bullets = []

while True:
    screen.fill(GREEN)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(ship_rect.right, ship_y + ship_rect.height // 2 - bullet_height // 2, bullet_width, bullet_height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ship_y > 0:
        ship_y -= ship_speed
    if keys[pygame.K_DOWN] and ship_y < screen_height - ship_rect.height:
        ship_y += ship_speed

    for bullet in bullets:
        bullet.x += bullet_speed

    bullets = [bullet for bullet in bullets if bullet.x < screen_width]

    screen.blit(ship_image, (0, ship_y))

    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)  # Set bullet color to white

    pygame.display.flip()

    clock.tick(60)
