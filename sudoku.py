import pygame, sys
from constants import *
from sudoku_generator import *
from board import Board
import copy

image = pygame.image.load('backround.jpg')
DEFAULT_IMAGE_SIZE = (600,700)
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)


def draw_game_start(screen):

    # Initialize title font
    start_title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 40)
    screen.blit(image, (0,0))
    pygame.display.flip()
    # Color background
    # screen.fill(BG_COLOR)
    # Initialize and draw title
    title_surface = start_title_font.render("Welcome to Sudoku", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 300))
    screen.blit(title_surface, title_rectangle)

    start_message_font = pygame.font.Font(None, 65)
    button_font = pygame.font.Font(None, 70)
    # Color background
    # Initialize and draw title
    message_surface = start_message_font.render("Select a game mode:", 0, (0, 0, 0))
    message_rectangle = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 130))
    screen.blit(message_surface, message_rectangle)


    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    quit_text = button_font.render("Quit", 0, (255, 255, 255))
    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(LINE_COLOR)
    quit_surface.blit(quit_text, (10, 10))
    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 220))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 220))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 220))
    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 550))
    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    screen.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30


                    # Checks if mouse is on start button

              # If the mouse is on the start button, we can return to
                elif medium_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return 40


                elif hard_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return 50


                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()



def draw_game_over(screen):
    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)

    screen.blit(image, (0,0))
    pygame.display.flip()

    title_surface = start_title_font.render("Game Over :( ", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(restart_surface, restart_rectangle)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()

def draw_game_won(screen):
    start_title_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 50)

    screen.blit(image, (0, 0))
    pygame.display.flip()

    title_surface = start_title_font.render("Game Won!!!", 0, (0, 0, 0))
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(exit_surface, exit_rectangle)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    sys.exit()


def main():
    game_over = False
    chip = 'x'
    winner = 0
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    difficulty = draw_game_start(screen)  # Calls function to draw start screen
    screen.fill(BG_COLOR)

    button_font = pygame.font.Font(None, 40)
    restart_text = button_font.render("restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 300))

    reset_text = button_font.render("reset", 0, (255, 255, 255))
    exit_text = button_font.render("exit", 0, (255, 255, 255))
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # Initialize button rectangle
    medium_rectangle = reset_surface.get_rect(
        center=(WIDTH // 2 - 107, HEIGHT // 2 + 300))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2 + 100, HEIGHT // 2 + 300))

    grid, master = generate_sudoku1(9, difficulty)
    reset_board = copy.deepcopy(grid.board)
    grid2 = Board(WIDTH, HEIGHT, screen, 2, grid.get_board())

    arr = copy.deepcopy(grid.get_board())

    grid2.draw(screen)


    screen.blit(restart_surface, restart_rectangle)
    screen.blit(reset_surface, medium_rectangle)
    screen.blit(exit_surface, exit_rectangle)


    while True:

        # x, y = None, None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                ex_x, ex_y = event.pos

                x, y = ex_x, ex_y
                # print(x, y)
                if (y <= 600):
                    x, y = grid2.click(x, y)
                    grid2.select(x, y)

                # reset button
                if (ex_x >= 150 and ex_x <= 240) and (ex_y >= 620 and ex_y <= 675):

                    grid2.reset_to_original(reset_board)
                    arr = copy.deepcopy(reset_board)
                # restart button the main screen
                if (ex_x >= 260 and ex_x <= 350) and (ex_y >= 620 and ex_y <= 675):
                    draw_game_start(screen)
                    main()

                    pass

                if (ex_x >= 366 and ex_x <= 435) and (ex_y >= 627 and ex_y <= 670):
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if grid.get_board()[x][y] == 0:
                    if event.key == pygame.K_1:
                        num = 1
                        grid2.sketch(1, x, y)
                    if event.key == pygame.K_2:
                        num = 2
                        grid2.sketch(2, x, y)
                    if event.key == pygame.K_3:
                        num = 3
                        grid2.sketch(3, x, y)
                    if event.key == pygame.K_4:
                        num = 4
                        grid2.sketch(4, x, y)
                    if event.key == pygame.K_5:
                        num = 5
                        grid2.sketch(5, x, y)
                    if event.key == pygame.K_6:
                        num = 6
                        grid2.sketch(6, x, y)
                    if event.key == pygame.K_7:
                        num = 7
                        grid2.sketch(7, x, y)
                    if event.key == pygame.K_8:
                        grid2.sketch(8, x, y)
                        num = 8
                    if event.key == pygame.K_9:
                        num = 9

                        grid2.sketch(9, x, y)
                    # make a
                    if event.key == pygame.K_RETURN:
                        # if(num != -1):
                        grid2.place(num, x, y)
                        arr[x][y] = num
                        num = 0

                        full = True
                        for i in range(9):
                            for j in range(9):
                                if arr[i][j] == 0:
                                    full = False

                        if full:
                            correct = True
                            for i in range(9):
                                for j in range(9):
                                    if (arr[i][j] != master[i][j]):
                                        correct = False

                            if correct:
                                draw_game_won(screen)


                            else:
                                draw_game_over(screen)


                        pass
                    if event.key == pygame.K_BACKSPACE:
                        grid2.clear(x, y)
                        arr[x][y] = 0
                        num = 0



                    pass


        # game is over
        if game_over:
            pygame.display.update()
            pygame.time.delay(1000)
            draw_game_over(screen)
        pygame.display.update()



if __name__ == '__main__':
    main()
