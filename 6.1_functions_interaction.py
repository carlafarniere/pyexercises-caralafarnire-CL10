"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a whole number (here I test 4, -3 and 0).
# 2. Process, function by function:
#    - is_zero checks if the number is 0.
#    - is_even checks if the number divides by 2 with no remainder.
#    - is_positive checks if the number is bigger than 0.
#    - describe_number calls the three functions above, in that order, to build one sentence.
# 3. Out: a sentence printed on screen, e.g. "4 is positive and even."
# 4. The question my fourth function answers: "What kind of number is this?"
#    Splitting it into three makes it easier to check, because I can test each small
#    function alone: if the final sentence is wrong, I know which function to look at.
 
 
# Your code below
 
# Tells me if the number is zero (True or False)
def is_zero(num):
    return num == 0
 
# Tells me if the number is even: the remainder of a division by 2 is 0
def is_even(num):
    return num % 2 == 0
 
# Tells me if the number is above zero
def is_positive(num):
    return num > 0
 
# Uses the three functions above to describe the number in one sentence
def describe_number(num):
    # Zero is a special case: it is neither positive nor negative
    if is_zero(num):
        return f"{num} is zero."
    # Otherwise I choose the sign first, then the parity
    if is_positive(num):
        sign = "positive"
    else:
        sign = "negative"
    if is_even(num):
        parity = "even"
    else:
        parity = "odd"
    return f"{num} is {sign} and {parity}."
 
 
# My three tests, one per small function (input -> expected output)
# is_zero(0)      -> True
# is_even(4)      -> True
# is_positive(-3) -> False
print(is_zero(0))
print(is_even(4))
print(is_positive(-3))
 
# The final result, on three numbers where I already know the answer
for number in [4, -3, 0]:
    print(describe_number(number))
# Expected: "4 is positive and even." / "-3 is negative and odd." / "0 is zero."
# Result when I ran it: True, True, False, then exactly the three expected sentences. Test OK.
