def Numeric_Letter_Grade():
        
    while True:
        try:
            # Prompt the user to enter their marks
            marks_input = input("Please enter your marks (0-100): ")

            # Attempt to convert the input to a float
            marks = float(marks_input)

            # Validate if the marks are within the allowed range (0 to 100)
            if 0 <= marks <= 100:
                if marks >= 90:
                    print(f"With marks {marks} you have an A grade")
                elif 85<= marks <90:
                        print(f"With marks {marks} you have a B+ grade")
                elif 80<= marks <85:
                        print(f"With makrs {marks} you have a B grade")
                elif  75<= marks <80:
                        print(f"With the marks {marks} you have a B- grade")
                elif 70<= marks <70:
                        print(f" with the marks {marks} you have a C- grade")
                elif 65 <= marks < 70:
                        print(f"With the marks {marks} you have a C grade")
                elif 60<= marks <65:
                        print(f"With the markds {marks} you have a C- grade")
                else:
                    print(f"With the marks {marks} you have a D grade")
                break 
            else:
                print("Marks must be between 0 and 100. Please try again.")

        except ValueError:
            # Handle cases where the input cannot be converted to a float (e.g., non-numeric strings)
            print("Invalid input. Please enter a numerical value for your marks (e.g., 75, 88.5).")
        except Exception as e:
            # Catch any other unexpected errors (less common for simple input)
            print(f"An unexpected error occurred: {e}")

Numeric_Letter_Grade()