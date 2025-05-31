def pass_fail():
    """
    Accepts user input for marks, validates it, and prints it if the user
    has passed or failed based on a 60% threshold.
    """
    while True:
        try:
            # Prompt the user to enter their marks
            marks_input = input("Please enter your marks (0-100): ")

            # Attempt to convert the input to a float
            marks = float(marks_input)

            # Validate if the marks are within the allowed range (0 to 100)
            if 0 <= marks <= 100:
                if marks >= 60:
                    print(f"Congratulations! With {marks}%, you have PASSED.")
                else:
                    print(f"Unfortunately, with {marks}%, you have FAILED.")
                break 
            else:
                print("Marks must be between 0 and 100. Please try again.")

        except ValueError:
            # Handle cases where the input cannot be converted to a float (e.g., non-numeric strings)
            print("Invalid input. Please enter a numerical value for your marks (e.g., 75, 88.5).")
        except Exception as e:
            # Catch any other unexpected errors (less common for simple input)
            print(f"An unexpected error occurred: {e}")


pass_fail()
