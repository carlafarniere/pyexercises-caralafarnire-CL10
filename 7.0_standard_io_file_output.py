"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: four answers typed by the user about one advertising campaign:
#    the month, the channel (Instagram, Google Ads...), the budget in euros and the clicks.
# 2. Process: the program asks each value with input(). If a value is not acceptable,
#    it says why and asks again. Then it adds one line to the CSV file.
#    The very first time, the file does not exist yet: the program writes the header first.
# 3. Out, file name and columns: campaign_log.csv, with the columns
#    Month, Channel, Budget, Clicks.
# 4. Why these columns, and what this file is for:
#    it continues my exercise 4.0 (monthly ad budgets). With budget and clicks for each
#    channel and month, once the file has 200 rows I could compute the cost per click
#    (budget / clicks) and see which channel brings clicks for the least money.
#    My two decisions:
#    - First time: I check if the file exists. If not, I write the header, only once.
#    - Unacceptable value (empty text, budget or clicks with letters): I ask again,
#      so a bad line never goes into the file.
 
 
# Your code below
import os
 
file_name = "campaign_log.csv"
 
# Asks a question again and again until the answer is not empty
def ask_not_empty(question):
    answer = input(question).strip()
    while answer == "":
        print("This field cannot be empty.")
        answer = input(question).strip()
    return answer
 
# Asks a question until the answer is a whole number (only digits)
def ask_whole_number(question):
    answer = input(question).strip()
    while not answer.isdigit():
        print("Please type a whole number, digits only (for example 1200).")
        answer = input(question).strip()
    return answer
 
 
print("Please fill in the campaign details:")
month = ask_not_empty("Month (e.g. January): ")
channel = ask_not_empty("Channel (e.g. Instagram): ")
budget = ask_whole_number("Budget in euros: ")
clicks = ask_whole_number("Number of clicks: ")
 
# I check BEFORE opening: if the file is not there yet, it will need its header
file_is_new = not os.path.exists(file_name)
 
# Mode "a" (append) adds at the end of the file instead of erasing it
with open(file_name, "a", newline="") as file:
    if file_is_new:
        file.write("Month,Channel,Budget,Clicks\n")
    file.write(month + "," + channel + "," + budget + "," + clicks + "\n")
 
print("Data saved successfully!")
 
 
# Check it yourself: I ran the program three times with three different campaigns.
# Then I opened campaign_log.csv and counted the lines:
# 1 header line + 3 entries = 4 lines. Test OK.
# I also typed an empty channel and the budget "12OO" (letters O): each time the
# program refused and asked again.
 