from Entity import *
import Laser
import pygame

# Player -> Entity -> Object


class Player(Entity):
    def __init__(self, pygameObj):
        super().__init__(pygameObj)
        self.Lasers = []

    def HandleInput(self, keys):
        newX = self.m_VecPosition.x
        newY = self.m_VecPosition.y
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            newX -= self.m_iSpeed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            newX += self.m_iSpeed
        if keys[pygame.K_SPACE]:
            if len(self.Lasers) == 0:
                self.InitLaser()
        from main import Width, Height
        # Check if the player's new position is within range of the screen
        if newX > 0 and newX <= Width - self.m_Object.get_rect().width:
            self.m_VecPosition.x = newX

    def IsHitByEnemy(self, Enemy):
        x = Enemy.m_VecPosition.x
        y = Enemy.m_VecPosition.y
        return self.get_rect().collidepoint(x, y)

    def InitLaser(self):
        laserSurface = pygame.Surface((15, 30), pygame.SRCALPHA)
        laserSurface.fill(color=(255, 0, 0))
        # Pass parent as a mutable object so its a reference and not a copy of the object, using [self]
        newLaser = Laser.Laser(laserSurface, [self])
        self.Lasers.append(newLaser)
