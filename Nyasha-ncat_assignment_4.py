"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game (Extended Edition)
Name: Nyasha
GitHub Username: Nyasha-ncat
Date: February 13, 2026
Description: An expanded college simulation game spanning the full semester.
             Manages GPA, Stress, and Social Points through 6 distinct events.
"""

# Step 1: Foundation Setup

student_name = "Nyasha"
current_gpa = 3.5
study_hours = 0
social_points = 20
stress_level = 10

print(f"--- Welcome to the College Life Adventure, {student_name}! ---")
print("Objective: Balance your Trifecta (GPA, Social, Sanity).")
print(f"Starting Stats: GPA: {current_gpa} | Stress: {stress_level} | Social: {social_points}")
print("=" * 60)

# EVENT 1: Course Registration (Week 1)

print("\n[WEEK 1] Course Registration")
print("The Registrar needs your schedule for the semester. How hard do you want your semster to be?")
print("A) Light Load (12 credits) - Coasting")
print("B) Standard Load (15 credits) - The norm")
print("C) Overload (18+ credits) - Academic Weapon")

choice_1 = input("Enter choice (A/B/C): ").upper() # .upper changes lower case letter to uppercase

if choice_1 == "A":
    study_hours = 10
    stress_level -= 5
    print(">> Strategy: Less work, more fun.")
elif choice_1 == "B":
    study_hours = 25
    stress_level += 10
    print(">> Strategy: Balanced college life, balanced life. ")
elif choice_1 == "C":
    study_hours = 40
    # Only high GPA students can handle the overload without panic, there are levels to these things.
    if current_gpa >= 3.0:
        stress_level += 25
        print(">> Strategy: You're trying to get stuff done. Let's hope you don't burn out.")
    else:
        stress_level += 45
        print(">> WARNING: You are biting more than you can chew, stay strong though.")
else:
    print(">> Invalid input. The system auto-enrolled you in standard classes.")
    study_hours = 25
    stress_level += 15


# EVENT 2: The Social Scene

print("\n" + "-" * 30)
print("[EVENT 2] Friday Night Lights") # J Cole iykyk
print("Your friends are going out, but you have an essay due.")
print("Options: Party, Library, Sleep")

choice_2 = input("Where are you going? ")

if choice_2 == "Party":
    social_points += 25
    current_gpa -= 0.1
    stress_level -= 10
    print(">> You danced the stress away, but your essay is trash.")
elif choice_2 == "Library":
    current_gpa += 0.2
    social_points -= 5
    stress_level += 10
    print(">> You got an A, but you couldn't stop hearing conversations about the party in the library.")
elif choice_2 == "Sleep":
    stress_level -= 20
    print(">> You slept like a baby, health over anything.")
else:
    # This handles any invalid input simply
    print(">> You stood indecisively in the hallway. Wasted time.")
    stress_level += 10
    social_points -= 5

# EVENT 3: The Roommate Dispute

print("\n" + "-" * 30)
print("[EVENT 3] The Dirty Dishes War")
print("Your roommate left a mountain of dishes. Again.")
print("A. Clean them yourself (Passive)")
print("B. Leave a sticky note (Passive-Aggressive)")
print("C. Throw them in their bed (Aggressive)")

choice_3 = input("Choose (A/B/C): ")

if choice_3 == "A":
    stress_level += 15
    print(">> You did everything by yourself again (SMH). Now look at you, your mad.")
elif choice_3 == "B":
    social_points -= 5
    stress_level += 5
    print(">> They ignored the note. Now it's awkward.")
elif choice_3 == "C":
    social_points -= 20
    stress_level -= 5
    print(">> You chose violence. Welp, thats one way to handle it")
else:
    print(">> You did nothing, your roomate won't clean them, and now the house stinks.")
    stress_level += 10

# EVENT 4: Midterm Exams

print("\n" + "-" * 30)
print("[EVENT 4] Midterm Exams")
print(f"Current Status -> Stress: {stress_level} | Study Hours: {study_hours}")

# Logical Operators (and, or)
if study_hours >= 25 and stress_level < 60:
    print(">> You crushed the exams, now this is what a perfect student looks like")
    current_gpa += 0.3
elif study_hours < 15 or stress_level > 80:
    print(">> You failed. Don't act surprissed.")
    current_gpa -= 0.6
    stress_level += 20
else:
    print(">> You passed, barely.")
    stress_level += 5

# EVENT 5: Spring Break Plans

print("\n" + "-" * 30)
print("[EVENT 5] Spring Break Decision")
print("Everyone is going to Miami. What are you doing?")
print("Destinations: Miami, Home, Work")

choice_5 = input("Enter destination: ")

fun_locations = ["Miami", "NYC", "Beach"]

if choice_5 in fun_locations:
    social_points += 40
    current_gpa -= 0.2
    stress_level -= 15
    print(">> You had the time of your life.")
elif choice_5 == "Home":
    stress_level -= 30
    print(">> Home cooked meals and free laundry. Smart choice.")
elif choice_5 == "Work":
    stress_level += 10
    current_gpa += 0.1
    print(">> You grinded all week. No fun, but productive.")
else:
    print(">> You couldn't decide and stayed in the dorms alone.")
    social_points -= 10

# EVENT 6: The Tech Disaster

print("\n" + "-" * 30)
print("[EVENT 6] The Laptop Crash")
print("It's 2 AM. Your laptop crashes while working on a 5 page paper.")
print("Do you have a backup? (Yes/No)")

choice_6 = input("Enter Yes or No: ").upper()

if choice_6 == "YES":
    stress_level += 5
    print(">> Thank goodness for the cloud. You only lost 5 minutes of work.")
else:
    stress_level += 50
    current_gpa -= 0.4
    print(">> You lost the whole file. Murphy's law in full effect.")

# EVENT 7: The Group Project

print("\n" + "-" * 30)
print("[EVENT 7] The Group Project from Hell")
print("Your partner isn't replying. What do you do?")
print("1. Do it all yourself")
print("2. Snitch to the professor")

choice_7 = input("Choose (1 or 2): ")

if choice_7 == "1":
    current_gpa += 0.2
    stress_level += 25
    print(">> You carried the team. Lost sleep, but anything for that the gpa.")
elif choice_7 == "2":
    social_points -= 15
    print(">> You told on them. The class thinks you're a snitch, who cares.")
else:
    current_gpa -= 0.3
    print(">> You waited too long and submitted a half-finished project.")

# EVENT 8: Finals Week

print("\n" + "-" * 30)
print("[EVENT 8] Finals Week")
print("The final battle. Choose your strategy:")
print("A) All-Nighter (High Risk)")
print("B) Group Study (Social)")
print("C) Sleep & Pray (Health)")

choice_8 = input("Choose strategy (A/B/C): ").upper()

if choice_8 == "A":
    if stress_level < 70:
        current_gpa += 0.4
        print(">> The monster, celcius, and coffee did its job. who cares about sleep.")
    else:
        current_gpa -= 0.2
        print(">> You fell asleep during the exam. Tragic(Could never be me).")
elif choice_8 == "B":
    if social_points > 50:
        current_gpa += 0.2
        print(">> Your friends actually helped you study.")
    else:
        print(">> Nobody invited you to the study group.")
        stress_level += 10
elif choice_8 == "C":
    stress_level -= 30
    print(">> You prioritized mental health. The exam was hard, but you were calm.")
else:
    print(">> Panic set in. You blanked.")
    current_gpa -= 0.5
