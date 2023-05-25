import pygame

class Sfx:
    """Przechowywanie efektów dźwiękowych."""

    def __init__(self, ai_game):
        self.laser = pygame.mixer.Sound('sounds/laser.wav')
        self.explosion = pygame.mixer.Sound('sounds/explosion.wav')