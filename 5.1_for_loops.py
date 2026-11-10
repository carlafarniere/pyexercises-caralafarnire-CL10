"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of 8 monthly advertising budgets from exercise 4.0.
# 2. Process: a for loop goes through every budget, one by one, and computes
#    its share of the total budget in %.
# 3. Out: one line per month with its position, its budget and its share.
# 4. What I compute for each item, and why it is worth showing:
#    the share of the total budget. The reader sees at once which months
#    took the biggest part of the money (March 16.7%, August 16.1%).


# Your code below
# My list from exercise 4.0: advertising budget per month, January to August
budgets = [1200, 950, 1500, 800, 1300, 1100, 700, 1450]

# The total, needed to compute each share
total = sum(budgets)

# For every position in the list: position, budget and share of the total
for i in range(len(budgets)):
    share = round(budgets[i] / total * 100, 1)
    print("Month", i + 1, ": budget", budgets[i], "euros, share of total:", share, "%")

# Check:
# - The program printed 8 lines, and my list has 8 budgets: no off-by-one.
# - By hand: 1200 / 9000 * 100 = 13.3 %, the program shows 13.3 % for month 1.