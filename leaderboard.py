import os

# Initialize leaderboard
leaderboard = []

# Load leaderboard from file
def load_leaderboard():
    if os.path.exists('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as file:
            for line in file:
                name, score = line.strip().split(',')
                leaderboard.append((name, int(score)))

# Save leaderboard to file
def save_leaderboard():
    with open('leaderboard.txt', 'w') as file:
        for name, score in leaderboard:
            file.write(f"{name},{score}\n")

def add_to_leaderboard(name, score):
    leaderboard.append((name, score))  # Store as a tuple (name, score)
    save_leaderboard()  # Save changes to file

def display_leaderboard():
    # Sort leaderboard by score in descending order
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x[1], reverse=True)
    print("Leaderboard:")
    for i, (name, score) in enumerate(sorted_leaderboard):
        print(f"{i + 1}. {name}: {score} points")

