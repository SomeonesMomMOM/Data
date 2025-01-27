import random


class Game:
    def __init__(self, required_correct_answers):
        self.required_correct_answers = required_correct_answers
        self.correct_answers = 0
        self.operations = ["+", "-", "*", "/"]

    def __str__(self):
        return f"You have answered {self.correct_answers} questions correctly out of {self.required_correct_answers}."

    def is_game_over(self):
        return self.correct_answers >= self.required_correct_answers

    def ask_result(self):
        """Asks the user to calculate the result of a random operation."""
        a, b, operation = self._generate_valid_question()
        if operation == "/":
            result = a // b
        elif operation == "*":
            result = a * b
        elif operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b

        print(f"What is {a} {operation} {b}?")
        user_input = input("Your answer: ")
        if user_input.isdigit() and int(user_input) == result:
            self.correct_answers += 1
            print("Correct!")
            return True
        else:
            print(f"Wrong. The correct answer was {result}.")
            return False

    def ask_operation(self):
        """Asks the user to identify the missing operation in a random calculation."""
        a, b, operation = self._generate_valid_question()
        if operation == "/":
            result = a // b
        elif operation == "*":
            result = a * b
        elif operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b

        print(f"What operation makes {a} ? {b} = {result}?")
        user_input = input("Your answer (+, -, *, /): ")
        if user_input == operation:
            self.correct_answers += 1
            print("Correct!")
            return True
        else:
            print(f"Wrong. The correct operation was {operation}.")
            return False

    def _generate_valid_question(self):
        """Generates a valid question with positive integers and valid division."""
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operation = random.choice(self.operations)

        # Ensure division is valid
        while operation == "/" and (a % b != 0 or b == 0):
            a = random.randint(1, 100)
            b = random.randint(1, 100)

        # Ensure subtraction doesn't go negative
        while operation == "-" and a < b:
            a = random.randint(1, 100)
            b = random.randint(1, 100)

        return a, b, operation
