import random
import sys
import pygame
from settings import WIDTH, HEIGHT, FPS, GAME_SECONDS, TARGET_SCORE
from entities import Player, FallingObject

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Star Collector | Collect the Stars')
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 27, bold=True)
large = pygame.font.SysFont('arial', 62, bold=True)
small = pygame.font.SysFont('arial', 23)


def text(message, face, color, center):
    image = face.render(message, True, color)
    screen.blit(image, image.get_rect(center=center))


def background():
    screen.fill((247, 228, 249))
    pygame.draw.rect(screen, (227, 192, 240), (0, 0, WIDTH, 88))
    for i in range(8):
        x = 55 + i * 118
        pygame.draw.circle(screen, (255, 248, 255), (x, 150 + (i % 3) * 95), 6)
    pygame.draw.rect(screen, (231, 206, 243), (0, HEIGHT - 35, WIDTH, 35))


def new_game():
    return Player(), [], 0, pygame.time.get_ticks(), pygame.time.get_ticks(), 'playing'


player, objects, score, start, last_spawn, state = new_game()
state = 'start'
running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE and state in ('start', 'won', 'lost'):
                player, objects, score, start, last_spawn, state = new_game()

    background()
    if state == 'playing':
        now = pygame.time.get_ticks()
        remaining = max(0, GAME_SECONDS - (now - start) // 1000)
        player.update(pygame.key.get_pressed())
        if now - last_spawn > 550:
            objects.append(FallingObject('star' if random.random() < 0.72 else 'rock'))
            last_spawn = now
        for item in objects[:]:
            item.update()
            if item.collides(player.rect):
                if item.kind == 'star':
                    score += 1
                else:
                    player.lives -= 1
                objects.remove(item)
            elif item.y > HEIGHT + 30:
                objects.remove(item)
            else:
                item.draw(screen)
        player.draw(screen)
        text(f'Stars: {score}/{TARGET_SCORE}', font, (70, 42, 96), (135, 44))
        text(f'Lives: {player.lives}', font, (70, 42, 96), (445, 44))
        text(f'Time: {remaining}s', font, (70, 42, 96), (760, 44))
        if score >= TARGET_SCORE:
            state = 'won'
        elif player.lives <= 0 or remaining <= 0:
            state = 'lost'
    else:
        if state == 'start':
            text('STAR COLLECTOR', large, (105, 53, 137), (WIDTH // 2, 210))
            text('Collect 15 stars and avoid the purple rocks!', small, (88, 55, 103), (WIDTH // 2, 290))
            text('Move: Arrow Keys or WASD', small, (88, 55, 103), (WIDTH // 2, 330))
        elif state == 'won':
            text('YOU WIN!', large, (105, 53, 137), (WIDTH // 2, 225))
            text(f'You collected {score} stars!', font, (88, 55, 103), (WIDTH // 2, 305))
        else:
            text('GAME OVER', large, (105, 53, 137), (WIDTH // 2, 225))
            text(f'Stars collected: {score}', font, (88, 55, 103), (WIDTH // 2, 305))
        text('Press SPACE to play', font, (82, 39, 118), (WIDTH // 2, 405))
        text('ESC to quit', small, (112, 83, 124), (WIDTH // 2, 450))
    pygame.display.flip()
pygame.quit()
sys.exit()
