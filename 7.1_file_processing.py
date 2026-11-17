"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Empty lines (line 3 and line 9): they are not names.
# - Spaces at the start of some lines ("  alan TURING", "  linus torvalds").
# - Capital letters are mixed: "ada LOVELACE", "grace hopper", "GUIDO van rossum".
#   Nothing is written the same way.
# - One last name has two words: "van rossum". If I take only the last word, I would
#   sort Guido under "rossum", and "van" would be lost or treated as a first name.
# - The names are not in any order.
 
# 1. In: names.txt, one person per line, first name then last name.
# 2. Process, problem by problem:
#    - Empty lines: I skip every line that is empty after removing spaces.
#    - Spaces at the start/end: strip() removes them, split() ignores double spaces.
#    - Mixed capitals: I rewrite each word with only its first letter in capital,
#      except "van", which stays in small letters as in "van Rossum".
#    - Two-word last name: the first word is the first name, ALL the other words are
#      the last name.
#    - Order: I sort the clean names by last name, ignoring capitals and "van".
# 3. Out: a new file names_sorted.txt, one clean name per line, sorted by last name.
#    names.txt is only read, never modified.
# 4. How I decide which word is the last name:
#    In this file every line starts with the first name. So the first word is the first
#    name and everything after it is the last name. For "GUIDO van rossum" the last name
#    is "van Rossum", and I sort it under R (Rossum), because "van" is a particle.
 
 
# Your code below
 
input_file = "names.txt"
output_file = "names_sorted.txt"
 
# Reads the file and gives back its lines, without changing the file
def load_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.readlines()
 
# Cleans one line: removes extra spaces and fixes the capitals.
# Gives back None for an empty line, so I can skip it.
def clean_name(line):
    words = line.split()
    if len(words) == 0:
        return None
    clean_words = []
    for word in words:
        if word.lower() == "van":
            clean_words.append("van")
        else:
            clean_words.append(word.capitalize())
    return " ".join(clean_words)
 
# Gives the word used to sort: the last name, without "van", in small letters
def sort_key(name):
    last_name_words = name.split()[1:]
    if last_name_words[0] == "van":
        last_name_words = last_name_words[1:]
    return " ".join(last_name_words).lower()
 
# Writes the clean names in a new file, one per line
def save_names(names, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")
 
# Runs the whole program, step by step
def main():
    lines = load_lines(input_file)
    clean_names = []
    for line in lines:
        name = clean_name(line)
        if name is not None:
            clean_names.append(name)
    sorted_names = sorted(clean_names, key=sort_key)
    save_names(sorted_names, output_file)
    print("Lines in", input_file, ":", len(lines))
    print("Names in", output_file, ":", len(sorted_names))
    print(sorted_names)
 
# Runs main() only when this file is the one being executed
if __name__ == "__main__":
    main()
 
 
# Check it yourself:
# - names.txt has 10 lines, names_sorted.txt has 8 lines. The difference is 2,
#   because the 2 empty lines (line 3 and line 9) were removed.
# - By hand: the first last name in alphabetical order is Hamilton (H-a before H-o of
#   Hopper), the last one is Turing (T-u after T-o of Torvalds).
#   My file starts with Margaret Hamilton and ends with Alan Turing. Test OK.
