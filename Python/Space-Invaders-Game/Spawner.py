import Enemy


def AddEnemiesToList(EnemyList, count, image):
    for i in range(1, count):
        newEnemy = Enemy.Enemy(image)
        newEnemy.m_iSpeed = 4
        newEnemy.m_VecPosition.x += i * (newEnemy.get_rect().width + 10)
        EnemyList.append(newEnemy)
