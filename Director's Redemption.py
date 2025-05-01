import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT_NAME = pygame.font.match_font('arial')

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DIRECTOR'S REDEMPTION")

font_large = pygame.font.Font(FONT_NAME, 40)
font_medium = pygame.font.Font(FONT_NAME, 28)
font_small = pygame.font.Font(FONT_NAME, 22)

clock = pygame.time.Clock()

def draw_text(surface, text, size, color, x, y, center=True):
    font = pygame.font.Font(FONT_NAME, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

def input_names():
    names = ["", "", ""]
    current_input = 0
    input_active = True

    while input_active:
        screen.fill(WHITE)
        draw_text(screen, "Enter 3 names:", 36, BLACK, WIDTH // 2, 40)
        for i in range(3):
            color = RED if i == current_input else BLACK
            draw_text(screen, f"Name {i+1}: {names[i]}", 28, color, WIDTH // 2, 100 + i*50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    names[current_input] = names[current_input][:-1]
                elif event.key == pygame.K_RETURN:
                    if names[current_input].strip() != "":
                        current_input += 1
                        if current_input >= 3:
                            input_active = False
                else:
                    if len(names[current_input]) < 15 and event.unicode.isprintable():
                        names[current_input] += event.unicode

        pygame.display.flip()
        clock.tick(30)

    return names

def tossing_animation(names):
    selected_index = None
    toss_time = 2000 
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < toss_time:
        screen.fill(WHITE)
        elapsed = pygame.time.get_ticks() - start_time
        # Cycle through names quickly
        current_index = (elapsed // 200) % 3
        draw_text(screen, "Tossing...", 40, BLACK, WIDTH // 2, 50)
        for i, name in enumerate(names):
            color = RED if i == current_index else BLACK
            draw_text(screen, name, 36, color, WIDTH // 2, 150 + i*50)
        pygame.display.flip()
        clock.tick(30)

    selected_index = random.randint(0, 2)
    return selected_index

def main():
    running = True
    while running:
        names = input_names()
        selected = tossing_animation(names)

        result_shown = True
        while result_shown:
            screen.fill(WHITE)
            draw_text(screen, "DIRECTOR'S REDEMPTION", 40, BLACK, WIDTH // 2, 40)
            draw_text(screen, f"The Director is:", 32, BLACK, WIDTH // 2, 120)
            draw_text(screen, names[selected], 48, RED, WIDTH // 2, 180)
            draw_text(screen, "Press R to restart or Q to quit", 24, BLACK, WIDTH // 2, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        result_shown = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    main()
