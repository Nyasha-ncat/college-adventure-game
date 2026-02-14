
# College Life Adventure Game (Extended Edition)

**Developer:** Nyasha

**GitHub:** [Nyasha-ncat](https://github.com/Nyasha-ncat)

## Description

This program is an interactive text-based adventure that simulates the chaotic life of a college student. Players must go through a full semester by making  decisions regarding course loads, fun, and health. The goal is to balance the "Trifecta": GPA, Social Points, and Stress Levels. Every choice changes the narrative, leading to one of many unique endings based on your final stats.

---

## Repository Files

* `Nyasha-ncat_assignment_4.py`: The main Python script containing the game logic, events, and ending trees.
* `test_assignment.py`: A script used for testing the program's functionality.
* `README.md`: Documentation for the project (this file).

---

## How to Run the Program
1. Copy code and paste into ide of your choice.
2. Run the game 
3. Follow the on-screen prompts and enter your choices (A, B, C, etc.) when prompted.

---

## Key Features

* Stat Tracking: Your GPA, Stress, and Social life are updated in real-time based on your choices.
* Input Handling: Uses .upper to ensure player inputs are valid regardless of case sensitivity.
* Complex Logic: Utilizes nested if statements and logical operators and,or to determine success in exams.
* Data Integrity Check: Includes an identity operator check is float to verify data types before the final audit.
* Archetype System: A robust "Ending Tree" that categorizes your performance into specific student personas.

---

Game Design & Concepts

Creative Theme

The game explores the "Academic Weapon" vs. "Social Butterfly" struggle. It focuses on the reality of college life—from the "Dirty Dishes War" with roommates to the panic of a 2 AM laptop crash.

Branching Concepts & Logic

* Simple Branching: Event 1 (Course Registration) uses if statments to set the baseline difficulty.
* Logical Operators: Event 4 (Midterms) checks multiple conditions
* Membership Operators: Event 5 (Spring Break) uses if choice_5 in fun_location to check a list of valid vacation spots.
* Nested Conditions: Event 8 (Finals) nests an if statement inside the "All-Nighter" choice to check if your stress level is too high to succeed.

The Ending Tree

The game features multiple endings based on your final "Audit":

* **THE UNICORN:** High GPA, high Social, low Stress (The perfect student).
* **THE BURNOUT GENIUS:** High GPA but dangerously high Stress.
* **THE PARTY ANIMAL:** Passing GPA but maxed-out Social points.
* **ACADEMIC PROBATION:** Failed the semester; the Dean wants a word.

---

AI Assistance Documentation

* Usage: AI was utilized specifically to help implement the identity operator within the final stat calculation section.
* Purpose: To learn how to verify that the current_gpa variable remained a float throughout the various mathematical operations in the game.

---

What I Learned

Through this assignment, I learned how to use git properly this time. Succesfully cloned a reposetory and can now use git commands. I also got better at my if statments, and managing logic of multi layer choices.
