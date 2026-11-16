"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a list of monthly advertising budgets in euros (the list from my exercise 4.0).
# 2. Process: the function adds all the budgets of the list, then divides by the number
#    of months, to get the average budget per month.
# 3. Out: the function returns the average budget (a number), or None if the list is empty.
# 4. My function name, and why return rather than print:
#    It is called average_budget: the name says what it gives back without reading the code.
#    I use return and not print because print only shows the result on the screen and then
#    it is lost. With return, I get the value back in a variable, so I can reuse it:
#    round it, compare two periods, or give it to another function.
 
 
# Your code below
 
# My list from exercise 4.0: advertising budget per month, from January to August (in euros)
budgets = [1200, 950, 1500, 800, 1300, 1100, 700, 1450]
 
# Computes the average monthly budget of a list of budgets and gives it back
def average_budget(monthly_budgets):
    # An empty list has no average: dividing by 0 would crash the program
    if len(monthly_budgets) == 0:
        return None
    total = sum(monthly_budgets)
    return total / len(monthly_budgets)
 
 
# I call my function three times, on three different periods
average_all = average_budget(budgets)            # January to August
average_q1 = average_budget(budgets[0:3])        # January, February, March
average_summer = average_budget(budgets[5:8])    # June, July, August
 
# Because the function returns the value, I can round it before displaying it
print("Average budget, January to August:", round(average_all, 2))
print("Average budget, January to March:", round(average_q1, 2))
print("Average budget, June to August:", round(average_summer, 2))
 
# Check by hand:
# - January to March: (1200 + 950 + 1500) / 3 = 3650 / 3 = 1216.67
# - June to August: (1100 + 700 + 1450) / 3 = 3250 / 3 = 1083.33
# - January to August: 9000 / 8 = 1125.0
# Result when I ran it: 1125.0, 1216.67 and 1083.33. The program agrees.
 
 
# Check it yourself: the empty list
average_empty = average_budget([])
print("Average budget of an empty list:", average_empty)
# Without the "if len(...) == 0" line, the program crashed with ZeroDivisionError
# (division by zero), because an empty list has 0 months.
# With it, the function returns None, which means "no result".
# I think this is acceptable: the program does not crash, and None is clearly
# different from a real budget of 0 euros.
# Result when I ran it: None. Test OK.
 
