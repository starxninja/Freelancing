# COMP11124 Object Oriented Programming - Week 1 Practical Lab Exercises

# Exercise 1: Variables and Types

# Boolean variable indicating if a user is active
is_user_active = True
# Integer variable representing a student's age
student_age_years = 42
# Float variable for the value of pi
math_pi_value = 3.14
# String variable for a welcome message
welcome_message_text = "Hello World"

# Print types to verify guesses
print("Exercise 1: Variables and Types")
print(f"Type of is_user_active: {type(is_user_active)}")
print(f"Type of student_age_years: {type(student_age_years)}")
print(f"Type of math_pi_value: {type(math_pi_value)}")
print(f"Type of welcome_message_text: {type(welcome_message_text)}")

# Casting variables
integer_example = 5
float_example = 5.5
boolean_example = True

print(f"integer_example: {integer_example}")
print(f"float_example: {float_example}")
print(f"boolean_example: {boolean_example}") 

# Casting to different types
integer_to_float = float(integer_example)
float_to_integer = int(float_example)
boolean_to_integer = int(boolean_example)

print("\nCasting Results:")
print(f"integer to float: {integer_to_float}")
print(f"float to integer: {float_to_integer}")
print(f"boolean to integer: {boolean_to_integer}")

print("\n" + "-"*50 + " End of Exercise 1 " + "-"*50 + "\n")

# Exercise 2: Arithmetic Operators
print("\nExercise 2: Arithmetic Operators")
addition_result = 10 + 5
print("Addition:", addition_result)
subtraction_result = 20 - 8
print("Subtraction:", subtraction_result)
multiplication_result = 6 * 4
print("Multiplication:", multiplication_result)
division_result = 15 / 3
print("Division:", division_result)
floor_division_result = 17 // 4
print("Floor Division:", floor_division_result)
modulus_result = 17 % 4
print("Modulus:", modulus_result)
exponentiation_result = 2 ** 3
print("Exponentiation:", exponentiation_result)

# Calculating the Average of two test scores
math_test_score = 25
science_test_score = 75
average_test_score = (math_test_score + science_test_score) / 2
print(f"\nAverage of {math_test_score} and {science_test_score} is: {average_test_score}")

# Calculate the Area and Perimeter of a Rectangle
rectangle_length_cm = 10
rectangle_width_cm = 5
rectangle_area_sqcm = rectangle_length_cm * rectangle_width_cm
rectangle_perimeter_cm = 2 * (rectangle_length_cm + rectangle_width_cm)
print(f"Rectangle with length {rectangle_length_cm}cm and width {rectangle_width_cm}cm has area: {rectangle_area_sqcm} square cm")
print(f"Perimeter of rectangle: {rectangle_perimeter_cm} cm")

# Calculate the area of a triangle
triangle_base_cm = 8
triangle_height_cm = 6
triangle_area_sqcm = 0.5 * triangle_base_cm * triangle_height_cm
print(f"Area of triangle with base {triangle_base_cm}cm and height {triangle_height_cm}cm: {triangle_area_sqcm} square cm")

print("\n" + "-"*50 + " End of Exercise 2 " + "-"*50 + "\n")

# Exercise 3: Strings and f-Strings
print("\nExercise 3: Strings and f-Strings")
course_description_text = "This class covers OOP."
print(f"Original string: {course_description_text}")

uppercase_description = course_description_text.upper()
lowercase_description = course_description_text.lower()
replaced_description = course_description_text.replace("OOP", "Object Oriented Programming")
description_length = len(course_description_text)

print(f"Uppercase: {uppercase_description}")
print(f"Lowercase: {lowercase_description}")
print(f"Replaced: {replaced_description}")
print(f"Length: {description_length}")

# f-String Task
student_name = "Peter"
number_of_classes = 10
campus_location = "Paisley"
introduction_text = f"My name is {student_name} and I am studying {number_of_classes} classes in {campus_location}"
print(introduction_text)

print("\n" + "-"*50 + " End of Exercise 3 " + "-"*50 + "\n")

# Exercise 4: Temperature Converter
print("\nExercise 4: Temperature Converter")
celsius_temperature = 25  # Example input
degrees_fahrenheit = (celsius_temperature * 9/5) + 32  # Celsius to Fahrenheit
degrees_kelvin = celsius_temperature + 273.15     # Celsius to Kelvin

print("Welcome to the Temperature Converter!")
print(f"The temperature you have entered is {celsius_temperature} degree Celsius.")
print("\nConverted Temperatures:")
print(f"{celsius_temperature} degree Celsius is equal to {degrees_fahrenheit} Fahrenheit.")
print(f"{celsius_temperature} degree Celsius is equal to {degrees_kelvin} Kelvin.")
print("\nThank you for using the Temperature Converter!")

print("\n" + "-"*50 + " End of Exercise 4 " + "-"*50 + "\n")