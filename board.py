import pygame
from constants import *
class Board:
    def __init__(self, width, height, screen, difficulty, board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = board


    def draw(self, screen):
        x = self.board
        for j in range(len(x)):
            for q in range(len(x[j])):
                if x[j][q] != 0:
                    position = (((j) * 67) + 22, ((q) * 65) + 15)
                    font = pygame.font.SysFont('arial', 50)
                    text = font.render(str(x[j][q]), True, (0, 0, 0))
                    screen.blit(text, position)
                pygame.display.update()

        for i in range(1, 10):
            pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            if i == 3 or i == 6 or i == 9:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    BOLD_LINE
                )

        # draw vertical lines
        for i in range(1, 10):
            pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, HEIGHT - 100), LINE_WIDTH)
            if i == 3 or i == 6 or i == 9:
                pygame.draw.line(
                    screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT - 100),
                    BOLD_LINE
                )
    def select(self, row, col):
        # self.draw(self.screen)
        self.draw(self.screen)

        x = (row ) * 67
        y = (col ) * 67
        pygame.draw.line(self.screen, (255,0,0), (x,y) ,(x +65,y), 1)
        pygame.draw.line(self.screen, (255, 0, 0), (x, y),(x, y + 65), 1)
        pygame.draw.line(self.screen, (255, 0, 0), (x+65, y), (x+65, y + 65),1)
        pygame.draw.line(self.screen, (255, 0, 0), (x, y+65), (x + 65, y + 65), 1)
        pass

    def click(self, x, y):

        clicked_row = int(x/ SQUARE_SIZE)
        clicked_col = int(y / SQUARE_SIZE)
        return (clicked_row, clicked_col)
        pass

    def clear(self,x_cord,y_cord):
        pygame.draw.rect(self.screen , (255,255,245) , ((x_cord)*67+2,(y_cord)*67 + 2,45,45))
        pass

    def sketch(self, value,row,col):
        # self.clear(row,col)
        cell = (row) * 67 + 5, (col) * 67 + 3
        self.clear(row, col)
        font = pygame.font.SysFont('arial', 15)
        text = font.render(str(value), True, (50,50,50))
        self.screen.blit(text, cell)
        pygame.display.update()
        pass

    def place(self, value, pos_x , pos_y):
        if value != 0:
            self.clear(pos_x, pos_y)
            cell = (pos_x) * 67 + 20, (pos_y) * 67 + 5
            self.clear(pos_x, pos_y)
            font = pygame.font.SysFont('arial', 50)
            text = font.render(str(value), True, (50, 50, 50))
            self.screen.blit(text, cell)
            pygame.display.update()

        pass
    def reset_to_original(self, key):
        for i in range(9):
            for j in range(9):
                if(key[i][j] == 0):
                    self.clear(i,j)
        return

