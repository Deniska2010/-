import pygame
import sys
import random

# Ініціалізація Pygame
pygame.init()

# Константи для вікна гри
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шутер")

# Константи для кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Константи для гравця
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_VELOCITY = 5
PLAYER_BULLET_VELOCITY = 7

# Константи для ворога
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 50
ENEMY_VELOCITY = 3
ENEMY_BULLET_VELOCITY = 5

# Константи для життя
PLAYER_LIVES = 3

# Константи для куль
BULLET_WIDTH, BULLET_HEIGHT = 10, 20

# Функція для малювання гравця
def draw_player(player):
    pygame.draw.rect(WIN, WHITE, player)

# Функція для малювання ворога
def draw_enemy(enemy):
    pygame.draw.rect(WIN, RED, enemy)

# Функція для малювання куль
def draw_bullet(bullet):
    pygame.draw.rect(WIN, WHITE, bullet)

# Функція для відображення повідомлення про перемогу
def draw_win_message():
    font = pygame.font.SysFont(None, 100)
    text = font.render("You WIN!", True, WHITE)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

# Функція для відображення повідомлення про програш
def draw_lose_message():
    font = pygame.font.SysFont(None, 100)
    text = font.render("You LOSE", True, WHITE)
    WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

# Функція для обробки подій
def handle_events(player, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY > 0:
        player.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player.x + PLAYER_WIDTH + PLAYER_VELOCITY < WIDTH:
        player.x += PLAYER_VELOCITY
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player.x + PLAYER_WIDTH // 2 - BULLET_WIDTH // 2, player.y - BULLET_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT))
# Функція для обновлення позиції ворога
def update_enemy_position(enemy):
    direction = random.choice([-1, 1])
    enemy.x += direction * ENEMY_VELOCITY
    if enemy.x <= 0:
        enemy.x = 0
    elif enemy.x >= WIDTH - ENEMY_WIDTH:
        enemy.x = WIDTH - ENEMY_WIDTH

# Функція для стрільби ворога
def enemy_shoot(enemy, bullets):
    if random.randint(1, 50) == 1:
        bullets.append(pygame.Rect(enemy.x + ENEMY_WIDTH // 2 - BULLET_WIDTH // 2, enemy.y + ENEMY_HEIGHT, BULLET_WIDTH, BULLET_HEIGHT))

# Функція для обновлення позиції куль
def update_bullets(bullets, target):
    for bullet in bullets:
        bullet.y += ENEMY_BULLET_VELOCITY if target == "enemy" else -PLAYER_BULLET_VELOCITY

# Основна функція гри
def main():
    player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy = pygame.Rect(WIDTH/2 - ENEMY_WIDTH/2, 10, ENEMY_WIDTH, ENEMY_HEIGHT)

    bullets = []

    clock = pygame.time.Clock()

    player_lives = PLAYER_LIVES

    while True:
        WIN.fill(BLACK)

        draw_player(player)
        draw_enemy(enemy)

        handle_events(player, bullets)

        update_enemy_position(enemy)

        enemy_shoot(enemy, bullets)

        update_bullets(bullets, "enemy")

        for bullet in bullets:
            draw_bullet(bullet)

        if player.colliderect(enemy):
            player_lives -= 1
            if player_lives == 0:
                draw_lose_message()
                pygame.quit()
                sys.exit()

        if enemy.y >= HEIGHT - ENEMY_HEIGHT:
            draw_win_message()
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
