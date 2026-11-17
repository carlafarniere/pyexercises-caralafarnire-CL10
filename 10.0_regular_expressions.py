"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. What goes in?
#    Three answers typed by the user to register a new marketing campaign:
#    the campaign code, the contact email and the contact phone number.
#
# 2. What happens to it?
#    Each answer is cleaned with strip(), then checked against its rule with
#    re.fullmatch. fullmatch means the WHOLE text must follow the rule, not just a part.
#    The program says for each field if it is OK or not.
#
# 3. What comes out?
#    If the three answers are OK: one line is added to campaigns.csv (header only once).
#    If one answer is wrong: a message says which one, and nothing is saved.
#
# 4. My three fields and my rules (in plain English):
#    - Campaign code: 3 capital letters, a dash, then 4 digits. Example: SUM-2026.
#      I reject small letters (sum-2026) and missing parts (SUM2026, SU-2026).
#    - Email: some letters, digits, dots, dashes or underscores, then one @, then a
#      domain name, a dot, and at least 2 letters at the end. No spaces.
#      Example: carla.f@skema.edu. I reject carla.skema.edu (no @) and carla@skema (no dot).
#      Borderline case: I accept capital letters before the @, but the ending (fr, com)
#      must be small letters. I do not try to accept every real email, only the usual ones.
#    - French phone number: exactly 10 digits, the first one is 0, no spaces.
#      Example: 0612345678. I reject 612345678 (9 digits) and 06 12 34 56 78 (spaces).
 
import re
import csv
import os
 
FILE_NAME = "campaigns.csv"
 
# Campaign code: [A-Z]{3}  = 3 capital letters
#                -         = a dash
#                \d{4}     = 4 digits (\d means one digit 0-9)
CODE_PATTERN = r"[A-Z]{3}-\d{4}"
 
# Email: [\w.-]+   = one or more letters, digits, _ (that is \w), dots or dashes
#        @         = the @ sign, once
#        [\w-]+    = the domain name (skema), one or more letters, digits or dashes
#        \.        = a real dot (the \ is needed because . alone means "any character")
#        [a-z]{2,} = at least 2 small letters at the end (fr, com, edu)
EMAIL_PATTERN = r"[\w.-]+@[\w-]+\.[a-z]{2,}"
 
# Phone: 0     = starts with the digit 0
#        \d{9} = then 9 more digits, so 10 digits in total
PHONE_PATTERN = r"0\d{9}"
 
 
# Gives True if the whole text follows the pattern, False otherwise
def is_valid(text, pattern):
    return re.fullmatch(pattern, text) is not None
 
 
# Adds one line to the file; writes the header only if the file is new
def save_campaign(code, email, phone):
    file_is_new = not os.path.exists(FILE_NAME)
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file_is_new:
            writer.writerow(["code", "email", "phone"])
        writer.writerow([code, email, phone])
 
 
def main():
    code = input("Campaign code (example SUM-2026): ").strip()
    email = input("Contact email: ").strip()
    phone = input("Phone number (10 digits, no spaces): ").strip()
 
    # I check the three fields and keep the result of each one
    code_ok = is_valid(code, CODE_PATTERN)
    email_ok = is_valid(email, EMAIL_PATTERN)
    phone_ok = is_valid(phone, PHONE_PATTERN)
 
    print("Campaign code:", "OK" if code_ok else "wrong, 3 capital letters, a dash, 4 digits")
    print("Email:", "OK" if email_ok else "wrong, it needs one @ and a dot in the domain")
    print("Phone:", "OK" if phone_ok else "wrong, 10 digits starting with 0, no spaces")
 
    # I save only when all three are acceptable
    if code_ok and email_ok and phone_ok:
        save_campaign(code, email, phone)
        print("Saved in", FILE_NAME)
    else:
        print("Nothing saved. Please run the program again.")
 
 
# Runs main() only when this file is the one being executed
if __name__ == "__main__":
    main()
 
 
# Check it yourself: I ran it 3 times, so 9 values (1 pass + 2 fails per field).
# - Run 1: SUM-2026 / carla.f@skema.edu / 0612345678 -> OK, OK, OK, saved.
# - Run 2: sum-2026 / carla.skema.edu / 612345678 -> wrong, wrong, wrong, nothing saved.
# - Run 3: SUM2026 / carla@skema / 06 12 34 56 78 -> wrong, wrong, wrong, nothing saved.
# Surprise: carla@student.skema.edu is refused, but it is a real email. My domain part
# [\w-]+ does not accept a dot, so "student.skema" fails. I keep my rule simple and I
# accept this limit: most campaign contacts have an email like name@company.com. 