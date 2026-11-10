"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of 8 monthly advertising budgets from exercise 4.0.
# 2. Process: Python displays the list in four orders, using only methods
#    that create a new list, so the original list stays the same.
# 3. Out: the four orders, then the original list again on the last line.
# 4. My four orders, and which ones modify the original:
#    - original order (January to August)
#    - from the smallest to the largest budget, with sorted()
#    - from the largest to the smallest budget, with sorted(reverse=True)
#    - from August back to January, with [::-1]
#    None of them modifies the original: sorted() and [::-1] return a new list.
#    budgets.sort() and budgets.reverse() would modify the original list
#    in place, so I did not use them.


# Your code below
# My list from exercise 4.0: advertising budget per month, January to August
budgets = [1200, 950, 1500, 800, 1300, 1100, 700, 1450]

# Order 1: the original order
print("Original order : ", budgets)

# Order 2: smallest to largest, sorted() creates a new list
print("Smallest to largest : ", sorted(budgets))

# Order 3: largest to smallest, sorted() with reverse=True also creates a new list
print("Largest to smallest : ", sorted(budgets, reverse=True))

# Order 4: from August back to January, [::-1] creates a reversed copy
print("August to January : ", budgets[::-1])

# Proof: the original list has not been damaged
print("The original list is still : ", budgets)

# Check:
# - Last line: [1200, 950, 1500, 800, 1300, 1100, 700, 1450].
# - Compared item by item with 4.0: same 8 budgets in the same order,
#   so the original list was not modified.