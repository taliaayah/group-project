def main():  
    numbers = []  
  
    print("Enter 10 consecutive whole numbers:")  
  
    for i in range(10):  
        while True:  
            try:  
                num = int(input("Enter number " + str(i + 1) + ": "))  
                if i > 0 and num != numbers[i - 1] + 1:  
                    print("Number must be consecutive. Try again.")  
                    continue  
                numbers.append(num)  
                break  
            except ValueError:  
                print("Invalid input. Please enter a whole number.")  
  
    print("\nAll Numbers:")  
    print(numbers)  
  
    evens = [n for n in numbers if n % 2 == 0]  
    odds = [n for n in numbers if n % 2 != 0]  
  
    print("\nEven Numbers:")  
    print(evens)  
    print("Sum of Even Numbers:", sum(evens))  
  
    print("\nOdd Numbers:")  
    print(odds)  
    print("Sum of Odd Numbers:", sum(odds))  
  
if __name__ == "__main__":  
    main()  
