import pygame

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text Input Example")

# Define the font for rendering text
font = pygame.font.Font(None, 36)

# Initialize variables
input_text = ""
typing = True

# Input handling loop
while typing:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit loop if user closes the window
            typing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Exit loop if Enter key is pressed
                typing = False
            elif event.key == pygame.K_BACKSPACE:
                # Remove last character if Backspace key is pressed
                input_text = input_text[:-1]
            else:
                # Add typed character to input_text
                input_text += event.unicode
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Render input_text using the defined font
    text_surface = font.render("Enter Text: " + input_text, True, (0, 0, 0))
    
    # Blit the rendered text onto the screen
    screen.blit(text_surface, (10, 10))
    
    # Update the display
    pygame.display.update()

# Clean up and exit Pygame
pygame.quit()

