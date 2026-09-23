import pygame
from settings import EntityType


# Base class
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos, type=EntityType.OTHER):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        # self.mask = pygame.mask.from_surface(self.image)
        self.type = type

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, dt):
        pass


class MovingSprite(BaseSprite):
    def __init__(self, image, pos, speed, type=EntityType.OTHER):
        super().__init__(image, pos, type)
        self.speed = speed
        self.x = float(pos[0])
        self.y = float(pos[1])

    def update(self, dt):
        self.x += self.speed * dt
        self.rect.x = round(self.x)


# rectangular collision check
def collide_rect(a, b) -> bool:
    return a.rect.colliderect(b.rect)


# mask collision check
# def collide_mask(a, b) -> bool:
#     return pygame.sprite.collide_mask(a, b)
