# SUM GAME

## Project Description

The SUM GAME is an interactive mathematical puzzle game where players solve addition problems within a given time limit. The game progresses through multiple levels, each increasing in difficulty by presenting larger numbers and reducing the time limit. Players must solve the problem correctly and within the time limit to advance to the next level. Completing all five levels wins the game.

## Features

1. **Random Number Generation**
   - Generates two random numbers to be added together.
   - Numbers increase in size with each level.

2. **User Input and Validation**
   - Accepts user input for the sum of the two numbers.
   - Validates the input to ensure it is a number.
   - Checks if the input is correct and within the time limit.

3. **Scoring System**
   - Tracks the player's current level.
   - Decreases the time limit with each level.

4. **Game Over and Restart**
   - Ends the game if the player runs out of time or answers incorrectly.
   - Provides an option for the player to restart the game after it ends.

5. **Graphical Interface with Pygame**
   - Uses Pygame to create a graphical interface for the game.
   - Displays numbers, user input, time left, and game status on the screen.
   - Handles user input through keyboard events.
   - Provides visual feedback for correct/incorrect answers and game status.

## Installation

### Prerequisites

- Python 3.x
- Pygame library

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/Stanford-Python-CS106A.git
   cd math\qize
