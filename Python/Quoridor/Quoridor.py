'''
-time: 2023/07/14 01:07
-author: https://github.com/Arrieeee
-note: This code is still in production. Not all features have been added. Please feel free to contribute to the repository.
'''


import pygame


# Define constants for the grid
GRID_SIZE = 9
BLOCK_SIZE = 50
SPACE_SIZE = 10
WINDOW_PADDING = 20
WINDOW_WIDTH = (BLOCK_SIZE + SPACE_SIZE) * GRID_SIZE + SPACE_SIZE + 2 * WINDOW_PADDING
WINDOW_HEIGHT = (BLOCK_SIZE + SPACE_SIZE) * GRID_SIZE + SPACE_SIZE + 2 * WINDOW_PADDING

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WINDOW_GRADIENT_START = (230, 230, 230)
WINDOW_GRADIENT_END = (180, 180, 180)
BLOCK_COLOR = (100, 100, 100)
PLAYER_COLOR_TOP = (255, 165, 0)  # Orange
PLAYER_COLOR_BOTTOM = (255, 0, 0)  # Red


class Block:
    def __init__(self, row, col, size, space, padding):
        self.row = row
        self.col = col
        self.size = size
        self.space = space
        self.padding = padding
        self.color = BLOCK_COLOR

    def draw(self, window):
        x = (self.size + self.space) * self.col + self.space + self.padding
        y = (self.size + self.space) * self.row + self.space + self.padding

        pygame.draw.rect(window, self.color, (x, y, self.size, self.size))
        pygame.draw.rect(window, BLACK, (x, y, self.size, self.size), 2)


class Player:
    def __init__(self, row, col, size, space, padding, color, total_walls):
        self.row = row
        self.col = col
        self.size = size
        self.space = space
        self.padding = padding
        self.color = color
        self.walls = total_walls

    def draw(self, window):
        x = (self.size + self.space) * self.col + self.space + self.padding
        y = (self.size + self.space) * self.row + self.space + self.padding

        pygame.draw.circle(window, self.color, (x + self.size // 2, y + self.size // 2), self.size // 2)
        pygame.draw.circle(window, BLACK, (x + self.size // 2, y + self.size // 2), self.size // 2, 2)

    def move_up(self, grid):
        if self.row > 0 and not grid.is_player_at(self.row - 1, self.col):
            self.row -= 1

    def move_down(self, grid):
        if self.row < grid.size - 1 and not grid.is_player_at(self.row + 1, self.col):
            self.row += 1

    def move_left(self, grid):
        if self.col > 0 and not grid.is_player_at(self.row, self.col - 1):
            self.col -= 1

    def move_right(self, grid):
        if self.col < grid.size - 1 and not grid.is_player_at(self.row, self.col + 1):
            self.col += 1


class Grid:
    def __init__(self, size, block_size, space_size, window_padding):
        self.size = size
        self.block_size = block_size
        self.space_size = space_size
        self.window_padding = window_padding
        self.blocks = []
        self.players = []
        self.current_player = 1  # Index of the current player in the players list
        self.game_over = False  # Flag to track game state
        self.winner = None

        self.create_blocks()
        self.create_players()

    def create_blocks(self):
        for row in range(self.size):
            for col in range(self.size):
                block = Block(row, col, self.block_size, self.space_size, self.window_padding)
                self.blocks.append(block)

    def create_players(self):
        player1 = Player(0, 4, self.block_size, self.space_size, self.window_padding, PLAYER_COLOR_TOP, 10)
        player2 = Player(self.size - 1, 4, self.block_size, self.space_size, self.window_padding, PLAYER_COLOR_BOTTOM, 10)
        self.players = [player1, player2]

    def draw(self, window):
        for block in self.blocks:
            block.draw(window)

        for player in self.players:
            player.draw(window)

    def switch_player(self):
        if self.game_over:
            return
        self.current_player = (self.current_player + 1) % len(self.players)

    def handle_key_event(self, event):
        if self.game_over:
            return

        player = self.players[self.current_player]
        prev_row, prev_col = player.row, player.col

        if event.key == pygame.K_UP:
            player.move_up(self)
        elif event.key == pygame.K_DOWN:
            player.move_down(self)
        elif event.key == pygame.K_LEFT:
            player.move_left(self)
        elif event.key == pygame.K_RIGHT:
            player.move_right(self)

        if player.row != prev_row or player.col != prev_col:
            self.switch_player()

    def check_winner(self):
        top_player = self.players[0]
        bottom_player = self.players[1]

        if top_player.row == self.size - 1:
            self.game_over = True
            self.winner = top_player
        elif bottom_player.row == 0:
            self.game_over = True
            self.winner = bottom_player

        return self.winner


class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.window = None
        self.grid = None

    def initialize_pygame(self):
        pygame.init()

    def quit_game(self):
        pygame.quit()

    def create_window(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + 2 * WINDOW_PADDING))
        pygame.display.set_caption("Quoridor!")

    def create_grid(self):
        self.grid = Grid(self.grid_size, BLOCK_SIZE, SPACE_SIZE, WINDOW_PADDING)

    def draw_background(self):
        self.window.fill(WHITE)

        # Draw top rectangle (orange)
        orange_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_PADDING)
        pygame.draw.rect(self.window, PLAYER_COLOR_TOP, orange_rect)

        # Draw bottom rectangle (red)
        red_rect = pygame.Rect(0, WINDOW_HEIGHT + WINDOW_PADDING, WINDOW_WIDTH, WINDOW_PADDING)
        pygame.draw.rect(self.window, PLAYER_COLOR_BOTTOM, red_rect)

        for y in range(WINDOW_HEIGHT):
            gradient_color = tuple(
                int(WINDOW_GRADIENT_START[i] + (WINDOW_GRADIENT_END[i] - WINDOW_GRADIENT_START[i]) * y / WINDOW_HEIGHT)
                for i in range(3)
            )
            pygame.draw.line(self.window, gradient_color, (0, y + WINDOW_PADDING), (WINDOW_WIDTH, y + WINDOW_PADDING))

    def show_current_player_turn(self):
        current_player = self.grid.players[self.grid.current_player]
        if current_player.color == PLAYER_COLOR_TOP:
            color_text =f"Current Player: Orange (Total Walls: {current_player.walls})"
        else:
            color_text = f"Current Player: Red (Total Walls: {current_player.walls})"
        font = pygame.font.SysFont(None, 30)
        text_surface = font.render(color_text, True, BLACK)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_PADDING // 2))
        self.window.blit(text_surface, text_rect)

    def display_winner(self, player):
        winner_text = "Winner: "
        if player.color == PLAYER_COLOR_TOP:
            winner_text += "Orange"
        else:
            winner_text += "Red"

        font = pygame.font.SysFont(None, 40)
        winner_surface = font.render(winner_text, True, BLACK)
        winner_rect = winner_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_PADDING // 2))

        self.window.blit(winner_surface, winner_rect)

    def run(self):
        self.initialize_pygame()
        self.create_window()
        self.create_grid()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.grid.handle_key_event(event)

            self.draw_background()
            self.grid.draw(self.window)
            self.show_current_player_turn()
            winner = self.grid.check_winner()
            if winner is not None:
                self.display_winner(winner)
            pygame.display.update()

        self.quit_game()


if __name__ == "__main__":
    game = Game(GRID_SIZE)
    game.run()
