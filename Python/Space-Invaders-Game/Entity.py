from Object import *

# Entity -> Object


class Entity(Object):
    def __init__(self, pygameObj):
        super().__init__(pygameObj)
        self.m_iSpeed = 10

    # Position is a pygame Vector2
    def Move(self, Position):
        self.m_VecPosition = pygame.Vector2(Position)
        self.screen.blit(self.m_Object, Position)

    # #Updates position on screen from self.m_VecPosition member variable
    def UpdatePosition(self):
        self.Move(self.m_VecPosition)

    def DrawHitbox(self):
        from main import DrawHitBoxes
        if DrawHitBoxes:
            pygame.draw.rect(self.screen, (255, 0, 0), self.get_rect(), 2)

    def DrawCoords(self):
        from main import DrawCoords, font
        if DrawCoords:
            text = font.render(str(self.m_VecPosition), True, (255, 255, 255))
            textRect = text.get_rect()
            self.screen.blit(text, self.m_VecPosition)
