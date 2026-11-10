"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of 8 monthly advertising budgets (in euros), written in the code.
# 2. Process: Python displays the list, picks one item, sorts the list,
#    and computes the total, the average and the highest budget.
# 3. Out: the whole list, one budget, the sorted list, the total, the average and the max.
# 4. What my list is about, and what I computed from it:
#    my list is the advertising budget of a brand from January to August.
#    I computed the total, the average and the max: the total shows how much
#    was spent, the average helps plan next month, the max shows the most expensive month.


# Your code below
# My list: advertising budget per month, from January to August (in euros)
budgets = [1200, 950, 1500, 800, 1300, 1100, 700, 1450]
print("The whole list is : ", budgets)

# One item of my choice: March is the third item, so index 2 (Python counts from 0)
print("The budget in March is : ", budgets[2])

# The list sorted from the smallest to the largest budget
sorted_budgets = sorted(budgets)
print("The sorted list is : ", sorted_budgets)

# Something computed from the list: total, average and highest budget
total = sum(budgets)
average = total / len(budgets)
print("The total budget is : ", total)
print("The average budget per month is : ", average)
print("The highest budget is : ", max(budgets))

# Check on three items: January, February and March
first_three = budgets[0] + budgets[1] + budgets[2]
print("The total of the first three months is : ", first_three)

# Check:
# - By hand: 1200 + 950 + 1500 = 3650. The program shows 3650, it agrees.
# - By hand, the highest of these three is 1500. The program's max is 1500, it agrees.