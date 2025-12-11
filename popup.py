import pygame
import os
import subprocess

def popup():
    
    pygame.init()
    pygame.font.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("popup")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    font = pygame.font.SysFont("Arial", 18)

    output = subprocess.check_output("upower -i /org/freedesktop/UPower/devices/battery_BAT0", shell=True).decode("utf-8")

    lines = output.split("\n")


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        y = 15
        for line in lines:
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (20, y))
            y += 22  # line spacing

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    popup()
