"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two whole numbers typed by the user.
# 2. Process: Python converts them with int(), then computes the sum,
#    the difference, the product and the division.
# 3. Out: the two numbers and the result of the four operations.
# 4. What happens when the second number is zero, and why:
#    dividing by zero is impossible (Python crashes with ZeroDivisionError).
#    I chose to display a message instead of a result, so the user still
#    gets the sum, difference and product.


# Your code below
# Ask for two numbers and convert them into integers
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number:"))

# Display the two numbers
print("The first number is : ", number_1)
print("The second number is : ", number_2)

# Sum of two number
sum = number_1 + number_2
print("The sum of two numbers is: ", sum)

# Difference of two numbers
diff = number_1 - number_2
print("The diff of two numbers is: ", diff)

# produt of two numbers
product = number_1 * number_2
print("The product of two numbers is:", product)

# division of two numbers, only if the second number is not zero

if number_2 != 0:
    division = number_1 / number_2
    print("The division of two numbers is:", division)
else:
    print("The second number is zero")

# Check:
# - 7 and 2: in my head 7 / 2 = 3.5. The program shows 3.5, correct,
#   because / is the real division. With // it would show 3 (it keeps
#   only the whole part).
# - 7 and 0: sum 7, diff 7, product 0, then "The second number is zero",
#   no crash.