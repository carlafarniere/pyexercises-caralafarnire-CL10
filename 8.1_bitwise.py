"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: three permissions for a marketing campaign, each one stored as one bit:
#    VIEW = 1 (binary 001), EDIT = 2 (binary 010), PUBLISH = 4 (binary 100).
# 2. Process: I give a person VIEW and EDIT (combined with |), I test if they can
#    PUBLISH (with &), then I add PUBLISH (with |) and remove EDIT (with & and ~).
# 3. Out: on screen, at each step, the value as a number and in binary (3 bits),
#    and the answer True or False to "can this person publish?".
# 4. What my permissions are about:
#    who may work on a campaign: VIEW = see the campaign and its results,
#    EDIT = change the texts and the budget, PUBLISH = put the campaign online.
#    Example: an intern can view and edit, but only the manager can publish.


# Your code below

# Each permission is one bit, so they never overlap
VIEW = 1      # 001
EDIT = 2      # 010
PUBLISH = 4   # 100

# Shows a value as a number and as 3 bits, so I can read each permission
def show(step, value):
    print(f"{step:<30} {value}  ->  {value:03b}")

# Step 1: an intern gets VIEW and EDIT. | turns on both bits
intern = VIEW | EDIT
show("Intern: VIEW | EDIT", intern)

# Step 2: can the intern publish? & keeps only the PUBLISH bit: 0 means no
can_publish = (intern & PUBLISH) != 0
print("Can the intern publish?", can_publish)

# Step 3: the intern is promoted: I add PUBLISH with |
intern = intern | PUBLISH
show("Add PUBLISH", intern)

# Step 4: I remove EDIT: ~EDIT has every bit on except EDIT, & keeps the others
intern = intern & ~EDIT
show("Remove EDIT", intern)
print("Can publish now?", (intern & PUBLISH) != 0)
print("Can edit now?", (intern & EDIT) != 0)


# Check it yourself: I read the bits at each step (from right to left: VIEW, EDIT, PUBLISH).
# 011 = VIEW + EDIT, no PUBLISH -> "Can the intern publish?" False. Correct.
# 111 = all three permissions after adding PUBLISH. Correct.
# 101 = VIEW + PUBLISH, the middle bit (EDIT) is off. Correct.
