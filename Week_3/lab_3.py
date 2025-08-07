# COMP11124 Object Oriented Programming - Week 3 Practical Lab Exercises

# =========================
# Exercise 1: Functions in Python
# =========================
# Task: Greet Friends
print("Exercise 1: Greet Friends")
def greet_friends(friend_names):
    for single_friend in friend_names:
        print(f"Greetings, {single_friend}! Welcome to the club.")
friend_group = ["John", "Jane", "Jack"]
greet_friends(friend_group)
# --- End of Greet Friends ---

# Task: Tax Calculation
print("\nExercise 1: Tax Calculation")
def calculate_income_tax(annual_income, rate_of_tax):
    return annual_income * rate_of_tax
tax_result_1 = calculate_income_tax(52000, 0.18)
print(f"Income tax for £52,000 at 18%: £{tax_result_1}")
tax_result_2 = calculate_income_tax(83000, 0.27)
print(f"Income tax for £83,000 at 27%: £{tax_result_2}")
# --- End of Tax Calculation ---

# Task: Compound Interest Calculator
print("\nExercise 1: Compound Interest Calculator")
def calculate_compound_interest(start_amount, years, yearly_rate):
    if yearly_rate < 0 or yearly_rate > 1:
        print("Interest rate must be between 0 and 1 (decimal form)")
        return None
    if years < 0:
        print("Years must be a positive integer")
        return None
    for current_year in range(years + 1):
        total_amount = start_amount * (1 + yearly_rate) ** current_year
        print(f"Year {current_year}: Investment value is £{total_amount:.2f}")
    return int(total_amount)
final_value = calculate_compound_interest(1200, 4, 0.04)
print(f"Total value after 4 years: £{final_value}")
# --- End of Compound Interest Calculator ---

# =========================
# Exercise 2: Variable Scope
# =========================
print("\nExercise 2: Variable Scope")
global_counter = 10
def scope_demo_function():
    local_counter = 25
    print(f"Inside function: local_counter = {local_counter}")
scope_demo_function()
print(f"Outside function: global_counter = {global_counter}")
# --- End of Variable Scope ---

# =========================
# Exercise 3: Assertions
# =========================
print("\nExercise 3: Assertions")
assert calculate_compound_interest(1200, 4, 0.04) == 1400, "Compound interest calculation did not match expected value"
# --- End of Assertions ---

# =========================
# Exercise 4: Fixing Common Errors
# =========================

# Syntax Error (Fixed)
print("\nExercise 4: Fixed Syntax Error")
print("Welcome to Python error fixing!")  # Fixed: Added missing quote
# --- End of Syntax Error ---

# Name Error (Fixed)
print("\nExercise 4: Fixed Name Error")
favorite_food = "Pizza"
print("My favorite food is", favorite_food)  # Fixed: Defined favorite_food
# --- End of Name Error ---

# Value Error (Fixed)
print("\nExercise 4: Fixed Value Error")
first_number = 12  # Fixed: Converted string to integer
second_number = 8
sum_result = first_number + second_number
print("The total sum is:", sum_result)
# --- End of Value Error ---

# Index Error (Fixed)
print("\nExercise 4: Fixed Index Error")
fruit_basket = ["apple", "banana", "cherry"]
print(fruit_basket[2])  # Fixed: Accessed index 2 instead of 3
# --- End of Index Error ---

# Indentation Error (Fixed)
print("\nExercise 4: Fixed Indentation Error")
current_hour = 15
if current_hour < 18:
    print("Good afternoon!")  # Fixed: Proper indentation
# --- End of Indentation Error ---