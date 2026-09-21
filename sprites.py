import pygame
from settings import EntityType


# Base class
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos, type=EntityType.OTHER):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.type = type

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self, dt):
        pass
