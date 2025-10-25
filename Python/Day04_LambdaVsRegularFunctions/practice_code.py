"""
Day 4: Lambda vs Regular Functions - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with lambda functions and regular functions
"""

import time
import sys
from functools import reduce, partial
from typing import List, Dict, Any, Callable

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_lambda():
    """Show basic lambda function usage"""
    print("=== Basic Lambda Demo ===")
    
    # Basic lambda function
    add = lambda x, y: x + y
    print(f"Add 5 + 3: {add(5, 3)}")
    
    # Lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared numbers: {squared}")
    
    # Lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")

def demonstrate_advanced_lambda():
    """Show advanced lambda usage patterns"""
    print("\n=== Advanced Lambda Demo ===")
    
    # Sorting with lambda
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78}
    ]
    
    sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
    print(f"Students by grade: {sorted_students}")
    
    # Lambda with reduce
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product of numbers: {product}")
    
    # Higher-order function with lambda
    def create_multiplier(factor):
        return lambda x: x * factor
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"Double 5: {double(5)}")
    print(f"Triple 5: {triple(5)}")

def demonstrate_performance():
    """Show performance comparison between lambda and regular functions"""
    print("\n=== Performance Demo ===")
    
    def regular_square(x):
        return x ** 2
    
    lambda_square = lambda x: x ** 2
    
    numbers = list(range(100000))
    
    # Regular function
    start = time.time()
    result1 = list(map(regular_square, numbers))
    regular_time = time.time() - start
    
    # Lambda function
    start = time.time()
    result2 = list(map(lambda_square, numbers))
    lambda_time = time.time() - start
    
    print(f"Regular function: {regular_time:.6f}s")
    print(f"Lambda function: {lambda_time:.6f}s")

def demonstrate_common_pitfalls():
    """Show common lambda pitfalls"""
    print("\n=== Common Pitfalls Demo ===")
    
    # Pitfall 1: Variable capture in loops
    functions = []
    for i in range(3):
        functions.append(lambda x: x + i)  # All capture the same 'i'
    
    print(f"Variable capture issue: {[f(0) for f in functions]}")
    
    # Solution: Use default parameter
    functions_fixed = []
    for i in range(3):
        functions_fixed.append(lambda x, i=i: x + i)  # Capture current value
    
    print(f"Fixed version: {[f(0) for f in functions_fixed]}")

# =============================================================================
# EXERCISE 1: Basic Lambda Operations
# =============================================================================

def exercise_1_basic_lambda():
    """
    TODO: Create basic lambda functions
    
    Instructions:
    1. Create a lambda function that doubles a number
    2. Create a lambda function that checks if a number is even
    3. Create a lambda function that concatenates two strings
    4. Test all functions with sample inputs
    5. Print the results
    """
    # Your code here
    pass

def exercise_1_lambda_with_builtins():
    """
    TODO: Use lambda functions with built-in functions
    
    Instructions:
    1. Use lambda with map() to square all numbers in a list
    2. Use lambda with filter() to get all positive numbers
    3. Use lambda with sorted() to sort a list of tuples by the second element
    4. Use lambda with reduce() to find the maximum number in a list
    5. Print all results
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Advanced Lambda Usage
# =============================================================================

def exercise_2_data_processing():
    """
    TODO: Use lambda functions for data processing
    
    Instructions:
    1. Create a list of dictionaries with student data (name, age, grade)
    2. Use lambda to filter students with grade >= 80
    3. Use lambda to sort students by age
    4. Use lambda to extract just the names of top 3 students
    5. Print the results
    """
    # Your code here
    pass

def exercise_2_functional_programming():
    """
    TODO: Implement functional programming patterns with lambda
    
    Instructions:
    1. Create a list of numbers
    2. Use lambda with map to apply a transformation (e.g., x*2 + 1)
    3. Use lambda with filter to keep only numbers > 10
    4. Use lambda with reduce to calculate the sum
    5. Chain these operations together
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Lambda vs Regular Functions
# =============================================================================

def exercise_3_performance_comparison():
    """
    TODO: Compare performance of lambda vs regular functions
    
    Instructions:
    1. Create a regular function that squares a number
    2. Create a lambda function that squares a number
    3. Test both with a large list of numbers
    4. Measure execution time for both approaches
    5. Compare memory usage
    6. Provide recommendations
    """
    # Your code here
    pass

def exercise_3_readability_analysis():
    """
    TODO: Analyze readability of lambda vs regular functions
    
    Instructions:
    1. Create a complex lambda expression (e.g., nested conditions)
    2. Rewrite it as a regular function
    3. Compare readability and maintainability
    4. Identify when to use each approach
    5. Provide guidelines for choosing between them
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: Common Pitfalls
# =============================================================================

def exercise_4_variable_capture():
    """
    TODO: Demonstrate and fix variable capture issues
    
    Instructions:
    1. Create a list of lambda functions in a loop
    2. Show the variable capture problem
    3. Implement the default parameter solution
    4. Implement the partial function solution
    5. Compare all approaches
    """
    # Your code here
    pass

def exercise_4_side_effects():
    """
    TODO: Handle side effects in lambda functions
    
    Instructions:
    1. Create a lambda function with side effects (e.g., printing)
    2. Show why this is problematic
    3. Rewrite using a regular function
    4. Create a better approach using functional programming
    5. Compare the approaches
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_lambda_decorators():
    """
    PRO TASK: Create decorators using lambda functions
    
    Instructions:
    1. Create a decorator that uses lambda functions
    2. Implement a retry decorator with lambda
    3. Create a timing decorator with lambda
    4. Test your decorators with sample functions
    5. Compare with regular decorator implementations
    """
    # Your code here
    pass

def pro_task_lambda_pipelines():
    """
    PRO TASK: Create data processing pipelines with lambda
    
    Instructions:
    1. Create a complex dataset (e.g., employee records)
    2. Build a processing pipeline using lambda functions
    3. Include filtering, transformation, and aggregation steps
    4. Make the pipeline reusable and configurable
    5. Add error handling and logging
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 4: Lambda vs Regular Functions Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_lambda()
    demonstrate_advanced_lambda()
    demonstrate_performance()
    demonstrate_common_pitfalls()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_basic_lambda()
    # exercise_1_lambda_with_builtins()
    # exercise_2_data_processing()
    # exercise_2_functional_programming()
    # exercise_3_performance_comparison()
    # exercise_3_readability_analysis()
    # exercise_4_variable_capture()
    # exercise_4_side_effects()
    # pro_task_lambda_decorators()
    # pro_task_lambda_pipelines()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")
    print("💬 Comment 'Day 4' on our social media for the solution!")
