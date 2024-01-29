import sys

def ask_question(question, correct_answer):
    print(question)
    user_answer = input("Your answer: ").strip().lower()
    return user_answer == correct_answer.strip().lower()

def run_quiz(questions):
    score = 0
    for question, correct_answer in questions:
        if ask_question(question, correct_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {correct_answer}\n")
    return score

def main():
    # Questions format: ("Question", "Correct Answer")
    questions = [
        ("What is the capital of France?", "Paris"),
        ("Who wrote 'To be or not to be'?", "William Shakespeare"),
        # More questions can be added here.
    ]

    total_questions = len(questions)
    score = run_quiz(questions)

    print(f"Quiz complete! You scored {score} out of {total_questions}.")

if __name__ == "__main__":
    main()
