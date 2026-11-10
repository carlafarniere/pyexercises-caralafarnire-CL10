"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user's answers to one question about my budgets from exercise 4.0:
#    "Which month had the biggest advertising budget?"
# 2. Process: a while loop asks again after each wrong answer. Each answer is
#    cleaned with .strip().lower(), so "March", "march" and " MARCH " count
#    as the same answer: my decision, because only the word matters.
# 3. Out: a message after each attempt, then a summary.
# 4. Stop condition: the answer is "march" OR 3 attempts are used.
#    Limit: 3 attempts, then the program stops and gives the right answer.
#    Summary: success or not, number of attempts used, list of answers given.

# Your code below
max_attempts = 3
attempts = 0
found = False
answers = []   # every answer, to show in the summary

while attempts < max_attempts and not found:
    answer = input("Which month had the biggest advertising budget? ")
    attempts = attempts + 1
    answers.append(answer)
    # Same answer with or without capitals and extra spaces
    if answer.strip().lower() == "march":
        found = True
        print("Correct!")
    else:
        print("Wrong. Attempts left:", max_attempts - attempts)

# Summary
print("--- Summary ---")
if found:
    print("Found in", attempts, "attempt(s).")
else:
    print("Limit reached. The answer was March (1500 euros).")
print("Answers given:", answers)

# Check:
# - Three wrong answers: the program stops after attempt 3.
# - " MARCH " is accepted as correct.