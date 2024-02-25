from Entity import *

# Laser -> Entity -> Object


class Laser(Entity):
    def __init__(self, pygameObj, parent):
        super().__init__(pygameObj)
        # Pass parent as a mutable object so its a reference and not a copy of the object
        self.Parent = parent[0]
        self.m_iSpeed = 10
        self.m_VecPosition = pygame.Vector2(
            self.Parent.m_VecPosition.x, self.Parent.m_VecPosition.y)

    def LaserMove(self):
        selfRect = self.m_Object.get_rect()
        from main import Height, Width
        newY = self.m_VecPosition.y - self.m_iSpeed
        newX = self.m_VecPosition.x

        # Check if the laser's new position is within range of the screen
        if newX >= 0 and newX <= Width - self.m_Object.get_rect().width and newY >= 0 and newY <= Height:
            self.m_VecPosition.x = newX
            self.m_VecPosition.y = newY

        if self.m_VecPosition.y == 0:
            self.Parent.Lasers.remove(self)
