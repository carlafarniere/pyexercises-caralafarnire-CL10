# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-11-10 22:02, in .

**Me:** Exercise 1.0: What does the print() function do?

**Tutor:**

The print() function displays text or values on the screen.

Pattern:
```python
# TODO: print the text "Hello, world!"
print("Hello, world!")
```

What does print() expect as its argument?

**My note:** print() expects what I want to display between the parentheses: text in quotes ("Hello World") or a number. In exercise 1.0 I used it 6 times: once for "Hello World", then 5 times for my numbered name.
---
## 2026-11-10 22:25, in .

**Me:** Exercise 2.0: Why does input() give text and how do I add 1 to it?

**Tutor:**

The concept is: `input()` always returns a string, and you must convert it to a number before arithmetic.

```python
# TODO: ask the user for a number, convert it, then add 1
user_text = input("Enter a number: ")
# TODO: convert user_text to an integer or float
# TODO: add 1 to the number
result = # your number + 1
print("Result:", result)
```

Which function converts a string to an integer?

**My note:** input() always returns text, so age + 1 fails. I used int(age) to turn it into a number, and it crashes with ValueError if the user types a word instead of a number.
---
## 2026-11-10 22:38, in .

**Me:** Exercise 2.1: What does strip() do?

**Tutor:**

The `strip()` method removes leading and trailing whitespace from a string.

```python
text = "   Hello, world!   "
clean_text = text.strip()  # TODO: What will clean_text be?
```

What is the exact output of `clean_text` after running this code?

**My note:** strip() removes the spaces at both ends only, so clean_text is "Hello, world!". In my program, the other methods (upper, lower, title) keep those spaces, so strip() is useful to clean form answers.

---
## 2026-11-10 22:55, in .

**Me:** Exercise 3.0: In my code number_1 / number_2 gives 3.5 for 7 and 2. Why not 3, and how do I get only the whole number?

**Tutor:**

Division with / always returns a float in Python.
To get the whole number part, use integer division //.

```python
# TODO: replace 7 and 2 with your variables
result = 7 // 2
```

What is the type of the value returned by //?

**My note:** / always returns a float, so 7 / 2 gives 3.5. // keeps only the whole part and returns an int when both numbers are int: 7 // 2 gives 3. I kept / in my program because I want the exact result.
---
## 2026-11-10 23:07, in .

**Me:** Exercise 3.1: In my code, what does i % 2 == 0 check?

**Tutor:**

Checking even indices.
The expression `i % 2 == 0` checks whether the index `i` is even.

```python
# TODO: write a loop that prints every other element
items = ["alpha", "beta", "gamma", "delta"]
for i in range(len(items)):
    if i % 2 == 0:        # TODO: what does this condition do?
        print(items[i])
```

What does the condition `i % 2 == 0` evaluate to when `i` is 0?

**My note:** % gives the remainder of a division, so i % 2 == 0 is True when i is even. When i is 0, 0 % 2 is 0, so the condition is True. In my program, i starts at 1, so it prints "is odd" for 1, 3, 5 and "is even" for 2, 4, 6.

---
## 2026-11-10 23:21, in .

**Me:** Exercise 4.0: In my list, why does budgets[2] give the third item and not the second? How does list indexing work in Python?

**Tutor:**

List indexing starts at 0, so the first item is at index 0, the second at index 1, and the third at index 2.

```python
budgets = ["low", "medium", "high", "very high"]
# TODO: What does budgets[0] print?
print(budgets[2])  # prints the third item
```

What is the index of the last item in the list?

**My note:** Python counts from 0, so budgets[2] is the third item (March in my list). The last item of a list of 4 is at index 3. In my list of 8 budgets, the last one (August) is budgets[7].

---
## 2026-11-10 23:26, in .

**Me:** Exercise 4.2: In my dictionary, why does customer["phone"] crash with KeyError but customer.get("phone") does not?

**Tutor:**

Dictionary lookup with square brackets vs .get()

When you use customer["phone"] the program looks for the exact key "phone".
If the key is missing, Python raises a KeyError.

customer.get("phone") asks for the key "phone" but returns None if the key is missing instead of raising an error.

TODO pattern
```python
customer = {"name": "alpha", "email": "beta@example.com"}

# This line will crash:
# phone = customer["phone"]

# This line will not crash:
phone = customer.get("phone")
```

Question: Which method returns a default value when the key is missing?

**My note:** customer["phone"] crashes with KeyError because the key does not exist. The method that returns a default value is .get(): in my program, customer.get("phone", "not available") displays "not available" instead of crashing.

---
## 2026-11-10 23:31, in .

**Me:** Exercise 4.1: In my list, what is the difference between sorted(budgets) and budgets.sort()?

**Tutor:**

Difference between sorted() and .sort()

- sorted(budgets) returns a new list that is sorted, leaving the original list unchanged.
- budgets.sort() sorts the list in place and returns None.

Pattern on toy data:

```python
budgets = [300, 150, 200]
sorted_budgets = sorted(budgets)  # TODO: what is sorted_budgets?
original_budgets = budgets.copy()  # TODO: what is budgets now?
budgets.sort()  # TODO: what is budgets after this line?
```

Which function leaves the original list unchanged?

**My note:** sorted() leaves the original list unchanged because it returns a new sorted list. budgets.sort() sorts the list in place and returns None. In my program I used sorted() and [::-1], so my last line shows the original list from 4.0 unchanged.

---
## 2026-11-10 23:41, in .

**Me:** Exercise 5.1: Here is my code: for i in range(len(budgets)): print(i + 1, budgets[i]). Why does range start at 0, and is i + 1 correct to number the items from 1?

**Tutor:**

Understanding range and indexing.

range(len(budgets)) starts at 0 because Python ranges are zero-based by default.
Adding 1 to i is the correct way to number items from 1.

Pattern:
```python
# TODO: replace budgets with your list
budgets = [1200, 800, 2100]

for i in range(len(budgets)):
    print(i + 1, budgets[i])
```

What does range(len(budgets)) produce when budgets has 3 items?

**My note:** range(len(budgets)) gives the positions 0 to 7 for my 8 budgets, because Python counts from 0 (with 3 items: 0, 1, 2). I print i + 1 so the months are numbered 1 to 8 for the reader, while budgets[i] still uses the real position.

---
## 2026-11-10 23:53, in .

**Me:** Exercise 5.2: In Python, how do I make sure a while loop stops after a maximum number of attempts, and why use answer.strip().lower() before comparing?

**Tutor:**

Concept: Guarding a while loop with a counter and normalising user input.

```python
max_attempts = 3
attempt = 0
secret = "python"

while attempt < max_attempts:
    guess = input("Enter the secret word: ")
    # TODO: normalise the input before comparing
    if guess.strip().lower() == secret:
        print("Correct!")
        break
    attempt += 1
else:
    print("Too many attempts.")
```

Why strip().lower()?
- `strip()` removes leading/trailing spaces.
- `lower()` converts the string to lowercase.

Question: Which two string methods are used to clean the input before comparison?

**My note:** My while loop has two exits: the right answer (found = True) or the counter reaching max_attempts = 3, so it can never run for ever. I clean each answer with strip() (removes spaces) and lower() (lowercase), so " MARCH " and "march" count as the same answer, as my test showed.