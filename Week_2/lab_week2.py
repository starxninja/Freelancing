# COMP11124 Object Oriented Programming - Week 2 Practical Lab Exercises

# =========================
# 1. Comparisons and Conditionals
# =========================

# -------- Exercise 1: Comparison Operators --------
print("Exercise 1: Comparison Operators")
comparison_flag = True  # Boolean flag for demonstration
is_five_greater_than_four = 5 > 4  # Result of comparison
print("is_five_greater_than_four (5 > 4):", is_five_greater_than_four)
first_value = 10
second_value = 20
print("first_value == second_value:", first_value == second_value)  # False
print("first_value != second_value:", first_value != second_value)  # True
print("first_value <= second_value:", first_value <= second_value)  # True
print("first_value >= second_value:", first_value >= second_value)  # False
# -------- End of Exercise 1 --------

# -------- Exercise 2: Logical Operators --------
print("\nExercise 2: Logical Operators")
user_age = 25
is_in_20s = user_age > 20 and user_age < 30
print("Is user age between 20 and 30?:", is_in_20s)  # True
is_not_teenager = not (user_age >= 13 and user_age <= 19)
print("Is not a teenager?:", is_not_teenager)  # True
is_adult_or_senior_citizen = user_age >= 18 or user_age > 65
print("Is adult or senior citizen?:", is_adult_or_senior_citizen)  # True
# -------- End of Exercise 2 --------

# -------- Exercise 3: if - Conditionals --------
print("\nExercise 3: if - Conditionals")
current_age = 19
current_age_group = "child"
if current_age > 18:
    current_age_group = "adult"
print(f"The age group is {current_age_group}")  # adult

current_age = 17  # Test with age below 18
current_age_group = "child"
if current_age > 18:
    current_age_group = "adult"
print(f"The age group is {current_age_group}")  # child
# -------- End of Exercise 3 --------

# -------- Exercise 4: if - else Conditionals --------
print("\nExercise 4: if - else Conditionals")
current_wind_speed = 30
if current_wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")  # windy

current_wind_speed = 5  # Test with wind speed below 10
if current_wind_speed < 10:
    print("It is a calm day")  # calm
else:
    print("It is a windy day")
# -------- End of Exercise 4 --------

# -------- Exercise 5: if - elif - else Conditionals --------
print("\nExercise 5: if - elif - else Conditionals")
exam_grade = 55
if exam_grade < 50:
    print("You failed")
elif exam_grade < 60:
    print("You passed")  # passed
elif exam_grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")
# -------- End of Exercise 5 --------

# -------- Exercise 6: Compare Temperatures --------
print("\nExercise 6: Compare Temperatures")
first_temperature = 22.5
second_temperature = 22.5
if first_temperature == second_temperature:
    print("The temperatures are equal")
else:
    print("The temperatures are not equal")  # equal

first_temperature = 22.5
second_temperature = 25.0
if first_temperature == second_temperature:
    print("The temperatures are equal")
else:
    print("The temperatures are not equal")  # not equal
# -------- End of Exercise 6 --------

# =========================
# 2. Python Lists
# =========================

# -------- Exercise 1: Creating a List --------
print("\nExercise 1: Creating a List")
uk_cities = ["Glasgow", "London", "Edinburgh"]
print("uk_cities:", uk_cities)
# -------- End of Exercise 1 --------

# -------- Exercise 2: Accessing a List --------
print("\nExercise 2: Accessing a List")
print("Third item in uk_cities:", uk_cities[2])  # Edinburgh
print("Last two items in uk_cities:", uk_cities[-2:])  # ['London', 'Edinburgh']
# -------- End of Exercise 2 --------

# -------- Exercise 3: Modifying a List --------
print("\nExercise 3: Modifying a List")
uk_cities.append("Manchester")
print("After appending Manchester:", uk_cities)
uk_cities[1] = "Birmingham"
print("After changing second item to Birmingham:", uk_cities)
# -------- End of Exercise 3 --------

# -------- Exercise 4: Summary Task - Create, Access, and Modify Lists --------
print("\nExercise 4: Create, Access, and Modify Lists")
colour_palette = ["blue", "green", "yellow"]
print("Original colour_palette:", colour_palette)
print("Second element:", colour_palette[1])  # green
colour_palette[0] = "red"
print("Modified colour_palette:", colour_palette)
print("Length of colour_palette:", len(colour_palette))
if "red" in colour_palette:
    print("Red is in the list")
selected_colours = colour_palette[1:3]
print("Selected colours (second and third):", selected_colours)
# -------- End of Exercise 4 --------

# =========================
# 3. Python Loops
# =========================

# -------- Exercise 1: While Loops --------
print("\nExercise 1: While Loops")
loop_counter = 0
while loop_counter < 5:
    print(loop_counter)
    loop_counter += 1
# -------- End of Exercise 1 --------

# -------- Exercise 2: For Loops --------
print("\nExercise 2: For Loops")
for city_name in uk_cities:
    print(city_name)
# -------- End of Exercise 2 --------

# -------- Exercise 3: Loop Keywords - Range, break, and continue --------
print("\nExercise 3: Loop Keywords")
for range_index in range(5):
    if range_index == 3:
        break
    print(range_index)

print("Using continue to skip 2:")
for range_index in range(5):
    if range_index == 2:
        continue
    print(range_index)
# -------- End of Exercise 3 --------

# -------- Exercise 4: Summary Tasks --------
# Task - Even Numbers
print("\nExercise 4: Even Numbers")
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
for number in number_list:
    if number % 2 == 0:
        print(number)

# Task - Sum of Squares
print("\nExercise 4: Sum of Squares")
squares_total = 0
for square_index in range(1, 6):
    squares_total += square_index ** 2
print("Sum of squares (1 to 5):", squares_total)  # 55

# Task - Countdown
print("\nExercise 4: Countdown")
countdown_value = 10
while countdown_value >= 1:
    print(countdown_value)
    countdown_value -= 1
print("Liftoff!")
# -------- End of Exercise 4 --------

# =========================
# 4. Obtaining User Input
# =========================

# -------- Task: User Input and Conditional Statements --------
print("\nTask: User Input and Conditional Statements")
user_input_age = int(input("Enter your age: "))
if user_input_age < 18:
    print("You are a minor.")
elif 18 <= user_input_age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# -------- End of Task --------

# -------- Task: Temperature Converter --------
print("\nTask: Temperature Converter")
input_temp_type = input("Enter temperature unit (C, F, K): ").upper()
input_temp_value = float(input("Enter temperature value: "))

if input_temp_type == "C":
    temp_in_fahrenheit = (input_temp_value * 9/5) + 32
    temp_in_kelvin = input_temp_value + 273.15
    print(f"\nWelcome to the Temperature Converter!")
    print(f"The temperature you entered is {input_temp_value}°C.")
    print(f"Converted Temperatures:")
    print(f"{input_temp_value}°C is equal to {temp_in_fahrenheit}°F.")
    print(f"{input_temp_value}°C is equal to {temp_in_kelvin}K.")
elif input_temp_type == "F":
    temp_in_celsius = (input_temp_value - 32) * 5/9
    temp_in_kelvin = temp_in_celsius + 273.15
    print(f"\nWelcome to the Temperature Converter!")
    print(f"The temperature you entered is {input_temp_value}°F.")
    print(f"Converted Temperatures:")
    print(f"{input_temp_value}°F is equal to {temp_in_celsius}°C.")
    print(f"{input_temp_value}°F is equal to {temp_in_kelvin}K.")
elif input_temp_type == "K":
    temp_in_celsius = input_temp_value - 273.15
    temp_in_fahrenheit = (temp_in_celsius * 9/5) + 32
    print(f"\nWelcome to the Temperature Converter!")
    print(f"The temperature you entered is {input_temp_value}K.")
    print(f"Converted Temperatures:")
    print(f"{input_temp_value}K is equal to {temp_in_celsius}°C.")
    print(f"{input_temp_value}K is equal to {temp_in_fahrenheit}°F.")
else:
    print("Invalid temperature unit. Please enter C, F, or K.")
print("\nThank you for using the Temperature Converter!")
# -------- End of Task --------