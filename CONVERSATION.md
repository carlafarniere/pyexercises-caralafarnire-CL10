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
