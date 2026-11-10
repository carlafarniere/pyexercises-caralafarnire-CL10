"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence typed by the user.
# 2. Process: Python applies four different string methods to the sentence.
# 3. Out: four transformed versions of the sentence, one per line.
# 4. My four transformations, and when each is useful:
#    - strip(): clean a form answer by removing spaces typed by mistake.
#    - upper(): write a promo code or a slogan in capitals.
#    - lower(): store emails in one format so "Carla@" and "carla@" match.
#    - title(): put a capital on each word of a customer's name.

# Your code below
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Show the four transformations, between [ ] to see the spaces
print("strip: [" + sentence.strip() + "]")
print("upper: [" + sentence.upper() + "]")
print("lower: [" + sentence.lower() + "]")
print("title: [" + sentence.title() + "]")

# Check: I typed "  hello My friend  " (spaces at both ends, capital in the middle)
# - strip: [hello My friend] -> expected, spaces at both ends removed.
# - upper: [  HELLO MY FRIEND  ] -> expected, but the spaces stay.
# - lower: [  hello my friend  ] -> expected, the capital M became m.
# - title: [  Hello My Friend  ] -> expected, every word starts with a capital.