def quiz_game():
    print("Welcome to the Python Quiz Game!")
    print("Answer the following questions with 'True' or 'False'.")

    questions = {
        "Python is a programming language.": True,
        "The Earth is flat.": False,
        "2 + 2 equals 4.": True,
        "Cats are reptiles.": False,
    }

    score = 0

    for question, correct_answer in questions.items():
        user_answer = input(f"{question} (True/False): ").capitalize()
        if user_answer == str(correct_answer):
            print("Correct!")
            score += 1
        else:
            print("Oops! That's incorrect.")
    
    print(f"\nGame Over! Your final score is: {score}/{len(questions)}")

quiz_game()
