import pygame

class Button():
    def __init__(self,font, text, color, Position):
        Position = pygame.Vector2(Position)
        Position.x -= 10
        Position.y -= 10
        self.Position = pygame.Vector2(Position)
        self.text = font.render(text, True, color)
        from main import screen
        self.screen = screen
        self.textRect = self.text.get_rect()
        ButtonBgRect = pygame.Rect(self.Position.x - 5 ,self.Position.y - 5,self.textRect.width + 10, self.textRect.height + 10)
        pygame.draw.rect(self.screen, (66,66,66), ButtonBgRect)
        self.screen.blit(self.text, self.Position)
        
    def IsMouseOnTop(self,MousePos):
        return MousePos[0] in range(int(self.Position.x),int(self.Position.x + self.textRect.width)) and MousePos[1] in range(int(self.Position.y),int(self.Position.y + self.textRect.height))