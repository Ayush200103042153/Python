
import random

def display_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    user_input = input("Enter the number of your choice (1-4): ")
    return int(user_input)

def kbc_game():
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'London', 'Paris', 'Madrid'],
            'correct_answer': 3,
            'amount': 1000
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Venus'],
            'correct_answer': 2,
            'amount': 2000
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
            'correct_answer': 2,
            'amount': 5000
        },
         {
            'question': '7th Largest country in the world?',
            'options': ['India', 'Australia', 'Africa', 'Brazil'],
            'correct_answer': 1,
            'amount': 10000
        },
        # Add more questions as needed
    ]

    total_amount = 0

    for question_data in questions:
        current_question = question_data['question']
        current_options = question_data['options']
        correct_answer_index = question_data['correct_answer']
        amount = question_data['amount']

        user_choice = display_question(current_question, current_options)

        if user_choice == correct_answer_index:
            print("Correct!")
            total_amount += amount
        else:
            print(f"Sorry, the correct answer was {current_options[correct_answer_index - 1]}.")

        print(f"Current Total Amount: ${total_amount}\n")

    print(f"Congratulations! You have won ${total_amount}.")

if __name__ == "__main__":
    print("Welcome to the KBC Game!")
    kbc_game()


