from game import Game


def main():
    print("Welcome to the Math Game!")
    required_correct_answers = int(input("Enter the number of correct answers to win: "))
    game = Game(required_correct_answers)

    while not game.is_game_over():
        print(game)
        choice = input("\nWould you like to (1) solve a calculation or (2) guess the operation? Enter 1 or 2: ")
        if choice == "1":
            game.ask_result()
        elif choice == "2":
            game.ask_operation()
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print(f"\nCongratulations! You answered {game.correct_answers} questions correctly. You win!")


if __name__ == "__main__":
    main()
