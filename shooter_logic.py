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

# Константи для ворога
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 50
ENEMY_VELOCITY = 3

# Константи для життя
PLAYER_LIVES = 3

# Функція для малювання гравця
def draw_player(player):
    pygame.draw.rect(WIN, WHITE, player)

# Функція для малювання ворога
def draw_enemy(enemy):
    pygame.draw.rect(WIN, RED, enemy)

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
def handle_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY > 0:
        player.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player.x + PLAYER_WIDTH + PLAYER_VELOCITY < WIDTH:
        player.x += PLAYER_VELOCITY
    if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY > 0:
        player.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and player.y + PLAYER_HEIGHT + PLAYER_VELOCITY < HEIGHT:
        player.y += PLAYER_VELOCITY

# Функція для перевірки колізій
def check_collisions(player, enemy):
    return player.colliderect(enemy)

# Функція для обновлення позиції ворога
def update_enemy_position(enemy):
    direction = random.choice([-1, 1])
    enemy.x += direction * ENEMY_VELOCITY
    if enemy.x <= 0:
        enemy.x = 0
    elif enemy.x >= WIDTH - ENEMY_WIDTH:
        enemy.x = WIDTH - ENEMY_WIDTH

# Основна функція гри
def main():
    player = pygame.Rect(WIDTH/2 - PLAYER_WIDTH/2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    enemy = pygame.Rect(WIDTH/2 - ENEMY_WIDTH/2, 10, ENEMY_WIDTH, ENEMY_HEIGHT)

    clock = pygame.time.Clock()

    player_lives = PLAYER_LIVES

    while True:
        WIN.fill(BLACK)

        draw_player(player)
        draw_enemy(enemy)

        handle_events(player)

        update_enemy_position(enemy)

        if check_collisions(player, enemy):
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
