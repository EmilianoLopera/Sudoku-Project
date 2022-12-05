import pygame, sys
from constants import *
from sudoku_generator import Board, generate_sudoku


def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    # Color background
    screen.fill(BG_COLOR)
    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    start_message_font = pygame.font.Font(None, 75)
    button_font = pygame.font.Font(None, 70)
    # Color background
    # Initialize and draw title
    message_surface = start_message_font.render("Select a game mode", 0, LINE_COLOR)
    message_rectangle = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 70))
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
        center=(WIDTH // 2, HEIGHT // 2 + 50))
    medium_rectangle = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    hard_rectangle = hard_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 250))
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
                    # Checks if mouse is on start button
                    return  # If the mouse is on the start button, we can return to
                elif medium_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()


def draw_game_over(screen):
    game_over_font = pygame.font.Font(None, 40)
    screen.fill(BG_COLOR)
    if winner != 0:
        text = "Game Won!"

    else:
        text = "No one wins!"
    game_over_surf = game_over_font.render(text, 0, LINE_COLOR)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)
    restart_surf = game_over_font.render(
        'Press r to play again...', 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)
    #  Added key to return to main menu
    menu_surf = game_over_font.render(
        'Press m to return to the main menu...', 0, LINE_COLOR)
    menu_rect = menu_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(menu_surf, menu_rect)


if __name__ == '__main__':
    game_over = False
    chip = 'x'
    winner = 0
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    draw_game_start(screen)  # Calls function to draw start screen
    screen.fill(BG_COLOR)

    for i in range(1, 9):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                         (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        if i == 3 or i == 6:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                BOLD_LINE
            )

    # draw vertical lines
    for i in range(1, 9):
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                         (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)
        if i == 3 or i == 6:
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                BOLD_LINE
            )
    for i in range(9):
        for j in range(9):
            pass
            #cells[i][j].draw(screen)


    # draw_lines()
    # middle_cell = Cell('o', 1, 1, 200, 200)
    # middle_cell.draw(screen)
    #board = Board(9, 9, WIDTH, HEIGHT, screen)
    # board.print_board()
    #board.draw()
    x = generate_sudoku(9, 9)
    for y in x:
        for j in y:
            print(j, end=" ")
        print()


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                clicked_row = int(event.pos[1] / SQUARE_SIZE)
                clicked_col = int(event.pos[0] / SQUARE_SIZE)
                print(clicked_row, clicked_col)
                if board.available_square(clicked_row, clicked_col):
                    board.print_board()
                    board.mark_square(clicked_row, clicked_col, chip)
                    if board.check_if_winner(chip):
                        if chip == 'X':
                            winner = 1
                        else:
                            winner = 2
                        game_over = True
                    else:
                        if board.board_is_full():
                            winner = 0
                            game_over = True
                    chip = 'o' if chip == 'x' else 'x'
                    board.draw()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                    chip = 'x'
                    board.reset_board()
                    screen.fill(BG_COLOR)
                    board.draw()
                if event.key == pygame.K_m:
                    #  If the user presses m, return to the main menu
                    game_over = False
                    chip = 'x'
                    board.reset_board()
                    draw_game_start(screen)
                    screen.fill(BG_COLOR)
                    board.draw()
        # game is over
        if game_over:
            pygame.display.update()
            pygame.time.delay(1000)
            draw_game_over(screen)
        pygame.display.update()