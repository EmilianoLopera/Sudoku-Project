import math, random
import pygame
from constants import *
from sudoku import *

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.rows = 9
        self.cols = 9
        self.difficulty = difficulty

    def draw(self):
        x = generate_sudoku(9, self.difficulty)
        button_font = pygame.font.Font(None, 70)
        restart_text = button_font.render("restart", 0, (255, 255, 255))
        reset_text = button_font.render("reset", 0, (255, 255, 255))
        exit_text = button_font.render("exit", 0, (255, 255, 255))
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        restart_rectangle = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 300))
        medium_rectangle = reset_surface.get_rect(center=(WIDTH // 2 - 200, HEIGHT // 2 + 300))
        exit_rectangle = exit_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 300))

        for j in range(len(x)):
            for q in range(len(x[j])):
                if x[j][q] != 0:
                    position = (((j) * 67) + 22, ((q) * 65) + 9.76)
                    font = pygame.font.SysFont('arial', 50)
                    text = font.render(str(x[j][q]), True, (0, 0, 0))
                    self.screen.blit(text, position)
                pygame.display.update()

        for i in range(1, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
            if i == 3 or i == 6 or i == 9:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    BOLD_LINE
                )

            # draw vertical lines
        for i in range(1, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, HEIGHT - 100), LINE_WIDTH)
            if i == 3 or i == 6 or i == 9:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT - 100),
                    BOLD_LINE
                )
                self.screen.blit(restart_surface, restart_rectangle)
                self.screen.blit(reset_surface, medium_rectangle)
                self.screen.blit(exit_surface, exit_rectangle)

        for i in range(9):
            for j in range(9):
                pass
                # cells[i][j].draw(screen)

        # draw cells
        """for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)
                pass"""

    def select(self, row, col):
       pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def is_full(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    return False

    def update_board(self):
        pass