import pygame
import sys
import random
from GamePage import PlayGame

pygame.init()


class StartupPage:
    font = pygame.font.SysFont('Courier', 50, 'bold')

    def __init__(self):
        self.start = pygame.Rect(425, 440, 153, 50)
        self.scores = pygame.Rect(50, 600, 183, 50)
        self.configure = pygame.Rect(360, 600, 275, 50)
        self.exit = pygame.Rect(800, 600, 125, 50)

        # user game configurations
        self.gameExtension = False
        self.AiMode = False
        self.gameLevel = 1
        self.boardSize = 10  # board width

    def DrawStartupPage(self, startPage):
        pygame.display.set_caption('Welcome')
        pic = pygame.image.load('TetrisLogo.png')
        font = pygame.font.SysFont('Courier', 50, 'bold')
        font2 = pygame.font.SysFont('Courier', 20)
        yr = font2.render('2023, 2805ICT', True, (0, 0, 0))
        names = font2.render('Emily Gaelic, Sunwoo Nam, Adriana Naughton',
                             True, (0, 0, 0))
        text1 = font.render('Start', True, (0, 0, 0))
        text2 = font.render('Exit', True, (0, 0, 0))
        text3 = font.render('Scores', True, (0, 0, 0))
        text4 = font.render('Configure', True, (0, 0, 0))
        startPage.blit(pic, pic.get_rect(center=startPage.get_rect().center))
        startPage.blit(yr, (430, 10))
        startPage.blit(names, (250, 40))
        pygame.draw.rect(startPage, (255, 0, 0), self.exit)
        pygame.draw.rect(startPage, (255, 165, 0), self.configure)
        pygame.draw.rect(startPage, (0, 255, 0), self.start)
        pygame.draw.rect(startPage, (255, 255, 0), self.scores)
        startPage.blit(text1, (self.start.x, self.start.y))
        startPage.blit(text2, (self.exit.x, self.exit.y))
        startPage.blit(text3, (self.scores.x, self.scores.y))
        startPage.blit(text4, (self.configure.x, self.configure.y))

    def HandleMouseClick(self, startPage, mousePos):
        pygame.display.set_caption('Tetris 44')
        if self.exit.collidepoint(mousePos):
            pygame.quit()
            sys.exit()

        elif self.start.collidepoint(mousePos):  # GAME PLAY
            # clock = pygame.time.Clock()  # start clock
            # pygame.time.set_timer(pygame.USEREVENT, 300)
            # game = PlayGame(self.boardSize, self.gameExtension, self.AiMode, self.gameLevel)
            # rotate_sound = pygame.mixer.Sound("can_rotate.wav")
            # from ConfigurePage import ConfigurePage
            # configurePage = ConfigurePage()
            # self.boardSize = configurePage.getField()

            if self.AiMode:  # AI Playing
                self.AIPlaying(startPage)
            else:  # User Playing
                self.UserPlaying(startPage)

        elif self.configure.collidepoint(mousePos):
            from ConfigurePage import ConfigurePage
            configure_page = ConfigurePage()

            pygame.mixer.music.load("background.wav")
            pygame.mixer.music.play(-1)
            config = True
            while config:
                startPage.fill((0, 0, 0))
                pygame.display.set_caption("Tetris Setting")
                configure_page.draw_configure_page(startPage)
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif e.type == pygame.MOUSEBUTTONDOWN:
                        mousePos = pygame.mouse.get_pos()
                        config = configure_page.HandleMouseClick(startPage, mousePos)

                pygame.display.flip()
                clock = pygame.time.Clock()
                clock.tick(30)

            print("return from config page")
            self.DrawStartupPage(startPage)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        self.HandleMouseClick(startPage, mouse)
                pygame.display.flip()

        elif self.scores.collidepoint(mousePos):
            from TopscorePage import HighscorePage
            pygame.display.set_caption('Top Scores')

            # Generate random player scores
            # player_scores = [(f'Player {i}', random.randint(15000, 25000)) for i in range(1, 11)]

            # # Score range between 15000-25000
            # player_scores[0] = ('Player 1', 25000)
            # player_scores[-1] = ('Player 10', 15000)

            # # sort scores in desc order
            # player_scores.sort(key=lambda x: x[1], reverse=True)

            HighscorePage.ShowTopScores(startPage)

    def QuitGame(self):
        # new quit screen for confirming game exit
        quitScreen = pygame.display.set_mode((1000, 700))

        red = (255, 0, 0)
        white = (255, 255, 255)
        font = pygame.font.SysFont("Courier", 30)

        quit_rect = pygame.Rect(250, 250, 600, 200)
        yes_rect = pygame.Rect(350, 390, 100, 30)
        no_rect = pygame.Rect(600, 390, 100, 30)

        pygame.draw.rect(quitScreen, (red), quit_rect)
        pygame.draw.rect(quitScreen, (red), yes_rect)
        pygame.draw.rect(quitScreen, (red), no_rect)

        quit_surface = font.render("Are you sure you want to quit?", True, white)
        warning = font.render("Progress may be lost.", True, white)
        yes = font.render("Quit", True, white)
        no = font.render("Cancel", True, white)

        while True:
            quitScreen.blit(quit_surface, (300, 300))
            quitScreen.blit(warning, (300, 330))
            quitScreen.blit(yes, (350, 390))
            quitScreen.blit(no, (600, 390))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if yes_rect.collidepoint(mouse):
                        return True
                    elif no_rect.collidepoint(mouse):
                        return False

    def AIPlaying(self, startPage):
        clock = pygame.time.Clock()  # start clock
        pygame.time.set_timer(pygame.USEREVENT, 300)
        game = PlayGame(self.boardSize, self.gameExtension, self.AiMode, self.gameLevel)
        run = True  # run game variable
        while run:
            startPage.fill((0, 0, 0))  # black background
            game.DrawGame(startPage)

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

    def UserPlaying(self, startPage):
        clock = pygame.time.Clock()  # start clock
        pygame.time.set_timer(pygame.USEREVENT, 300)
        game = PlayGame(self.boardSize, self.gameExtension, self.AiMode, self.gameLevel)
        rotate_sound = pygame.mixer.Sound("can_rotate.wav")
        run = True  # run game variable
        while run:
            # DISPLAY - fill screen with grid and surfaces
            startPage.fill((0, 0, 0))  # black background
            game.DrawGame(startPage)

            # PLAYER ACTIONS
            for event in list(pygame.event.get()):

                if event.type == pygame.QUIT:  # user quits
                    if (self.QuitGame()):
                        run = False
                        sys.exit()
                    else:
                        continue
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # quits with escape key
                        if (self.QuitGame()):
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
            clock.tick(30)