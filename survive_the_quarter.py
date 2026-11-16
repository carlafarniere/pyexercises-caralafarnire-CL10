# Name: Carla Farniere          Group: C
#
# 1. What goes in?
#    scenarios_C.csv. The separator is a comma. Some texts contain commas, so they are
#    between quotes: the csv module handles that for me.
#    14 columns: Event (the situation), Day (the scenario number, I do not use it),
#    Decision 1, 2, 3 (the three options), Reputation 1, 2, 3, Budget 1, 2, 3,
#    Outcome 1, 2, 3 (the feedback line).
#    The numbers are written as text with a sign and a unit: "+15 pts", "-800 EUR".
#    To compute, I keep only the part before the space and turn it into an int.
#    The impact of option B is in the columns with "2": Decision 2, Budget 2,
#    Reputation 2, Outcome 2.
#    The player also types their name, the difficulty and A, B or C each day.
#
# 2. What happens? The steps of one day:
#    - show the day number and both gauges
#    - show the situation and the options A, B, C
#    - ask A, B or C until the answer is valid
#    - add the budget and reputation change of the chosen option
#    - keep the reputation at 100 maximum
#    - show the feedback line and the changes
#    - save the day in the history (a list of tuples)
#    - if budget or reputation is 0 or less: game over, stop at once
#
# 3. What comes out?
#    On screen: "fired" and the reason, or the final score and the title, then the best
#    and the worst move. In results.csv, one line per game, for example:
#    Carla,6350,100,CMO Material,2026-11-16
#
# 4. What could go wrong?
#    - The player types a wrong key (d, 1, nothing): I ask again until A, B or C.
#    - A gauge goes below zero: the game stops at once and says which one.
#    - The reputation goes above 100: I bring it back to 100.
#    - The scenario file is missing: I show a message and stop, without crashing.
#    - The player types an empty name: I ask again.
#
# My feature: d, Difficulty. I chose it because it changes the whole game with one
# question at the start (easy 15,000 EUR or hard 6,000 EUR), and I can test it easily.
 
import csv
import random
import os
from datetime import date
 
SCENARIO_FILE = "scenarios_C.csv"
RESULTS_FILE = "results.csv"
START_REPUTATION = 50
MAX_REPUTATION = 100
DAYS = 10
 
 
# Turns a text like "+15 pts" or "-800 EUR" into a number (15 or -800)
def text_to_number(text):
    return int(text.split()[0])
 
 
# Reads my scenario file and gives back a list of scenarios.
# Each scenario is a dictionary: the situation, and a list of 3 options.
# Each option is a tuple: (text, budget_change, reputation_change, feedback)
def load_scenarios(file_name):
    scenarios = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = []
            for number in ["1", "2", "3"]:
                option = (row["Decision " + number],
                          text_to_number(row["Budget " + number]),
                          text_to_number(row["Reputation " + number]),
                          row["Outcome " + number])
                options.append(option)
            scenarios.append({"event": row["Event"], "options": options})
    return scenarios
 
 
# Asks a question again until the answer is not empty
def ask_name():
    name = input("What is your name? ").strip()
    while name == "":
        name = input("Please type your name: ").strip()
    return name
 
 
# My feature: asks the difficulty and gives back the starting budget
def ask_difficulty():
    answer = input("Difficulty, easy or hard? ").strip().lower()
    while answer not in ["easy", "hard"]:
        answer = input("Please type easy or hard: ").strip().lower()
    if answer == "easy":
        return 15000
    return 6000
 
 
# Asks A, B or C until the answer is valid (small letters accepted).
# Gives back the position of the option: 0 for A, 1 for B, 2 for C
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ["A", "B", "C"]:
        answer = input("Please type A, B or C: ").strip().upper()
    return ["A", "B", "C"].index(answer)
 
 
# Applies one option to the two gauges and gives back both new values as a tuple
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, MAX_REPUTATION)
    return budget, reputation
 
 
# Gives the title that matches the final score
def get_title(score):
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    return "Viral Legend"
 
 
# Adds one line to results.csv; writes the header only if the file is new
def save_result(name, budget, reputation, title):
    file_is_new = not os.path.exists(RESULTS_FILE)
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file_is_new:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today()])
 
 
# Runs the whole game, day by day
def main():
    # If the file is missing, I stop with a clear message instead of crashing
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print("I cannot find", SCENARIO_FILE, "- put it in the same folder as the game.")
        return
 
    name = ask_name()
    budget = ask_difficulty()
    reputation = START_REPUTATION
 
    # I mix the scenarios and keep only the first 10
    random.shuffle(scenarios)
    history = []
    fired_reason = ""
 
    for day in range(1, DAYS + 1):
        scenario = scenarios[day - 1]
        print()
        print("--- Day", day, "---")
        print("[Budget:", budget, "EUR | Reputation:", str(reputation) + "/100]")
        print(scenario["event"])
        for letter, option in zip(["A", "B", "C"], scenario["options"]):
            print("   " + letter + ":", option[0])
 
        option = scenario["options"][ask_choice()]
        budget, reputation = apply_choice(budget, reputation, option)
        text, budget_change, reputation_change, feedback = option
        print(feedback)
        print("Budget", f"{budget_change:+}", "EUR, Reputation", f"{reputation_change:+}")
 
        # One tuple per day; the reputation change comes first so I can compare them
        history.append((reputation_change, day, text))
 
        # Game over at once if a gauge reaches 0
        if budget <= 0:
            fired_reason = "the budget is at " + str(budget) + " EUR"
            break
        if reputation <= 0:
            fired_reason = "the reputation is at " + str(reputation)
            break
 
    # The end: fired, or score and title
    print()
    print("=" * 30)
    if fired_reason != "":
        title = "Fired"
        print("You are fired:", fired_reason + ".")
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Quarter survived!")
        print("Budget left:", budget, "EUR, reputation:", str(reputation) + "/100")
        print("Final score:", score)
        print(name + ", your title:", title)
 
    # Best and worst move: max and min compare the tuples by reputation change first
    best = max(history)
    worst = min(history)
    print()
    print("Best move:  day", best[1], '"' + best[2] + '"', f"({best[0]:+})")
    print("Worst move: day", worst[1], '"' + worst[2] + '"', f"({worst[0]:+})")
 
    save_result(name, budget, reputation, title)
    print("Saved in", RESULTS_FILE)
 
 
# Runs main() only when this file is the one being executed
if __name__ == "__main__":
    main()
 