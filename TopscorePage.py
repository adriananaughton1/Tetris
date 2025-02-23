import sys
import pygame
import random

class HighscorePage:

    @staticmethod
    def ShowTopScores(screen):
        # Fetch scores from the PlayGame's method
        from GamePage import PlayGame
        scores = PlayGame.GetScores()

        font = pygame.font.SysFont('Courier', 50, 'bold')

        screen.fill((255, 255, 255))

        title_text = font.render('HIGHSCORES', True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(screen.get_width() // 2, 50))
        screen.blit(title_text, title_rect)

        font = pygame.font.SysFont('Courier', 30)

        # Top 10 scores
        for i, (name, score) in enumerate(scores, start=1):
            score_text = font.render(f'{name}: {score}', True, (0, 0, 0))
            score_rect = score_text.get_rect(center=(screen.get_width() // 2, 120 + i * 40))
            screen.blit(score_text, score_rect)

        # Calculate the position of the back and close buttons
        button_width, button_height = 200, 40
        button_spacing = 20
        total_button_width = 2 * button_width + button_spacing

        back_button_rect = pygame.Rect((screen.get_width() - total_button_width) // 2, 600, button_width, button_height)
        pygame.draw.rect(screen, (200, 0, 0), back_button_rect)
        back_button_text = font.render('Back', True, (255, 255, 255))
        back_text_rect = back_button_text.get_rect(center=back_button_rect.center)
        screen.blit(back_button_text, back_text_rect)

        close_button_rect = pygame.Rect(back_button_rect.right + button_spacing, 600, button_width, button_height)
        pygame.draw.rect(screen, (200, 0, 0), close_button_rect)
        close_button_text = font.render('Close', True, (255, 255, 255))
        close_text_rect = close_button_text.get_rect(center=close_button_rect.center)
        screen.blit(close_button_text, close_text_rect)

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if back_button_rect.collidepoint(mouse_pos):
                        screen.fill((255, 255, 255))
                        from StartupPage import StartupPage
                        startup_page = StartupPage()
                        startup_page.drawStartupPage(screen)
                        return
                    elif close_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

