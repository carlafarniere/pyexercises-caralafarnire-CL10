"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: two values written in the code: a = "Python" and b = "python".
# 2. Process: the program compares a and b with the 6 comparison operators
#    (==, !=, <, >, <=, >=), then combines two of the results with and, or, not.
# 3. Out: a table on screen, one line per operation, with its result True or False.
# 4. My two values, and the result that surprised me:
#    "Python" and "python": the same word, only the capital letter changes.
#    Surprise: a < b is True. Python compares letters by their code, and capital
#    letters come before small letters, so "P" is "smaller" than "p".
#    My predictions: 7 right out of 9.

# Your code below

a = "Python"
b = "python"

# The 6 comparisons, stored as (label, result) so I can print them in a loop
comparisons = [
    ("a == b", a == b),
    ("a != b", a != b),
    ("a < b", a < b),
    ("a > b", a > b),
    ("a <= b", a <= b),
    ("a >= b", a >= b),
]

# The logical combinations of two results: are they equal, and is a smaller?
logic = [
    ("(a == b) and (a < b)", (a == b) and (a < b)),
    ("(a == b) or (a < b)", (a == b) or (a < b)),
    ("not (a == b)", not (a == b)),
]

# Display everything as a readable table: the operation on the left, the result on the right
print("a =", repr(a), "| b =", repr(b))
print("-" * 32)
print(f"{'Operation':<24}{'Result'}")
print("-" * 32)
for label, result in comparisons + logic:
    print(f"{label:<24}{result}")


# Check it yourself: I predicted each result before running.
# Result when I ran it: ==, > and >= are False; !=, <, <= are True;
# and -> False, or -> True, not -> True.
# I got 7 out of 9 right. I was wrong on a > b (I said True, but "Python" comes before "python") and on or (I said False, but or only needs one True).
