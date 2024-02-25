from GameFiles import Board
import pygame

class GameLogic:
    def __init__(self):
        self.board = Board(800, 600)
        self.player = 0 # 0 = player1, 1 = player 2 
        self.was_pressed = []
        self.board_state = [0] * 9 

    def reset(self):
        self.player = 0
        self.was_pressed = []
        self.board_state = [0] * 9
        self.board.draw_board()

    def switch_player(self):
        if self.player == 0:
            self.player = 1
        else : self.player = 0

    def draw(self, x, y):
        if self.player == 0:
            player1 = True
        else: player1 = False

        if player1 == True:
                self.board.draw_x(x, y)
                self.board_state[x // 266 + (y // 200) * 3] = 1
        else: 
            self.board.draw_o(x, y)
            self.board_state[x // 266 + (y // 200) * 3] = 2

        pygame.display.update()

    def pressed(self, key):
        for i in self.was_pressed: 
            if i == key:
                return True
        return False

    def handle_inputs(self, event):
        if event.key == pygame.K_1:
            if not self.pressed(1):
                self.draw(0, 0)
                self.was_pressed.append(1)
                self.switch_player()
        elif event.key == pygame.K_2:
            if not self.pressed(2):
                self.draw(266, 0)
                self.switch_player()
                self.was_pressed.append(2)
        elif event.key == pygame.K_3:
            if not self.pressed(3):
                self.draw(532, 0)
                self.switch_player()
                self.was_pressed.append(3)
        elif event.key == pygame.K_4:
            if not self.pressed(4):
                self.draw(0, 200)
                self.switch_player()
                self.was_pressed.append(4)
        elif event.key == pygame.K_5:
            if not self.pressed(5):
                self.draw(266, 200)
                self.switch_player()
                self.was_pressed.append(5)
        elif event.key == pygame.K_6:
            if not self.pressed(6):
                self.draw(532, 200)
                self.switch_player()
                self.was_pressed.append(6)
        elif event.key == pygame.K_7:
            if not self.pressed(7):
                self.draw(0, 400)
                self.switch_player()
                self.was_pressed.append(7)
        elif event.key == pygame.K_8:
            if not self.pressed(8):
                self.draw(266, 400)
                self.switch_player()
                self.was_pressed.append(8)
        elif event.key == pygame.K_9:
            if not self.pressed(9):
                self.draw(532, 400)
                self.switch_player()
                self.was_pressed.append(9)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                self.handle_inputs(event)

            winner = self.check_winner(self.board_state)
            if winner:
                print(winner)
                self.reset()

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True

        self.board.draw_board()
        while running:
            clock.tick(60)
            self.handle_event()

    def check_winner(self, board_state):
        winning_pos = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0, 0]
        ]

        for pos in winning_pos:
            player1_wins = all(
                board_state[i] == 1 if pos[i] == 1 else True
                for i in range(len(pos))
            )
            player2_wins = all(
                board_state[i] == 2 if pos[i] == 1 else True
                for i in range(len(pos))
            )

            if player1_wins:
                return "Player 1 wins!"
            elif player2_wins:
                return "Player 2 wins!"
            
        if all(cell != 0 for cell in board_state):
            return "It's a draw!"


        return None

    
