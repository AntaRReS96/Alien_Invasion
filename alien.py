import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie."""

    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Umieszczanie nowego obcecgo w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego poziomego położenia obcego.
        self.x = float(self.rect.x)


    def check_edges(self):
        """Zwraca wartość True, jeśli obcyznajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


    def update(self):
        """Przesunięcie obcego w prawo lub lewo"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x


    def alien_animation(self):
        """Zmiana wyglądu obcego co 10 przesunięć"""
        while True:
            pygame.time.set_timer(self.change_alien_image(), 2000)


    def change_alien_image(self):
        image_flag = True
        if image_flag:
            self.image = pygame.image.load('images/alien2.png')
            image_flag = False
        else:
            self.image = pygame.image.load('images/alien.png')
            image_flag = True