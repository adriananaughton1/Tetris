# Tetris
import sys
import pygame
from ConfigurePage import ConfigurePage
from StartupPage import StartupPage
from GamePage import PlayGame

def main():
    # start page code
    pygame.init()
    win = pygame.display.set_mode((1000, 700))
    pygame.mouse.set_visible(1)
    win.fill((255, 255, 255))
    startupPage = StartupPage()
    startupPage.DrawStartupPage(win)
    go = True
    # start page
    while go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                startupPage.HandleMouseClick(win, mouse)

        pygame.display.flip()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
