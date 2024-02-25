import pygame

class Board:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('Tic-Tac-Toe')

    def draw_board(self):
        self.screen.fill('black')


        pygame.draw.line(self.screen, 'white', (self.window_width // 3, 0), (self.window_width // 3, self.window_height), 5)
        pygame.draw.line(self.screen, 'white', (self.window_width // 3 * 2, 0), (self.window_width // 3 * 2, self.window_height), 5)
        
        pygame.draw.line(self.screen, 'white', (0, self.window_height // 3), (self.window_width, self.window_height // 3), 5)
        pygame.draw.line(self.screen, 'white', (0, self.window_height // 3 * 2), (self.window_width, self.window_height // 3 * 2), 5)

        font = pygame.font.Font(None, 36)  

        for i in range(3):
            for j in range(3):
                num = i * 3 + j + 1  # Calculate the number to display in the cube
                text = font.render(str(num), True, 'white')
                text_rect = text.get_rect(center=(j * self.window_width // 3 + self.window_width // 6, i * self.window_height // 3 + self.window_height // 6))
                self.screen.blit(text, text_rect)

        pygame.display.flip()
        
    def draw_x(self, x, y):
        size = 50
        cell_size = 100
        offset = (cell_size - size) // 2

        x += (cell_size - size) // 2 + offset + 58
        y += (cell_size - size) // 2 + offset + 25

        pygame.draw.line(self.screen, 'white', (x, y), (x + size, y + size), 5)
        pygame.draw.line(self.screen, 'white', (x, y + size), (x + size, y), 5)

    def draw_o(self, x, y):
        size = 50
        cell_size = 100
        offset = (cell_size - size) // 2

        x += (cell_size - size) // 2 + offset + 58
        y += (cell_size - size) // 2 + offset + 25

        radius = size // 2
        center = (x + radius, y + radius)
        pygame.draw.circle(self.screen, 'white', center, radius, 5)

