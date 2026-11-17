"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. The two failures, and whether they deserve the same message:


# 1. In: the number of conversions of a campaign, typed by the user.
# 2. Process: the program divides the campaign budget (1200 EUR) by the conversions
#    to get the cost per conversion (CPA). If the answer is not usable, it explains why
#    and asks again, 3 attempts maximum.
# 3. Out: the cost per conversion, for example "Cost per conversion: 30.0 EUR",
#    or a clear message after 3 failed attempts. The program never crashes.
# 4. The two failures, and whether they deserve the same message:
#    - ValueError: the user typed text ("abc") or nothing. Message: "type a whole number".
#    - ZeroDivisionError: the user typed 0. This is a real campaign with no conversions,
#      not a typing mistake. Message: "no conversions, the cost per conversion cannot
#      be computed".
#    They do NOT deserve the same message: one is a typing error, the other is a real
#    business result. This is the case of the two campaigns with 0 conversions in the exam.
#    Why catch each error separately: with one "except" for everything, the user would get
#    the same vague message for both, and a real bug in my code would be hidden too.


# Your code below

BUDGET = 1200
MAX_ATTEMPTS = 3

# Asks the conversions and tries to compute the cost per conversion, 3 attempts maximum
attempt = 0
while attempt < MAX_ATTEMPTS:
    attempt = attempt + 1
    answer = input("Number of conversions: ")
    try:
        conversions = int(answer)
        cost = BUDGET / conversions
        print("Cost per conversion:", round(cost, 2), "EUR")
        break
    # Text or empty line: int() cannot read it
    except ValueError:
        print("Please type a whole number, for example 40.")
    # Zero: a campaign with no conversions, the division is impossible
    except ZeroDivisionError:
        print("This campaign has no conversions: the cost per conversion cannot be computed.")
        break
else:
    # The loop ended without break: 3 wrong answers in a row
    print("Too many wrong answers. Stopping here.")


# Check it yourself: I ran it 4 times.
# - 40: "Cost per conversion: 30.0 EUR" (1200 / 40 = 30). Correct.
# - 0: "This campaign has no conversions..." and the program stops calmly.
# - abc: "Please type a whole number" and it asks again.
# - empty line: same message as abc (also a ValueError), it asks again.
# After 3 wrong answers: "Too many wrong answers". It never crashed.

