import random
print("=" * 50)
print("🎮 Welcome to Hangman Game 🎮")
print("=" * 50)
words = [
    "python",
    "computer",
    "programming",
    "developer",
    "internship",
    "github",
    "flask",
    "coding",
    "project",
    "automation"
]
word = random.choice(words)
guessed_letters = []
attempts = 6
print("\nGuess the word one letter at a time!")
while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").strip().lower()
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("❤️ Attempts Left:", attempts)
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
print("\n🎮 Thanks for Playing Hangman!")