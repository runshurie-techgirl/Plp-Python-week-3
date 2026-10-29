# Plp-Python-week-3

# Grade Reporter & Bug Hunt

## About This Project

This project is my Week 3 Python assignment.

It practises two big ideas: repeating work with loops, and making decisions with conditions.

It has two small programs, and each one trains a different skill.

## Files

- `grade_reporter.py` - Goes through five scores and gives each one a grade.

- `bug_hunt.py` - A broken program with three bugs, fixed so it prints the right answer.

## Part A: Grade Reporter

The program starts with the list `[72, 45, 90, 61, 38]`.

A `for` loop goes through each score, one at a time.

Inside the loop, `if` / `elif` / `else` gives each score a grade:

- 80 and above is A.
- 70 to 79 is B.
- 50 to 69 is C.
- Below 50 is F.

A score of 50 or more counts as a pass.

The program counts the passes and fails itself.

It also adds up all the scores and prints the average, rounded to one decimal place.

The average is 61.2.

## Part B: Bug Hunt

The program should add 1 + 2 + 3 + 4 + 5 and print 15.

It started with three bugs, and I fixed them one at a time.

## How I Found and Fixed the Bugs

**Run 1: the program would not start.**

Python showed `SyntaxError: expected ':'` on line 4.

The `while` line had no colon at the end.

I added the colon, and the error disappeared.

**Run 2: the program started, then crashed at the end.**

Python showed `TypeError: can only concatenate str (not "int") to str` on line 8.

The `print` line was joining text and a number with `+`, and Python cannot do that.

I changed `total` to `str(total)` so both sides were text.

**Run 3: the program finished, but the answer was wrong.**

There was no error message, and it printed `Sum of 1 to 5 is: 10`.

I expected 15, so I knew the output was wrong even though Python did not complain.

I followed the loop one round at a time:

| count | Is count < 5? | total after the round |
|-------|---------------|-----------------------|
| 1 | yes | 1 |
| 2 | yes | 3 |
| 3 | yes | 6 |
| 4 | yes | 10 |
| 5 | no, the loop stops | 10 (5 was never added) |

The condition `count < 5` is false when `count` is 5, so the loop stopped before adding the last number.

I changed `<` to `<=`, so the loop now also runs when `count` is 5.

**Run 4: the program printed the correct answer.**

The final output is `Sum of 1 to 5 is: 15`.

Each fix has a `# BUG:` comment above it that explains what was wrong.

## How to Run

Run `python grade_reporter.py` to see the grades, pass count, fail count and average.

Run `python bug_hunt.py` to see the fixed sum.

## Reflection

The hardest bug to find was the third one, because the program ran without any error message, so Python gave me no clue about where the mistake was.

I knew something was wrong because the program printed 10, but when I added 1 + 2 + 3 + 4 + 5 by hand I got 15, so the output did not match the answer I expected.

I traced the loop round by round and saw that when `count` reached 5, the condition `count < 5` became false and the loop stopped before adding 5, so I changed it to `count <= 5` and the program printed 15.
