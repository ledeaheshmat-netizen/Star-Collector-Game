import random
import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 22, HEIGHT - 90, 44, 44)
        self.lives = 3

    def update(self, keys):
        dx = (int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])) * PLAYER_SPEED
        dy = (int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])) * PLAYER_SPEED
        self.rect.move_ip(dx, dy)
        self.rect.clamp_ip(pygame.Rect(0, 95, WIDTH, HEIGHT - 95))

    def draw(self, surface):
        pygame.draw.ellipse(surface, (55, 34, 80), self.rect.move(2, 5))
        pygame.draw.ellipse(surface, (255, 170, 210), self.rect)
        pygame.draw.circle(surface, (55, 34, 80), (self.rect.centerx - 9, self.rect.centery - 4), 3)
        pygame.draw.circle(surface, (55, 34, 80), (self.rect.centerx + 9, self.rect.centery - 4), 3)
        pygame.draw.arc(surface, (130, 50, 100), self.rect.inflate(-20, -17).move(0, 5), 0, 3.14, 2)

class FallingObject:
    def __init__(self, kind):
        self.kind = kind
        self.radius = 16 if kind == 'star' else 19
        self.x = random.randint(30, WIDTH - 30)
        self.y = -30
        self.speed = random.uniform(2.5, 4.5) if kind == 'star' else random.uniform(3, 5)

    def update(self):
        self.y += self.speed

    def collides(self, rect):
        return rect.collidepoint(self.x, self.y) or rect.inflate(self.radius * 2, self.radius * 2).collidepoint(self.x, self.y)

    def draw(self, surface):
        x, y = int(self.x), int(self.y)
        if self.kind == 'star':
            import math
            points = []
            for i in range(10):
                angle = -math.pi / 2 + i * math.pi / 5
                r = 19 if i % 2 == 0 else 9
                points.append((x + int(math.cos(angle) * r), y + int(math.sin(angle) * r)))
            pygame.draw.polygon(surface, (255, 204, 56), points)
            pygame.draw.polygon(surface, (255, 244, 181), points, 2)
        else:
            pygame.draw.circle(surface, (110, 63, 143), (x, y), self.radius)
            pygame.draw.circle(surface, (185, 133, 218), (x - 5, y - 5), 6)
            pygame.draw.line(surface, (75, 37, 105), (x - 8, y + 5), (x + 8, y - 4), 3)
