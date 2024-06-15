import random
import time
import pygame
import sys

def generate_number(limit):
    num1 = random.randint(1, limit)
    num2 = random.randint(1, limit)
    return num1, num2

def play_game(screen, font, time_limit, level):
    num1, num2 = generate_number(level * 10)
    question = f"{num1} + {num2}"
    correct_answer = num1 + num2
    input_answer = ''
    start_time = time.time()
    
    while True:
        screen.fill((255, 255, 255))
        
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            display_message(screen, font, "Time's Up! You lose!", (255, 0, 0))
            pygame.display.flip()
            pygame.time.wait(2000)
            return False
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_answer.isdigit() and int(input_answer) == correct_answer:
                        display_message(screen, font, "Correct!", (0, 255, 0))
                        pygame.display.flip()
                        pygame.time.wait(1000)
                        return True
                    else:
                        display_message(screen, font, f"Incorrect! The correct answer is {correct_answer}", (255, 0, 0))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        return False
                elif event.key == pygame.K_BACKSPACE:
                    input_answer = input_answer[:-1]
                elif event.unicode.isdigit():
                    input_answer += event.unicode
        
        render_game(screen, font, question, input_answer, time_limit - int(elapsed_time), level)
        pygame.display.flip()

def display_message(screen, font, message, color):
    text = font.render(message, True, color)
    rect = text.get_rect(center=(400, 300))
    screen.blit(text, rect)

def render_game(screen, font, question, input_answer, time_left, level):
    question_text = font.render(f"Add the following numbers: {question}", True, (0, 0, 0))
    screen.blit(question_text, (50, 150))
    
    input_text = font.render(f"Your answer: {input_answer}", True, (0, 0, 0))
    screen.blit(input_text, (50, 250))
    
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(level_text, (50, 50))
    
    time_text = font.render(f"Time left: {time_left}s", True, (255, 0, 0) if time_left < 5 else (0, 0, 0))
    screen.blit(time_text, (50, 100))

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('SUM GAME')
    font = pygame.font.Font(None, 36)
    
    while True:
        level = 1
        time_limit = 30

        screen.fill((255, 255, 255))
        render_welcome_screen(screen, font)
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False

        while True:
            if play_game(screen, font, time_limit, level):
                if level == 5:
                    display_message(screen, font, "Congratulations! You've completed all levels!", (0, 255, 0))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    break
                level += 1
                time_limit -= 5
                display_message(screen, font, f"Level up! Now Level {level} with {time_limit}s time limit.", (0, 0, 255))
                pygame.display.flip()
                pygame.time.wait(2000)
            else:
                display_message(screen, font, "Game Over! Try again.", (255, 0, 0))
                pygame.display.flip()
                pygame.time.wait(3000)
                break

        screen.fill((255, 255, 255))
        display_message(screen, font, "Do you want to play again? (Y/N)", (0, 0, 0))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting = False
                    if event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()

def render_welcome_screen(screen, font):
    lines = [
        "Welcome to SUM GAME!",
        "======================",
        "Rules:",
        "1. Solve the addition problem displayed on the screen.",
        "2. You have a limited time to enter the correct sum.",
        "3. If you answer correctly within the time limit, you advance to the next level.",
        "4. The time limit decreases with each level, and the numbers get larger.",
        "5. Complete all 5 levels to win the game!",
        "6. If you answer incorrectly or run out of time, the game is over.",
        "Press 'Enter' to start the game."
    ]
    y_offset = 50
    for line in lines:
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (50, y_offset))
        y_offset += 40

if __name__ == "__main__":
    main()
