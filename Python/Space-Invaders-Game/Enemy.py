from Entity import *

# Enemy -> Entity -> Object


class Enemy(Entity):
    # def __init__(self, pygameObj):
    #     super().__init__(pygameObj)

    def EnemyMove(self):
        selfRect = self.m_Object.get_rect()
        from main import Width
        newX = self.m_VecPosition.x
        newY = self.m_VecPosition.y
        if newX >= Width - selfRect.width - 100:
            newX = 1
            newY += selfRect.height
        else:
            newX += self.m_iSpeed

        # Check if the player's new position is within range of the screen
        if newX > 0 and newX <= Width - self.m_Object.get_rect().width:
            self.m_VecPosition.x = newX
            self.m_VecPosition.y = newY

        self.Move(self.m_VecPosition)

    def IsHitByLaser(self, PlayerLaserList):
        for laser in PlayerLaserList:
            x = laser.m_VecPosition.x
            y = laser.m_VecPosition.y
            if self.get_rect().collidepoint(x, y):
                return True

        return False

    def Kill(self):
        # Move somewhere off the screen to prevent flickering before disposing the object
        self.Move((-1000, -1000))
        from main import EnemyList
        EnemyList.remove(self)  # Remove from EnemyList
