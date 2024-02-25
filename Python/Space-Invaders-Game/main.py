import sys
import pygame
import Player
import Enemy
import UI.Button
from ScreenState import *
import Spawner
global screen
# Window Resolution
Width = 852 * 1.5
Height = 480 * 1.5

# The game has different screen states, on startup it will be SCREEN_START which is the start menu
CurrentScreenState = SCREEN_START

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
# Set the screen resolution
screen = pygame.display.set_mode((Width, Height))
# Set the window title
pygame.display.set_caption('Kai\'s Game')

# Store the states
ShowDebugMenu = True
DrawHitBoxes = False
DrawCoords = False

# Variables initialized for SCREEN_PLAY

# Load Player.png
PlayerImage = pygame.image.load("Player.png")
PlayerImage = pygame.transform.scale(PlayerImage, (100, 100))
Player1 = Player.Player(PlayerImage)
# Set the initial position of the player
Player1.Move((0, Player1.get_rect().height * 6))

# All enemies are stored in this enemy list
EnemyList = []
# Set number of enemies to create
EnemyCount = 10

PlayerImage = pygame.transform.scale(PlayerImage, (90, 90))
Spawner.AddEnemiesToList(EnemyList, EnemyCount, PlayerImage)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# Create font to draw text
font = pygame.font.Font('freesansbold.ttf', 15)

# Main game loop
while True:
    MouseDown = False  # Store if the current frame has the left mouse button down
    screen.fill((30, 30, 30))  # Create a grey background
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                # Invert DrawHitBoxes bool
                DrawHitBoxes = not DrawHitBoxes
            if event.key == pygame.K_F1:
                # Invert ShowDebugMenu bool
                ShowDebugMenu = not ShowDebugMenu
            if event.key == pygame.K_j:
                # Invert DrawCoords bool
                DrawCoords = not DrawCoords

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            MouseDown = True

    keys = pygame.key.get_pressed()
    # Convert to int to remove decimals then cast to string
    fps = str(int(clock.get_fps()))

    if CurrentScreenState == SCREEN_START:
        # Start Screen of the game
        btnFont = pygame.font.Font('freesansbold.ttf', 50)
        StartBtn = UI.Button.Button(
            btnFont, "Start", white, (Width / 2, Height / 2))

        if MouseDown:
            mouse = pygame.mouse.get_pos()
            if StartBtn.IsMouseOnTop(mouse):
                CurrentScreenState = SCREEN_PLAY
        # End of Start Screen
    elif CurrentScreenState == SCREEN_PLAY:

        Player1.HandleInput(keys)
        Player1.UpdatePosition()
        Player1.DrawHitbox()
        Player1.DrawCoords()

        # Make laser visible
        for laser in Player1.Lasers:
            laser.UpdatePosition()
            laser.LaserMove()
            laser.DrawCoords()

        for enemy in EnemyList:
            enemy.EnemyMove()
            enemy.DrawHitbox()
            enemy.DrawCoords()
            if enemy.IsHitByLaser(Player1.Lasers):
                print("Hit")
                enemy.Kill()

            if Player1.IsHitByEnemy(enemy):
                CurrentScreenState = SCREEN_GAMEOVER
                print("Game Over")

        if len(EnemyList) == 0:
            CurrentScreenState = SCREEN_GAMEOVER

    elif CurrentScreenState == SCREEN_GAMEOVER:
        # Game Over Screen
        btnFont = pygame.font.Font('freesansbold.ttf', 50)
        StartBtn = UI.Button.Button(
            btnFont, "Play Again", white, (Width / 2, Height / 2))

        if MouseDown:
            mouse = pygame.mouse.get_pos()
            if StartBtn.IsMouseOnTop(mouse):
                CurrentScreenState = SCREEN_PLAY

                Player1.Move((0, Player1.get_rect().height * 6))
                EnemyList.clear()
                Spawner.AddEnemiesToList(EnemyList, EnemyCount, PlayerImage)
        ####

    # Draw debug menu at the end so it overlays the whole screen
    if ShowDebugMenu:
        textList = []
        textList.append(f"Toggle this menu with the [F1] Key")
        textList.append(f"FPS: {fps}")
        textList.append(f"[H] Show Hitboxes: {DrawHitBoxes}")
        textList.append(f"[J] Show Coordinates: {DrawCoords}")
        textList.append(f"Enemies Left: {len(EnemyList)}")
        for count, s in enumerate(textList):
            text = font.render(s, True, white)
            textRect = text.get_rect()
            screen.blit(text, (Width - textRect.width - 10,
                        10 + (textRect.height + 10) * count))

    pygame.display.update()
