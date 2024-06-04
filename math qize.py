import random
import time

def generate_number(limit):
    num1 = random.randint(1, limit)
    num2 = random.randint(1, limit)
    return num1, num2

def play_game(time_limit, level):
    num1, num2 = generate_number(level * 10)
    print("\nAdd the following two numbers: ")
    print(f"{num1} + {num2}")

    start_time = time.time()
    user_input = input('Enter the Sum: ')

    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        return False

    if time.time() - start_time > time_limit:
        print("Time's Up! You lose!")
        return False

    if int(user_input) == num1 + num2:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct number is: {num1 + num2}")
        return False

def main():
    level = 1
    time_limit = 30

    print("Welcome to SUM GAME!")
    print("======================")
    print("Rules:")
    print("1. Solve the addition problem displayed on the screen.")
    print("2. You have a limited time to enter the correct sum.")
    print("3. If you answer correctly within the time limit, you advance to the next level.")
    print("4. The time limit decreases with each level, and the numbers get larger.")
    print("5. Complete all 5 levels to win the game!")
    print("6. If you answer incorrectly or run out of time, the game is over.")
    input("\nPress 'Enter' to start the game.")

    while True:
        print(f"\nYour Level is {level}")
        if play_game(time_limit, level):
            if level == 5:
                print("Congratulations! You've completed all levels!")
                break
            level += 1
            time_limit -= 5
            print(f"You've advanced to the next level with a time limit of {time_limit} seconds.")
        else:
            print("Game is over! Try again.")
            break

if __name__ == "__main__":
    main()
