import pygame

from Settings.Engine.EngineSettings import engine_settings
from Engine.Database.Database import Database


class Engine:
    _surface = None
    _db = None
    
    def __init__(self):
        self._init_pygame()
        self._init_database()
        
    def _init_pygame(self):
        pygame.init()
        self._surface = pygame.Surface((1920,1080))
        
    def _init_database(self):
        self._db = Database(engine_settings["db_name"])
        
    @property
    def surface(self):
        return self._surface
        
    @property
    def db(self):
        return self._db