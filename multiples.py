"""
Name: Multiples
Author: Ross Simpson
Description: A program which accepts 3 numbers as input: two numbers (named x & y for this description)
and a boundary. The program will calculate the multiples of x and y (up to, and including, the number
set as a boundary) and then calculate the sum of these multiples.

Example:
x = 5, y = 3, boundary = 1000
Multiples of 5: 5, 10, 15, 20, 25 ... {to 1000}
Multiples of 3: 3, 6, 9, 12, 15 ... {to 1000}
Add all multiples of 5 and 3 together.
"""

def get_input():
    # Initialise variables.
    num1, num2, boundary = 0, 0, 0

    try:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))
        boundary = int(input("Enter the boundary: "))
    except ValueError as err:
        print("One (or more) entry (or entries) is/are not an integer. Enter an integer when asked for each number.")
        get_input()
    except Exception as err:
        print(f'Unexpected exception: ({err.__class__.__name__}), {err}')
        print("Please report error to program creator.")
    return num1, num2, boundary

def generate_all_multiples(num1, num2, boundary):
    # Define a 2D array. Each index[i][*] stores an array, while every 'secondary index' [*][i] has a value.
    # This currently only accepts 2 arrays.
    multiples = []
    #!! ACCEPT ARBITRARY NUMBER OF INPUTS
    multiples.append(generate_multiple_array(num1, boundary))
    multiples.append(generate_multiple_array(num2, boundary))
    return multiples

def generate_multiple_array(num1, boundary):
    # Initialise variables.
    multiple = []
    counter = 1

    # Calculate next multiple of num1. If less than boundary set by user, add it to array.
    while num1*counter <= boundary:
        multiple.append(num1*counter)
        counter += 1
    return multiple

def calculate_sum(multiples):
    sum = 0
    for list in multiples:
        for item in list:
            sum += item
    return sum

def main():
    num1, num2, boundary = get_input()
    multiples = generate_all_multiples(num1, num2, boundary)
    sum = calculate_sum(multiples)
    print("Multiples array:\n")
    print(multiples)
    print("Sum:\n ")
    print(sum)
    # Add_multiples

# Boiler-Plate. If this script is being run by itself (and not imported), __name__ will store '__main__'.
if __name__ == '__main__':
    main()
