# 🎮 Python Number Guessing Game

A fun and interactive **Number Guessing Game built with Python**. The computer randomly generates a secret number, and the player tries to guess it using helpful hints.

This project combines Python fundamentals such as loops, conditional statements, random number generation, and user input in a simple command-line game.

## ✨ Features

- 🎯 Three difficulty levels: Easy, Medium, and Hard
- 🎲 Random number generation
- 💡 Smart hints: Too High, Too Low, and Very Close
- 🏆 Score tracking based on the number of attempts
- 🔄 Option to play multiple rounds
- 🚪 Option to exit the game
- 🐍 Beginner-friendly Python code

## 🕹️ Difficulty Levels

| Level | Difficulty | Number Range |
|---|---|---|
| 1 | Easy | 1–50 |
| 2 | Medium | 1–100 or 1–200 |
| 3 | Hard | 1–500 |

*Note: The Medium level range depends on which version of the game you run.*

## 💡 How the Game Works

1. The computer randomly selects a secret number.
2. The player chooses a difficulty level.
3. The player enters a guessed number.
4. The game provides hints:
   - **Too Low:** Your guess is smaller than the secret number.
   - **Too High:** Your guess is greater than the secret number.
   - **Very Close:** Your guess is within 5 of the secret number.
5. The player continues guessing until the correct number is found.
6. The game displays a success message and, in the score-enabled version, the number of attempts.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Module:** `random`
- **Concepts:** Variables, loops, conditional statements, user input, `abs()`, and score calculation

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd <your-project-folder>
```

### 3. Run the Game

```bash
python main.py
```

No external libraries are required.

## 📂 Project Structure

```text
Number-Guessing-Game/
│
├── main.py
└── README.md
```

## 📚 Learning Objectives

This project helped me practice:

- Generating random numbers using Python
- Using `while` loops for repeated gameplay
- Applying `if-elif-else` conditions
- Handling user input and displaying output
- Comparing numbers and calculating differences
- Implementing basic scoring logic

## 🔮 Future Improvements

- Add input validation for invalid choices.
- Introduce a maximum number of attempts.
- Add a high-score leaderboard.
- Include difficulty-based scoring.
- Develop a graphical user interface (GUI).

## 👨‍💻 Author

**Abhronil Jash**

---

⭐ If you like this project, consider giving the repository a star!

