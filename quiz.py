# * Python Quiz Project
import re
# Question List
questions = ("What is the capital of France?", 
            "What is the capital of Japan?", 
            "What is the capital of Spain?", 
            "What is the capital of United State of America?", 
            "What is the capital of Germany?")

# Choices
choices = (("A: Lyon", "B: Paris", "C: Nice", "D: Marseille"),
            ("A: Tokyo", "B: Osaka", "C: Hokkaido", "D: Kyoto"), 
            ("A: Barcelona", "B: Madrid", "C: Seville", "D: Valencia"), 
            ("A: New York", "B: Los Angeles", "C: Chicago", "D: Washington, D.C."),
            ("A: Hamburg", "B: Frankfurt", "C: Berlin", "D: Munich"))

# Answer
answers = ("B", "A", "B", "D", "C")
# Guess
guesses = []

#Quiz Function
def quiz():
    score = 0
    question_num = 0
    for question in questions:
        print("--------------------------")
        print(question)
        for choice in choices[question_num]:
            print(choice)

        try:
            guess = input("\nEnter Your Answer [A], [B], [C], [D]: ").upper()
            if not re.match('[A-D]', guess):
                print("Incorrect Input. Try Again.")
            else:
                guesses.append(guess)
                if guess == answers[question_num]:
                    score += 1
                    print(f"{guess} is CORRECT!")
                else:
                    print(f"{guess} is INCORRECT!")
                    print(f"{answers[question_num]} is the correct answer.")
        except Exception as e:
            print(f"An error occurred: {e}")
        question_num += 1
    print(f"Results: {score}")

# Start Application
print("\nWelcome To A Simple Quiz Application!!!\n")
quiz()
print("\nThank You For Taking The Quiz!!!")