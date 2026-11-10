"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a whole number N typed by the user.
# 2. Process: Python converts N with int(), checks it is between 1 and 100,
#    then goes through every number from 1 to N and uses % 2 to test it.
# 3. Out: one line per number saying if it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#    - 0: a message "Please enter a number greater than 0", nothing else.
#    - negative (-4): the same message, because counting from 1 to -4 makes no sense.
#    - very large (5000): I refuse above 100, because 5000 lines are unreadable.


# Your code below
# Ask the user for a number and convert it into an integer
n = int(input("Enter a number: "))

# Refuse 0 and negative numbers
if n <= 0:
    print("Please enter a number greater than 0")
# Refuse numbers that are too large
elif n > 100:
    print("The number is too large, please enter 100 or less")
# For every number from 1 to n, say if it is odd or even
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")

# Check:
# - 6: 1, 3, 5 are odd and 2, 4, 6 are even: three odd, three even, as expected.
# - 0: "Please enter a number greater than 0", as decided.
# - -4: same message, as decided.
# - 5000: "The number is too large...", as decided.