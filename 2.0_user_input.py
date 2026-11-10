"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user types their first name and their age.
# 2. Process: I store both answers, convert the age into a number and add 1.
# 3. Out: sentences that repeat the name and age, and the age next year.
# 4. My two fields, and what I would do with them: first name and age,
#    for a marketing sign-up form: the name to personalise emails,
#    the age to target offers by age group.

# Your code below
# Ask the user for their name and age (input always returns text)
name = input("Enter your name:")
age = input("Enter your age:")

# Display each answer
print("My name is ", name )
print("My age is ", age)

# Join everything in one sentence (works because everything is text)
print("My name is " + name + " and my age is " + age)

# age + 1 crashes because age is text, so I convert it with int()
next_age = int(age) + 1
print("Next year I will be", next_age)

# Check:
# - Empty line: the program continues, the sentences show nothing after "is",
#   then int("") crashes with ValueError.
# - A space: same thing, a blank name or age, then ValueError.
# - Text instead of a number ("twenty"): ValueError: invalid literal for int().

