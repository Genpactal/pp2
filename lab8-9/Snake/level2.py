import pygame, sys
from main import Snake  # Importing the Snake class from the snake

pygame.init()  # Initialize Pygame

def level_2(score):

    window = pygame.display.set_mode((850, 600))  # Creating the game window

    clock = pygame.time.Clock()  # Creating a Pygame clock to control frame rate
    fps = 10  # Frames per second

    font = pygame.font.Font(None, 36)  # Creating a font object for displaying text
    text = font.render("level2", True, (255, 255, 255))  # Rendering text for display

    apple = (20, 18)  # Initial position of the apple

    walls = [(15, 10), (15, 11), (16, 10), (16, 11)] # Coordinates of wall blocks

    snake = Snake([(6, 4), (5, 4)], walls)  # Creating a Snake object with initial positions and walls

    fruit = 1  # Indicator for different types of fruits

    direct = 0  # Initial direction of the snake
    fail = False  # Flag to indicate if the game is over

    # Main game loop
    while len(snake.pos) < 6:  # Continue until the snake's length reaches 6
        for e in pygame.event.get():  # Handling Pygame events
            if e.type == pygame.QUIT:  # If the user quits the game
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:  # If a key is pressed
                # Change the direction of the snake based on the key pressed
                if e.key == pygame.K_UP and direct != 1:
                    direct = 3
                elif e.key == pygame.K_DOWN and direct != 3:
                    direct = 1
                elif e.key == pygame.K_LEFT and direct != 0:
                    direct = 2
                elif e.key == pygame.K_RIGHT and direct != 2:
                    direct = 0

        # Update apple position, score, and fruit type after the snake eats the apple
        apple, score, fruit = snake.eat(apple, score, fruit)

        # Determine color of the apple based on its type
        if fruit == 1:
            color = (255, 0, 0)
        elif fruit == 2:
            color = (255, 255, 0)
        else:
            color = (0, 0, 255)

        score_text = font.render("score: " + str(score), True, (255, 255, 255))  # Render score text

        # Move the snake and check for collision
        fail = snake.move(direct)
        while fail:  # If the snake collides with itself
            for e in pygame.event.get():  # Wait for the user to quit the game
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        # Update the display
        window.fill((0, 0, 128))

        pygame.draw.rect(window, color, (25*apple[0], 25*apple[1], 25, 25))  # Draw the apple

        for i in walls:  # Draw the walls
            pygame.draw.rect(window, (122, 122, 122), (25*i[0], 25*i[1], 25, 25))

        snake.draw(window)  # Draw the snake

        window.blit(text, (750, 15))  # Display level text
        window.blit(score_text, (15, 15))  # Display score

        pygame.display.flip()  # Update the display
        
        clock.tick(fps)  # Control frame rate
    
    return score  # Return the final score