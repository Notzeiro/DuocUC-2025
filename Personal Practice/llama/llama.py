import pygame
import sys

# Initialize Pygame
pygame.init()

# --- Game Constants ---
# Set the width and height of the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Llama")

# Define some colors
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# --- Game World Size ---
WORLD_WIDTH = 2000
WORLD_HEIGHT = 1500
game_world_surface = pygame.Surface((WORLD_WIDTH, WORLD_HEIGHT))
game_world_surface.fill(GREEN)  # This is your big green background

# --- Camera Class ---
class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, target):
        """
        Updates the camera's position to follow a target (e.g., the player).
        """
        self.x = target.x - SCREEN_WIDTH // 2
        self.y = target.y - SCREEN_HEIGHT // 2

        # Keep the camera within the game world boundaries
        self.x = max(0, self.x)
        self.y = max(0, self.y)
        self.x = min(WORLD_WIDTH - SCREEN_WIDTH, self.x)
        self.y = min(WORLD_HEIGHT - SCREEN_HEIGHT, self.y)

# --- Character Class ---
class Character:
    """
    Represents a character with health, damage, etc., and can be drawn on screen.
    Now includes animation and sprite handling.
    """
    def __init__(self, name, health, damage, speed, mana, armor, x, y, image_paths):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed
        self.mana = mana
        self.armor = armor
        
        # Dictionary to hold images for different directions
        self.images = {}
        self.current_image = None
        self.facing = 'down'  # Default facing direction

        # Load images for each direction
        for direction, path in image_paths.items():
            try:
                self.images[direction] = pygame.image.load(path).convert_alpha()
            except pygame.error as e:
                print(f"Error loading image: {e}. Using a default square instead.")
                self.images[direction] = pygame.Surface((50, 50))
                self.images[direction].fill(BLUE)
        
        # Set the initial image and rectangle
        self.current_image = self.images[self.facing]
        self.rect = self.current_image.get_rect(x=x, y=y)

    def attack(self, target):
        # Your attack logic here...
        pass
    
    def move(self, dx, dy):
        """
        Moves the character and updates the facing direction.
        """
        # Update facing direction based on movement
        if dx > 0:
            self.facing = 'right'
        elif dx < 0:
            self.facing = 'left'
        elif dy > 0:
            self.facing = 'down'
        elif dy < 0:
            self.facing = 'up'

        # Update the current image to reflect the new direction
        self.current_image = self.images[self.facing]
        
        # Move the rectangle
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
        # Clamp to world boundaries
        self.rect.x = max(0, min(WORLD_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(WORLD_HEIGHT - self.rect.height, self.rect.y))
        
    def draw(self, surface, camera):
        """
        Draws the character's image on the screen, adjusted by the camera's position.
        """
        # Calculate the character's position relative to the camera
        draw_x = self.rect.x - camera.x
        draw_y = self.rect.y - camera.y

        # Blit the image instead of drawing a rectangle
        surface.blit(self.current_image, (draw_x, draw_y))

# --- Game Objects ---
# Paths to your character image files
# Note: The 'images/' prefix tells the program to look in that folder.
PLAYER_IMAGE_PATHS = {
    'down': "images/player_down.png",
    'up': "images/player_up.png",
    'left': "images/player_left.png",
    'right': "images/player_right.png",
}

player = Character("Player", 100, 25, 5, 10, 10, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_IMAGE_PATHS)
camera = Camera(0, 0)

# --- Main Game Loop ---
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Player movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1
        
        # Normalize movement speed for diagonal movement
        if dx != 0 and dy != 0:
            dx /= 1.414
            dy /= 1.414
        
        player.move(dx, dy)
        
        # Update the camera position to follow the player
        camera.update(player.rect)

        # --- Drawing ---
        screen.fill((0, 0, 0))
        screen.blit(game_world_surface, (0, 0), (camera.x, camera.y, SCREEN_WIDTH, SCREEN_HEIGHT))
        player.draw(screen, camera)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
