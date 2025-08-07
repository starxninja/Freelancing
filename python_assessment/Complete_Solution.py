# Complete Solution for Python Programming Assignment
# Question 1: Data Analysis Tasks

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Set style for better plots
plt.style.use('default')
sns.set_palette("husl")

print("=" * 60)
print("QUESTION 1: DATA ANALYSIS TASKS")
print("=" * 60)

# Task 1: Load the CSV dataset and create a dataframe
print("\nTask 1: Load the CSV dataset and create a dataframe")
df = pd.read_csv('sample_data.csv')
print("Dataset loaded successfully!")
print(f"Dataset shape: {df.shape}")

# Task 2: Print the whole dataset
print("\nTask 2: Print the whole dataset")
print(df)

# Task 3: Calculate how many records are in the dataset
print("\nTask 3: Calculate how many records are in the dataset")
num_records = len(df)
print(f"Number of records in the dataset: {num_records}")

# Task 4: Find missing values and fill them
print("\nTask 4: Find missing values and fill them")
print("Missing values in each column:")
print(df.isnull().sum())

# Fill missing values with mean of respective columns
df_filled = df.copy()
for column in df_filled.columns:
    if df_filled[column].dtype in ['int64', 'float64']:
        mean_value = df_filled[column].mean()
        df_filled[column].fillna(mean_value, inplace=True)

print("\nUpdated dataset after filling missing values:")
print(df_filled.head(10))

# Task 5: Mean and standard deviation of Age
print("\nTask 5: Mean and standard deviation of Age")
age_mean = df_filled['Age'].mean()
age_std = df_filled['Age'].std()
print(f"Mean Age: {age_mean:.2f}")
print(f"Standard Deviation of Age: {age_std:.2f}")

# Task 6: Highest and lowest Salary
print("\nTask 6: Highest and lowest Salary")
max_salary = df_filled['Salary'].max()
min_salary = df_filled['Salary'].min()
print(f"Highest Salary: ${max_salary:,.2f}")
print(f"Lowest Salary: ${min_salary:,.2f}")

# Task 7: Average salary by age groups
print("\nTask 7: Average salary by age groups")
age_groups = {
    '18-30': df_filled[(df_filled['Age'] >= 18) & (df_filled['Age'] <= 30)]['Salary'].mean(),
    '31-40': df_filled[(df_filled['Age'] >= 31) & (df_filled['Age'] <= 40)]['Salary'].mean(),
    '41-50': df_filled[(df_filled['Age'] >= 41) & (df_filled['Age'] <= 50)]['Salary'].mean(),
    '51-60': df_filled[(df_filled['Age'] >= 51) & (df_filled['Age'] <= 60)]['Salary'].mean()
}

print("Average Salary by Age Groups:")
for group, avg_salary in age_groups.items():
    print(f"{group}: ${avg_salary:,.2f}")

# Task 8: Correlation between Experience and Salary
print("\nTask 8: Correlation between Experience and Salary")
correlation = df_filled['Experience'].corr(df_filled['Salary'])
print(f"Correlation between Experience and Salary: {correlation:.4f}")

# Task 9: Histogram of Rating
print("\nTask 9: Histogram of Rating")
plt.figure(figsize=(10, 6))
plt.hist(df_filled['Rating'], bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Ratings')
plt.grid(True, alpha=0.3)
plt.show()

# Task 10: Individuals with more than 10 years experience
print("\nTask 10: Individuals with more than 10 years experience")
high_experience_count = len(df_filled[df_filled['Experience'] > 10])
print(f"Number of individuals with more than 10 years experience: {high_experience_count}")

# Task 11: Scatter plot of Age vs Salary
print("\nTask 11: Scatter plot of Age vs Salary")
plt.figure(figsize=(10, 6))
plt.scatter(df_filled['Age'], df_filled['Salary'], alpha=0.6, color='blue')
plt.xlabel('Age')
plt.ylabel('Salary ($)')
plt.title('Age vs Salary Scatter Plot')
plt.grid(True, alpha=0.3)
plt.show()

# Task 12: Percentage with salary above 50,000
print("\nTask 12: Percentage with salary above 50,000")
high_salary_count = len(df_filled[df_filled['Salary'] > 50000])
percentage = (high_salary_count / len(df_filled)) * 100
print(f"Percentage of individuals with salary above $50,000: {percentage:.2f}%")

# Task 13: Bar chart of Experience years
print("\nTask 13: Bar chart of Experience years")
experience_counts = df_filled['Experience'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
plt.bar(experience_counts.index, experience_counts.values, color='skyblue', edgecolor='black')
plt.xlabel('Years of Experience')
plt.ylabel('Number of Individuals')
plt.title('Distribution of Experience Years')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.show()

# Task 14: Rating with highest average salary
print("\nTask 14: Rating with highest average salary")
rating_salary_avg = df_filled.groupby('Rating')['Salary'].mean()
highest_avg_rating = rating_salary_avg.idxmax()
highest_avg_salary = rating_salary_avg.max()
print(f"Rating with highest average salary: {highest_avg_rating}")
print(f"Average salary for this rating: ${highest_avg_salary:,.2f}")

# Task 15: Check for duplicate rows
print("\nTask 15: Check for duplicate rows")
initial_rows = len(df_filled)
duplicate_count = df_filled.duplicated().sum()

if duplicate_count > 0:
    df_clean = df_filled.drop_duplicates()
    removed_rows = initial_rows - len(df_clean)
    print(f"Found {duplicate_count} duplicate rows")
    print(f"Removed {removed_rows} rows")
else:
    df_clean = df_filled.copy()
    print("No duplicate rows found")

# Task 16: Normalize Salary column
print("\nTask 16: Normalize Salary column")
scaler = MinMaxScaler()
df_clean['Salary_Normalized'] = scaler.fit_transform(df_clean[['Salary']])
print("Salary column normalized (0 to 1):")
print(f"Min normalized salary: {df_clean['Salary_Normalized'].min():.4f}")
print(f"Max normalized salary: {df_clean['Salary_Normalized'].max():.4f}")

# Task 17: Create Age Group column
print("\nTask 17: Create Age Group column")
def categorize_age(age):
    if 18 <= age <= 30:
        return 'Young'
    elif 31 <= age <= 50:
        return 'Middle-Aged'
    elif 51 <= age <= 60:
        return 'Senior'
    else:
        return 'Other'

df_clean['Age_Group'] = df_clean['Age'].apply(categorize_age)
print("Age Group distribution:")
print(df_clean['Age_Group'].value_counts())

print("\n" + "=" * 60)
print("QUESTION 2: LINEAR ALGEBRA OPERATIONS")
print("=" * 60)

# Question 2: Linear Algebra Operations
import numpy as np

# Task 1: Add two matrices function
def add_two_matrices(matrix1, matrix2):
    """Add two matrices and return the sum"""
    return np.array(matrix1) + np.array(matrix2)

# Task 2: Matrix determinant function
def matrix_determinant(matrix=None):
    """Calculate determinant of a matrix, default is 3x3 identity matrix"""
    if matrix is None:
        matrix = np.eye(3)
    return np.linalg.det(matrix)

# Task 3: Inverse matrix function
def inverse_matrix(matrix):
    """Calculate inverse of a matrix"""
    det = np.linalg.det(matrix)
    if det == 0:
        print("Matrix non invertible")
        return None
    else:
        return np.linalg.inv(matrix)

# Task 4: Multiply matrices function
def multiply_matrices(matrix1, matrix2):
    """Multiply two matrices"""
    try:
        return np.dot(matrix1, matrix2)
    except ValueError:
        print("Matrix multiplication is not possible")
        return None

# Task 5: Matrix transpose function
def matrix_transpose(matrix):
    """Calculate transpose of a matrix"""
    return np.transpose(matrix)

# Define the matrices
Mat1 = np.array([[4, 7, 2], [3, 5, 8], [6, 1, 9]])
Mat2 = np.array([[1, 8, 3], [4, 2, 6], [7, 9, 5]])

print("Mat1:")
print(Mat1)
print("\nMat2:")
print(Mat2)

# Task 6: Add matrices
print("\nTask 6: Add Mat1 and Mat2")
result_add = add_two_matrices(Mat1, Mat2)
print("Result:")
print(result_add)

# Task 7: Determinant of Mat1
print("\nTask 7: Determinant of Mat1")
det_result = matrix_determinant(Mat1)
print(f"Determinant: {det_result:.2f}")

# Task 8: Multiply Mat1 and Mat2
print("\nTask 8: Multiply Mat1 and Mat2")
mult_result = multiply_matrices(Mat1, Mat2)
print("Result:")
print(mult_result)

# Task 9: Inverse of Mat1
print("\nTask 9: Inverse of Mat1")
inv_result = inverse_matrix(Mat1)
if inv_result is not None:
    print("Inverse:")
    print(inv_result)
    
    # Verify by multiplying with original
    verify = np.dot(Mat1, inv_result)
    print("\nVerification (should be identity matrix):")
    print(verify)

# Task 10: Transpose of Mat1
print("\nTask 10: Transpose of Mat1")
transpose_result = matrix_transpose(Mat1)
print("Transpose:")
print(transpose_result)

# Verify transpose of transpose equals original
transpose_twice = matrix_transpose(transpose_result)
print("\nTranspose of transpose (should equal original):")
print(transpose_twice)
print("\nOriginal matrix:")
print(Mat1)

print("\n" + "=" * 60)
print("QUESTION 3: VECTOR OPERATIONS")
print("=" * 60)

# Question 3: Vector Operations
import numpy as np
import matplotlib.pyplot as plt

# Define vectors
vector1 = np.array([-1, 4])  # (-1i, 4j)
vector2 = np.array([5, 3])   # (5i, 3j)

print("Vector1:", vector1)
print("Vector2:", vector2)

# Task 1: Add vectors
print("\nTask 1: Add vector1 and vector2")
vector_sum = vector1 + vector2
print(f"Result: {vector_sum}")

# Task 2: Find norms (magnitudes)
print("\nTask 2: Find norms of vectors")
norm1 = np.linalg.norm(vector1)
norm2 = np.linalg.norm(vector2)
print(f"Norm of vector1: {norm1:.4f}")
print(f"Norm of vector2: {norm2:.4f}")

# Task 3: Dot product
print("\nTask 3: Calculate dot product")
dot_product = np.dot(vector1, vector2)
print(f"Dot product: {dot_product}")

# Task 4: Angle between vectors
print("\nTask 4: Angle between vectors")
cos_angle = dot_product / (norm1 * norm2)
angle_rad = np.arccos(np.clip(cos_angle, -1.0, 1.0))
angle_deg = np.degrees(angle_rad)
print(f"Angle in radians: {angle_rad:.4f}")
print(f"Angle in degrees: {angle_deg:.2f}")

# Task 5: Plot vectors
print("\nTask 5: Plot vectors")
plt.figure(figsize=(10, 8))
plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Vector1')
plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector2')
plt.quiver(0, 0, vector_sum[0], vector_sum[1], angles='xy', scale_units='xy', scale=1, color='green', label='Sum')

plt.xlim(-2, 6)
plt.ylim(-1, 8)
plt.grid(True)
plt.legend()
plt.title('Vector Visualization')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()

print("\n" + "=" * 60)
print("QUESTION 4: STUDENT CLASS")
print("=" * 60)

# Question 4: Student Class
class Student:
    def __init__(self, student_id, first_name, last_name, year_of_birth, course):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.course = course

# Task 1: Create Student class (already done above)
print("Task 1: Student class created with attributes: student_id, first_name, last_name, year_of_birth, course")

# Task 2: Create object with your details
print("\nTask 2: Create student object")
student = Student("12345", "John", "Doe", 2000, "Computer Science")
print("Student object created successfully")

# Task 3: Print object attributes
print("\nTask 3: Print object attributes")
print(f"Student ID: {student.student_id}")
print(f"First Name: {student.first_name}")
print(f"Last Name: {student.last_name}")
print(f"Year of Birth: {student.year_of_birth}")
print(f"Course: {student.course}")

print("\n" + "=" * 60)
print("QUESTION 5: LINEAR EQUATIONS AND STATISTICAL ANALYSIS")
print("=" * 60)

# Question 5: Linear Equations and Statistical Analysis
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Task 1: Solve system of linear equations
print("Task 1: Solve system of linear equations")
# x + 2y = 3
# 4x + 5y = 6

A = np.array([[1, 2], [4, 5]])
b = np.array([3, 6])

solution = np.linalg.solve(A, b)
print(f"x = {solution[0]:.4f}")
print(f"y = {solution[1]:.4f}")

# Task 2: Generate normal distribution samples
print("\nTask 2: Generate normal distribution samples")
normal_samples = np.random.normal(10, 10, 1000)
print(f"Generated {len(normal_samples)} samples from normal distribution")

# Task 3: Calculate statistics
print("\nTask 3: Calculate statistics")
mean_val = np.mean(normal_samples)
median_val = np.median(normal_samples)
std_val = np.std(normal_samples)
print(f"Mean: {mean_val:.4f}")
print(f"Median: {median_val:.4f}")
print(f"Standard Deviation: {std_val:.4f}")

# Task 4: Plot histogram
print("\nTask 4: Plot histogram")
plt.figure(figsize=(10, 6))
plt.hist(normal_samples, bins=30, density=True, alpha=0.7, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram of Normal Distribution Samples')
plt.grid(True, alpha=0.3)
plt.show()

# Task 5: Plot probability density function with seaborn
print("\nTask 5: Plot probability density function")
plt.figure(figsize=(10, 6))
sns.kdeplot(normal_samples, fill=True)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Probability Density Function of Normal Distribution')
plt.grid(True, alpha=0.3)
plt.show()

# Task 6: Create pie chart
print("\nTask 6: Create pie chart")
threshold = mean_val + std_val
above_threshold = len(normal_samples[normal_samples > threshold])
below_threshold = len(normal_samples[normal_samples <= threshold])

plt.figure(figsize=(8, 8))
sizes = [above_threshold, below_threshold]
labels = ['Above Threshold', 'Below Threshold']
colors = ['#ff9999', '#66b3ff']
explode = (0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Distribution Above/Below Threshold (Mean + Std)')
plt.axis('equal')
plt.show()

# Task 7: Generate uniform distribution samples
print("\nTask 7: Generate uniform distribution samples")
uniform_samples = np.random.uniform(-1, 1, 500)
print(f"Generated {len(uniform_samples)} samples from uniform distribution")

# Task 8: Count numbers between 0 and 0.5
print("\nTask 8: Count numbers between 0 and 0.5")
count_between = len(uniform_samples[(uniform_samples >= 0) & (uniform_samples <= 0.5)])
print(f"Numbers between 0 and 0.5: {count_between}")

# Task 9: Plot uniform distribution PDF
print("\nTask 9: Plot uniform distribution PDF")
plt.figure(figsize=(10, 6))
sns.kdeplot(uniform_samples, fill=True)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Probability Density Function of Uniform Distribution')
plt.grid(True, alpha=0.3)
plt.show()

print("\n" + "=" * 60)
print("ALL TASKS COMPLETED SUCCESSFULLY!")
print("=" * 60) 