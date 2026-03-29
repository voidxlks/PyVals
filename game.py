import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyVals - 2D Rivals")

clock = pygame.time.Clock()

# Players
player1 = pygame.Rect(100, 300, 50, 50)
player2 = pygame.Rect(750, 300, 50, 50)

speed = 5
attack_range = 60
damage = 5

p1_health = 100
p2_health = 100

# Colors
WHITE = (255, 255, 255)
BLUE = (80, 150, 255)
RED = (255, 80, 80)
BLACK = (15, 15, 15)
GREEN = (0, 255, 0)

font = pygame.font.SysFont(None, 30)

def draw():
    screen.fill(BLACK)

    # Players
    pygame.draw.rect(screen, BLUE, player1)
    pygame.draw.rect(screen, RED, player2)

    # Health bars
    pygame.draw.rect(screen, RED, (50, 50, 200, 20))
    pygame.draw.rect(screen, GREEN, (50, 50, 2 * p1_health, 20))

    pygame.draw.rect(screen, RED, (650, 50, 200, 20))
    pygame.draw.rect(screen, GREEN, (650, 50, 2 * p2_health, 20))

    # Text
    text = font.render("WASD + F | Arrows + L", True, WHITE)
    screen.blit(text, (WIDTH//2 - 120, 10))

    pygame.display.update()

def handle_movement(keys):
    # Player 1 (WASD)
    if keys[pygame.K_a]:
        player1.x -= speed
    if keys[pygame.K_d]:
        player1.x += speed
    if keys[pygame.K_w]:
        player1.y -= speed
    if keys[pygame.K_s]:
        player1.y += speed

    # Player 2 (Arrow keys)
    if keys[pygame.K_LEFT]:
        player2.x -= speed
    if keys[pygame.K_RIGHT]:
        player2.x += speed
    if keys[pygame.K_UP]:
        player2.y -= speed
    if keys[pygame.K_DOWN]:
        player2.y += speed

def handle_attacks(keys):
    global p1_health, p2_health

    # Player 1 attack (F)
    if keys[pygame.K_f]:
        if player1.colliderect(player2.inflate(attack_range, attack_range)):
            p2_health -= damage

    # Player 2 attack (L)
    if keys[pygame.K_l]:
        if player2.colliderect(player1.inflate(attack_range, attack_range)):
            p1_health -= damage

def check_winner():
    if p1_health <= 0:
        return "Player 2 Wins!"
    if p2_health <= 0:
        return "Player 1 Wins!"
    return None

def show_winner(text):
    win_text = font.render(text, True, WHITE)
    screen.blit(win_text, (WIDTH//2 - 80, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global p1_health, p2_health

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        handle_movement(keys)
        handle_attacks(keys)

        winner = check_winner()
        if winner:
            draw()
            show_winner(winner)
            p1_health, p2_health = 100, 100
            player1.x, player1.y = 100, 300
            player2.x, player2.y = 750, 300

        draw()

if __name__ == "__main__":
    main()
