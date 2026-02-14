"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game (Extended Edition)
Name: Nyasha
GitHub Username: Nyasha-ncat
Date: February 13, 2026
Description: An expanded college simulation game spanning the full semester.
             Manages GPA, Stress, and Social Points through 6 distinct events.
"""
# ========================================
# Step 1: Foundation Setup
# ========================================

student_name = "Nyasha"
current_gpa = 3.5
study_hours = 0
social_points = 20
stress_level = 10

print(f"--- Welcome to the College Life Adventure, {student_name}! ---")
print("Objective: Balance your Trifecta (GPA, Social, Sanity).")
print(f"Starting Stats: GPA: {current_gpa} | Stress: {stress_level} | Social: {social_points}")
print("=" * 60)

# ========================================
# EVENT 1: Course Registration (Week 1)
# ========================================

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
