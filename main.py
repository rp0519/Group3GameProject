import random

# Import question sets from different files
from categories.python_syntax import questions_and_answers as python_syntax_qa
from categories.functions_methods import questions_and_answers as functions_methods_qa
from categories.sets_lists_dictionaries import questions_and_answers as sets_lists_dicts_qa
from categories.file_io import questions_and_answers as file_io_qa
from categories.modules import questions_and_answers as modules_qa
from leaderboard import load_leaderboard, add_to_leaderboard, display_leaderboard

# Map category names to their respective question sets
category_map = {
    "Python Syntax": python_syntax_qa,
    "Functions and Methods": functions_methods_qa,
    "Sets, Lists, and Dictionaries": sets_lists_dicts_qa,
    "File I/O": file_io_qa,
    "Modules": modules_qa
}

# Initialize a copy of questions so we can remove questions after asking
remaining_questions = {category: {d: dict(questions) for d, questions in difficulties.items()}
                       for category, difficulties in category_map.items()}

# Initialize leaderboard
load_leaderboard()

# Function to prompt the user to select a category
def get_category():
    categories = list(remaining_questions.keys())  # List of available categories
    print("\nSelect a Category:")
    for i, category in enumerate(categories, 1):  # Display categories to the user
        print(f"{i}. {category}")
    choice = int(input("Enter the number of the category: ")) - 1  # User selects a category by number
    return categories[choice]  # Return the chosen category



# Function to prompt the user to select a difficulty level (1-4)
def get_difficulty(category):
    available_difficulties = [d for d in remaining_questions[category] if remaining_questions[category][d]]
    if not available_difficulties:
        print("\nNo more questions available in this category.")
        return None

    print("\nSelect a Difficulty (1 = Easy, 4 = Hard):")
    for diff in available_difficulties:
        print(f"{diff}")
    difficulty = int(input("Enter difficulty level (1-4): "))

    if difficulty not in available_difficulties:
        print("Invalid difficulty or no questions available at this difficulty.")
        return None
    return difficulty  # Return the chosen difficulty


# Function to ask a random question from the selected category and difficulty level
def ask_question(category, difficulty):
    questions = remaining_questions[category][difficulty]  # Fetch remaining questions
    if not questions:
        print("No questions left in this difficulty.")
        return 0

    question, answer = random.choice(list(questions.items()))  # Pick a random question
    print(f"\nQuestion: {question}")  # Display the question
    user_answer = input("Your answer: ")  # Get the user's answer

    # Remove the asked question from the remaining pool
    del remaining_questions[category][difficulty][question]

    # Check if the user's answer is correct (ignoring case)
    if user_answer.lower() == answer.lower():
        points = difficulty * 100  # Assign points based on difficulty (100 points per level)
        print(f"Correct! You earned {points} points.")
        return points  # Return the points earned for a correct answer
    else:
        print(f"Wrong! The correct answer was: {answer}")
        return 0  # Return 0 points if the answer is incorrect


# Main function to run the quiz game
def main():
    print("Welcome to Python Jeopardy!")  # Display welcome message
    total_score = 0  # Initialize the total score to 0
    userName = input("Enter your name: ") # Ask for name


    # Game loop to allow the user to play multiple rounds
    while True:
        category = get_category()  # Get the category selected by the user
        difficulty = get_difficulty(category)  # Get the difficulty level selected by the user

        if difficulty is None:
            print("\nNo valid difficulty or questions available.")
            continue

        total_score += ask_question(category, difficulty)  # Ask a question and update the total score

        # Check if there are any remaining questions in all categories
        if all(not remaining_questions[cat][diff] for cat in remaining_questions for diff in remaining_questions[cat]):
            print("\nAll questions have been answered! The game is over.")
            break


        # Prompt the user to continue or quit
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':  # Exit loop if user does not want to play again
            break

    print(f"\nYour total score: {total_score}")  # Display the user's total score
    add_to_leaderboard(userName,total_score)
    display_leaderboard()
# Check if this file is being run as the main program
if __name__ == "__main__":
    main()  # Run the game
