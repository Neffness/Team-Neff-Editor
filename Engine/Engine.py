import pygame


class Engine:
    surface = None
    
    def __init__(self):
        pygame.init()
        self.surface = pygame.Surface((1920,1080))