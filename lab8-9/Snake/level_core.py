# Importing the level functions from their respective modules
from level1 import level_1
from level2 import level_2

# Initializing the score variable to 0
score = 0

# Executing each level function sequentially and updating the score
score = level_1(score)  # Execute level 1 and update the score
score = level_2(score)  # Execute level 2 and update the score