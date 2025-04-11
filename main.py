import os
import pygame
import subprocess

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# Fonts
pygame.font.init()
FONT = pygame.font.Font(None, 36)

# Function to run the game
def run_game(project):
    games_scripts = {
        "game1": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "subdir", "main.py"),
        "chess": os.path.join(os.path.dirname(os.path.abspath(__file__)), "games", "chess", "main.py"),
    }
    script_path = games_scripts.get(project)
    if script_path and os.path.exists(script_path):
        subprocess.run(["python", script_path])
    else:
        print(f"Error: Script for {project} not found!")

# Draw a button
def draw_button(screen, text, x, y, width, height, color, hover_color, is_hovered):
    button_color = hover_color if is_hovered else color
    pygame.draw.rect(screen, button_color, (x, y, width, height))
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

# Main application
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Personal Portfolio")

    # Load button image (optional)
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "download.png")
    button_image = None
    if os.path.exists(image_path):
        button_image = pygame.image.load(image_path)
        button_image = pygame.transform.scale(button_image, (50, 50))

    # Projects
    projects = ["game1", "chess", "game3", "game4", "game5"]

    # Button positions
    buttons = []
    for i, project in enumerate(projects):
        x = (SCREEN_WIDTH - BUTTON_WIDTH) // 2
        y = 150 + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
        buttons.append((project, x, y))

    running = True
    while running:
        screen.fill(WHITE)

        # Draw title
        title_surface = FONT.render("Welcome to Mini Phone", True, BLACK)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(title_surface, title_rect)

        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for project, x, y in buttons:
            is_hovered = x <= mouse_pos[0] <= x + BUTTON_WIDTH and y <= mouse_pos[1] <= y + BUTTON_HEIGHT
            draw_button(screen, project, x, y, BUTTON_WIDTH, BUTTON_HEIGHT, GRAY, DARK_GRAY, is_hovered)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                for project, x, y in buttons:
                    if x <= mouse_pos[0] <= x + BUTTON_WIDTH and y <= mouse_pos[1] <= y + BUTTON_HEIGHT:
                        run_game(project)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()