import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Button")

# Button
button_color = (0, 150, 255)
button_rect = pygame.Rect(100, 100, 200, 60)

# Fonts
font = pygame.font.Font(None, 36)
button_text = font.render("Click Me", True, (255, 255, 255))
button_text_rect = button_text.get_rect(center=button_rect.center)

goodboy_text = font.render("Good Boy", True, (255, 255, 255))
goodboy_rect = goodboy_text.get_rect(center=(200, 150))

# Game state
show_good_boy = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not show_good_boy and event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                show_good_boy = True
            

    screen.fill((30, 30, 30))

    if show_good_boy:
        # Show "Good Boy" screen
        screen.blit(goodboy_text, goodboy_rect)
    else:
        # Draw button
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, button_text_rect)

    pygame.display.update()

pygame.quit()
