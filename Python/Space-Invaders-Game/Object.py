import pygame


class Object:
    def __init__(self, pygameObj):
        self.m_VecPosition = pygame.Vector2(0, 0)
        self.m_Object = pygameObj
        from main import screen
        self.screen = screen

    def get_rect(self):
        return pygame.Rect(self.m_VecPosition.x, self.m_VecPosition.y, self.m_Object.get_rect().width, self.m_Object.get_rect().height)
