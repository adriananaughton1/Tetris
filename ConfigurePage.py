from GamePage import PlayGame
import pygame
import sys


pygame.init()

# Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SELECTED_COLOR = (173, 216, 239)  # Light Blue
DEFAULT_COLOR = (255, 255, 255)  # White
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)


class ConfigurePage:
    def __init__(self):
        self.selected_size = "10x20"
        self.game_lines = 0
        self.selected_level = "Easy"
        self.game_mode = "Normal"
        self.player_mode = "Player"

        self.size_options = ["5x20", "10x20", "15x20"]
        self.size_5x20_rect = pygame.Rect(50, 150, 200, 50)
        self.size_10x20_rect = pygame.Rect(300, 150, 200, 50)
        self.size_15x20_rect = pygame.Rect(550, 150, 200, 50)
        self.easy_mode_rect = pygame.Rect(50, 265, 200, 50)
        self.medium_mode_rect = pygame.Rect(300, 265, 200, 50)
        self.hard_mode_rect = pygame.Rect(550, 265, 200, 50)
        self.normal_mode_rect = pygame.Rect(50, 380, 200, 50)
        self.extended_mode_rect = pygame.Rect(300, 380, 200, 50)
        self.player_mode_rect = pygame.Rect(50, 520, 200, 50)
        self.ai_mode_rect = pygame.Rect(300, 520, 200, 50)
        self.close_button_rect = pygame.Rect(750, 650, 100, 30)
        self.back_button_rect = pygame.Rect(50, 650, 100, 30)
        self.play_game = None
        # user game configurations
        self.gameExtension = True
        self.AiMode = False
        self.gameLevel = "Easy"  # Set self.gameLevel to a string representing the desired difficulty level

        # user chooses game length
        self.boardSize = 10  # board width


    def draw_configure_page(self, screen):
        screen.fill(WHITE)

        # Determine button colors based on user selections
        size_5x20_color = SELECTED_COLOR if self.selected_size == "5x20" else pygame.Color('gray')
        size_10x20_color = SELECTED_COLOR if self.selected_size == "10x20" else pygame.Color('gray')
        size_15x20_color = SELECTED_COLOR if self.selected_size == "15x20" else pygame.Color('gray')
        easy_mode_color = SELECTED_COLOR if self.selected_level == "Easy" else pygame.Color('gray')
        medium_mode_color = SELECTED_COLOR if self.selected_level == "Medium" else pygame.Color('gray')
        hard_mode_color = SELECTED_COLOR if self.selected_level == "Hard" else pygame.Color('gray')
        normal_mode_color = SELECTED_COLOR if self.game_mode == "Normal" else pygame.Color('gray')
        extended_mode_color = SELECTED_COLOR if self.game_mode == "Extended" else pygame.Color('gray')
        player_mode_color = SELECTED_COLOR if self.player_mode == "Player" else pygame.Color('gray')
        ai_mode_color = SELECTED_COLOR if self.player_mode == "AI" else pygame.Color('gray')

        # Draw size buttons
        text = FONT.render("Field size:", True, pygame.Color('black'))
        screen.blit(text, (50, 110))
        size_5x20_text = FONT.render("5x20", True, pygame.Color('black'))
        size_10x20_text = FONT.render("10x20", True, pygame.Color('black'))
        size_15x20_text = FONT.render("15x20", True, pygame.Color('black'))
        pygame.draw.rect(screen, size_5x20_color, self.size_5x20_rect)
        pygame.draw.rect(screen, size_10x20_color, self.size_10x20_rect)
        pygame.draw.rect(screen, size_15x20_color, self.size_15x20_rect)
        pygame.draw.rect(screen, pygame.Color('black'), self.size_5x20_rect, 2)
        pygame.draw.rect(screen, pygame.Color('black'), self.size_10x20_rect, 2)
        pygame.draw.rect(screen, pygame.Color('black'), self.size_15x20_rect, 2)

        screen.blit(size_5x20_text, (self.size_5x20_rect.x + 20, self.size_5x20_rect.y + 15))
        screen.blit(size_10x20_text, (self.size_10x20_rect.x + 20, self.size_10x20_rect.y + 15))
        screen.blit(size_15x20_text, (self.size_15x20_rect.x + 20, self.size_15x20_rect.y + 15))

        # Draw level buttons
        text = FONT.render("Game level:", True, pygame.Color('black'))
        screen.blit(text, (50, 230))

        pygame.draw.rect(screen, easy_mode_color, self.easy_mode_rect)
        pygame.draw.rect(screen, medium_mode_color, self.medium_mode_rect)
        pygame.draw.rect(screen, hard_mode_color, self.hard_mode_rect)

        easy_text = FONT.render("Easy", True, pygame.Color('black'))
        medium_text = FONT.render("Medium", True, pygame.Color('black'))
        hard_text = FONT.render("Hard", True, pygame.Color('black'))

        screen.blit(easy_text, (self.easy_mode_rect.x + 10, self.easy_mode_rect.y + 10))
        screen.blit(medium_text, (self.medium_mode_rect.x + 10, self.medium_mode_rect.y + 10))
        screen.blit(hard_text, (self.hard_mode_rect.x + 10, self.hard_mode_rect.y + 10))

        pygame.draw.rect(screen, pygame.Color('black'), self.easy_mode_rect, 2)
        pygame.draw.rect(screen, pygame.Color('black'), self.medium_mode_rect, 2)
        pygame.draw.rect(screen, pygame.Color('black'), self.hard_mode_rect, 2)

        # Drawing the Game Mode buttons
        text = FONT.render("Game mode:", True, pygame.Color('black'))
        screen.blit(text, (50, 345))
        pygame.draw.rect(screen, normal_mode_color, self.normal_mode_rect)
        pygame.draw.rect(screen, extended_mode_color, self.extended_mode_rect)
        pygame.draw.rect(screen, pygame.Color('black'), self.normal_mode_rect, 2)
        pygame.draw.rect(screen, pygame.Color('black'), self.extended_mode_rect, 2)

        normal_text = FONT.render("Normal", True, pygame.Color('black'))
        extended_text = FONT.render("Extended", True, pygame.Color('black'))

        screen.blit(normal_text, (self.normal_mode_rect.x + 10, self.normal_mode_rect.y + 10))
        screen.blit(extended_text, (self.extended_mode_rect.x + 10, self.extended_mode_rect.y + 10))

        # Drawing the Player Mode buttons
        pygame.draw.rect(screen, player_mode_color, self.player_mode_rect)
        pygame.draw.rect(screen, ai_mode_color, self.ai_mode_rect)
        pygame.draw.rect(screen, pygame.Color('black'), self.player_mode_rect, 2)
        pygame.draw.rect(screen, pygame.Color('black'), self.ai_mode_rect, 2)

        player_text = FONT.render("Player", True, pygame.Color('black'))
        ai_text = FONT.render("AI", True, pygame.Color('black'))

        screen.blit(player_text, (self.player_mode_rect.x + 10, self.player_mode_rect.y + 10))
        screen.blit(ai_text, (self.ai_mode_rect.x + 10, self.ai_mode_rect.y + 10))

        #player mode label
        text = FONT.render("Player mode:", True, pygame.Color('black'))
        screen.blit(text, (50, 470))


        # Draw back button on the left side
        pygame.draw.rect(screen, pygame.Color('black'), self.back_button_rect)
        pygame.draw.rect(screen, pygame.Color('black'), self.back_button_rect, 2)
        back_text = FONT.render("Back", True, pygame.Color('white'))
        screen.blit(back_text, (self.back_button_rect.x + 10, self.back_button_rect.y + 5))

        # Calculate the position of the close button on the right side
        close_button_x = SCREEN_WIDTH - self.close_button_rect.width - 50

        # Draw close button on the right side
        close_button_rect = pygame.Rect(close_button_x, self.close_button_rect.y, self.close_button_rect.width,
                                        self.close_button_rect.height)
        pygame.draw.rect(screen, pygame.Color('black'), close_button_rect)
        pygame.draw.rect(screen, pygame.Color('black'), close_button_rect, 2)
        close_text = FONT.render("Close", True, pygame.Color('white'))
        screen.blit(close_text, (close_button_rect.x + 10, close_button_rect.y + 5))

        # Draw the Start button
        start_button_x = (SCREEN_WIDTH - 100) // 2  # Centered between Back and Close
        self.start_button_rect = pygame.Rect(start_button_x, 650, 100, 30)
        pygame.draw.rect(screen, pygame.Color('black'), self.start_button_rect)
        start_text = FONT.render("Start", True, pygame.Color('white'))
        screen.blit(start_text, (self.start_button_rect.x + 20, self.start_button_rect.y + 5))

    def HandleMouseClick(self, screen, configurePage, mouse_pos):
        # Handle board size buttons
        from StartupPage import StartupPage
        startPage = StartupPage()
        if self.size_10x20_rect.collidepoint(mouse_pos):
            self.selected_size = "10x20"
            self.getField()
        elif self.size_5x20_rect.collidepoint(mouse_pos):
            self.selected_size = "5x20"
            self.getField()
        elif self.size_15x20_rect.collidepoint(mouse_pos):
            self.selected_size = "15x20"
            self.getField()

        # Handle game level buttons
        elif self.easy_mode_rect.collidepoint(mouse_pos):
            self.selected_level = "Easy"
            self.getLevel()
        elif self.medium_mode_rect.collidepoint(mouse_pos):
            self.selected_level = "Medium"
            self.getLevel()
        elif self.hard_mode_rect.collidepoint(mouse_pos):
            self.selected_level = "Hard"
            self.getLevel()

        # Handle game mode buttons
        elif self.normal_mode_rect.collidepoint(mouse_pos):
            self.game_mode = "Normal"
        elif self.extended_mode_rect.collidepoint(mouse_pos):
            self.game_mode = "Extended"

        # Handle player mode buttons
        elif self.player_mode_rect.collidepoint(mouse_pos):
            self.player_mode = "Player"
        elif self.ai_mode_rect.collidepoint(mouse_pos):
            self.player_mode = "AI"

        # Handle system buttons
        elif self.close_button_rect.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()
        elif self.start_button_rect.collidepoint(mouse_pos):

            clock = pygame.time.Clock()  # start clock
            pygame.time.set_timer(pygame.USEREVENT, 300)
            run = True  # run game variable
            self.boardSize = self.getField()
            self.gameLevel = self.getLevel()
            game = PlayGame(self.boardSize, self.gameExtension, self.AiMode, self.gameLevel)
            rotate_sound = pygame.mixer.Sound("can_rotate.wav")

            if self.AiMode:  # AI Playing
                while run:
                    screen.fill((0, 0, 0))  # black background
                    game.DrawGame(configurePage)

                    for event in list(pygame.event.get()):
                        if event.type == pygame.QUIT:  # user quits
                            if (self.QuitGame()):
                                run = False
                                sys.exit()
                            else:
                                continue

                    if game.AiMove == False:  # AI decides move
                        moves = game.RunAi()
                        # print(moves)

                    # get first/next move
                    if len(moves) != 0:
                        makeMove = moves[0]
                        moves.remove(makeMove)

                    # make move
                    if makeMove == "up":
                        game.Rotate()
                    elif makeMove == "down":
                        game.BlockFalls()
                    elif makeMove == "left":
                        game.MoveBlock(False)
                    elif makeMove == "right":
                        game.MoveBlock(True)
                    game.BlockFalls()

                    if game.gameOver == True:
                        run = False
                    pygame.display.update()
                    clock.tick(30)

            else:  # User Playing
                while run:
                    # DISPLAY - fill screen with grid and surfaces
                    screen.fill((0, 0, 0))  # black background
                    game.DrawGame(configurePage)

                    # PLAYER ACTIONS
                    for event in list(pygame.event.get()):

                        if event.type == pygame.QUIT:  # user quits
                            if startPage.QuitGame():
                                run = False
                                sys.exit()
                            else:
                                continue
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:  # quits with escape key
                                if startPage.QuitGame():
                                    run = False
                                    sys.exit()
                                else:
                                    continue

                            if event.key == pygame.K_RIGHT:  # move right
                                game.MoveBlock(True)
                            if event.key == pygame.K_LEFT:  # move left
                                game.MoveBlock(False)
                            if event.key == pygame.K_UP:  # rotate
                                game.Rotate()
                                rotate_sound.play()
                            if event.key == pygame.K_DOWN:  # move down
                                game.BlockFalls()

                        if event.type == pygame.USEREVENT:
                            game.BlockFalls()

                    if game.gameOver == True:
                        run = False

                    pygame.display.update()
                    clock.tick(120)

        elif self.back_button_rect.collidepoint(mouse_pos):
            screen.fill((255, 255, 255))
            from StartupPage import StartupPage
            startup_page = StartupPage()
            startup_page.DrawStartupPage(screen)
            go = True
            # start page
            while go:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        startPage.HandleMouseClick(screen, mouse)
                pygame.display.flip()

        # Redraw the configure page with updated selections
        self.draw_configure_page(screen)
        pygame.display.flip()

    def getField(self):
        if self.selected_size == "5x20":
            return 5
        elif self.selected_size == "10x20":
            return 10
        elif self.selected_size == "15x20":
            return 15

    def getLevel(self):
        if self.selected_level == "Easy":
            return 1
        elif self.selected_level == "Medium":
            return 2
        elif self.selected_level == "Hard":
            return 3

    def play_game_loop(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Handle other events as needed for your game
            self.play_game.BlockFalls()
            self.play_game.MoveBlock(True)
            self.play_game.Rotate()  # Handle rotations
            self.play_game.DrawGame(screen)
            pygame.display.flip()
            clock.tick(60)  # Limit frame rate to 60 FPS

    def set_level(self, level):
        self.selected_level = level
        if self.play_game:
            self.play_game.handle_configuration(level)

    def start_game(self):
        boardWidth, boardHeight = self.get_board_size()
        self.play_game = PlayGame(boardWidth, boardHeight, self.selected_level, self.game_mode, self.player_mode)
        self.play_game_loop()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")

    configure_page = ConfigurePage()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                configure_page.HandleMouseClick(screen, mouse_pos)

        configure_page.draw_configure_page(screen)
        pygame.display.flip()
        clock.tick(60)  # Limit frame rate to 60 FPS

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()


