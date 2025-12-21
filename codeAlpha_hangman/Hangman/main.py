
from game import Hangman

def main():
    print("===== HANGMAN GAME =====")
    print("Welcome to this game! Now start guessing your word")

    game = Hangman()

    print("🧩 Clue:", game.get_clue())

    while True:
        print("\nWord:", game.display_word())
        print(f"Wrong Attempts: {game.wrong_attempts} / {game.max_attempts}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter!")
            continue

        game.guess_letter(guess)

        if game.is_won():
            print("\n🎉 Congratulations! You guessed the word:", game.word)
            break

        if game.is_lost():
            print("\n❌ You lost! The word was:", game.word)
            break

if __name__ == "__main__":
    main()
