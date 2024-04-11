import pygame
import random

class Snake:
    def __init__(self, pos, walls):
        # Initialize the snake with its initial position and the walls
        self.pos = pos  # Snake's positions
        self.possible_possition = [(i, j) for i in range(34) for j in range(24)]  # All possible positions on the game board
        self.possible_possition.append((-1, -1))  # Add a special position to indicate a segment of the snake that has been removed
        self.time = 0  # Time counter
        
        # Remove initial positions and wall positions from the list of possible positions
        for i in pos:
            self.possible_possition.remove(i)
        for i in walls:
            self.possible_possition.remove(i)

    def move(self, direct):
        # Move the snake in the given direction
        if direct == 0:
            self.pos.insert(0, (self.pos[0][0]+1, self.pos[0][1]))  # Move right
        elif direct == 1:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]+1))  # Move down
        elif direct == 2:
            self.pos.insert(0, (self.pos[0][0]-1, self.pos[0][1]))  # Move left
        else:
            self.pos.insert(0, (self.pos[0][0], self.pos[0][1]-1))  # Move up
        try:
            self.possible_possition.remove(self.pos[0])  # Remove the new head position from the list of possible positions
        except:
            return True  # If collision occurs, return True
        self.possible_possition.append(self.pos[-1])  # Add the old tail position back to the list of possible positions
        self.pos.pop()  # Remove the old tail position

    def eat(self, a, s, t):
        # Function to handle eating an apple
        self.time += 1  # Increment time counter
        if self.pos[0][0] == a[0] and self.pos[0][1] == a[1] or self.time > 30:  # If the snake eats the apple or time exceeds 30 moves
            self.possible_possition.remove((-1, -1))  # Remove the special position from possible positions
            a = random.choice(self.possible_possition)  # Choose a new random position for the apple
            if self.time > 30:  # If time exceeds 30 moves
                self.possible_possition.append((-1, -1))  # Add the special position back to possible positions
            else:
                self.pos.append((-1, -1))  # Add a new segment to the snake
                s += t  # Increase score
            self.time = 0  # Reset time counter
            t = random.randint(1, 3)  # Generate a new random fruit type
        return a, s, t  # Return the new apple position, score, and fruit type

    def draw(self, window):
        # Draw the snake on the game window
        for i in range(len(self.pos)):
            pygame.draw.rect(window, (0, 255, 0), (self.pos[i][0]*25, self.pos[i][1]*25, 25, 25))  # Draw each segment of the snake