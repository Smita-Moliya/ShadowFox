import random

words_with_hints = {
    "python": "A popular programming language.",
    "elephant": "The largest land animal.",
    "guitar": "A string musical instrument.",
    "astronaut": "A person trained for space travel.",
    "pizza": "An Italian dish loved by many."
}

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    """
]

word, hint = random.choice(list(words_with_hints.items()))
guessed = ["_"] * len(word)
used_letters = []
lives = len(hangman_stages) - 1

print("🕹️ Welcome to Hangman!")
print("Hint:", hint)

while lives > 0 and "_" in guessed:
    print("\n" + hangman_stages[len(hangman_stages) - 1 - lives])
    print("Word:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid single letter.")
        continue

    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
        print("✅ Correct guess!")
    else:
        lives -= 1
        print("❌ Wrong guess! Lives left:", lives)

if "_" not in guessed:
    print("\n🎉 You guessed the word:", word)
else:
    print("\n" + hangman_stages[-1])
    print("💀 Game Over! The word was:", word)
