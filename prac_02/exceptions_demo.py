
"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator <= 0:
            print("Denominator cannot = 0")
        else:
            valid_input = True
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Finished.")

# 1: If numerator or denominator are decimals or letters (not integers).
# 2: If the denominator is zero.
# 3: Start with condition then use while and for loops.