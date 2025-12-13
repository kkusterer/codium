import pygame
def popup():
    pygame.init()

    # make window
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("Button Example")

    # button setings
    button_color = (0, 150, 255)
    button_rect = pygame.Rect(200, 200, 200, 60)  # x, y, width, height

    # text and font
    font = pygame.font.Font(None, 36)
    button_text = font.render("HI", True, (225, 225, 225))
    button_text_rect = button_text.get_rect(center=button_rect.center)

    # loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # checks for button click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Button clicked!")

        # background
        screen.fill((30, 30, 30))

        # make button
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, button_text_rect)

        # update display
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    for i in range(5):
        popup()
