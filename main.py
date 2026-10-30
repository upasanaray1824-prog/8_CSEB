"""
Smart Calculation Utility
Main menu for the reusable calculation package.
"""

from utility_package import (
    add, subtract, multiply, divide, percentage,
    square_root, power, factorial, random_integer,
    square, get_calculation_count
)


def read_number(prompt):
    """Read a number from the user and handle invalid input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def read_integer(prompt):
    """Read a whole number from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def show_menu():
    """Display the available operations."""
    print("\n========== SMART CALCULATION UTILITY ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage (default: 10%)")
    print("6. Square root")
    print("7. Power (default: square)")
    print("8. Factorial")
    print("9. Random integer")
    print("10. Square using lambda function")
    print("11. Show successful calculation count")
    print("0. Exit")
    print("================================================")


def main():
    # Local variable: it exists only inside main().
    running = True

    while running:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice in ("1", "2", "3", "4"):
                first = read_number("Enter the first number: ")
                second = read_number("Enter the second number: ")

                if choice == "1":
                    result = add(first, second)
                elif choice == "2":
                    result = subtract(first, second)
                elif choice == "3":
                    result = multiply(first, second)
                else:
                    result = divide(first, second)

                print("Result:", result)

            elif choice == "5":
                number = read_number("Enter the number: ")
                percent_text = input(
                    "Enter percentage (press Enter for default 10%): "
                ).strip()

                if percent_text == "":
                    result = percentage(number)
                else:
                    result = percentage(number, float(percent_text))

                print("Result:", result)

            elif choice == "6":
                number = read_number("Enter a non-negative number: ")
                print("Result:", square_root(number))

            elif choice == "7":
                base = read_number("Enter the base: ")
                exponent_text = input(
                    "Enter exponent (press Enter for default 2): "
                ).strip()

                if exponent_text == "":
                    result = power(base)
                else:
                    result = power(base, float(exponent_text))

                print("Result:", result)

            elif choice == "8":
                number = read_integer("Enter a non-negative whole number: ")
                print("Result:", factorial(number))

            elif choice == "9":
                start = read_integer("Enter the starting integer: ")
                end = read_integer("Enter the ending integer: ")
                print("Random number:", random_integer(start, end))

            elif choice == "10":
                number = read_number("Enter a number: ")
                print("Square:", square(number))

            elif choice == "11":
                print("Successful calculations:", get_calculation_count())

            elif choice == "0":
                running = False
                print("Thank you for using Smart Calculation Utility!")

            else:
                print("Invalid menu choice. Please choose from 0 to 11.")

        except ValueError as error:
            print("Error:", error)
        except OverflowError:
            print("Error: the result is too large to calculate.")

if __name__ == "__main__":
    main()
