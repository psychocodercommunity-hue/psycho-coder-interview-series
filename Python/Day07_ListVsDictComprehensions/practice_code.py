"""
Day 7: List vs Dict Comprehensions - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with Python comprehensions
"""

import time
from typing import List, Dict, Any, Tuple
from collections import defaultdict

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_comprehensions():
    """Show basic list and dictionary comprehensions"""
    print("=== Basic Comprehensions Demo ===")
    
    # List comprehension
    squares = [x**2 for x in range(5)]
    print(f"List comprehension: {squares}")
    
    # Dictionary comprehension
    square_dict = {x: x**2 for x in range(5)}
    print(f"Dict comprehension: {square_dict}")
    
    # With conditions
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")

def demonstrate_performance():
    """Show performance difference between loops and comprehensions"""
    print("\n=== Performance Demo ===")
    
    # Traditional loop
    start = time.time()
    result1 = []
    for i in range(10000):
        if i % 2 == 0:
            result1.append(i**2)
    loop_time = time.time() - start
    
    # List comprehension
    start = time.time()
    result2 = [i**2 for i in range(10000) if i % 2 == 0]
    comp_time = time.time() - start
    
    print(f"Loop time: {loop_time:.6f}s")
    print(f"Comprehension time: {comp_time:.6f}s")
    print(f"Comprehension is {loop_time/comp_time:.1f}x faster")

def demonstrate_advanced_patterns():
    """Show advanced comprehension patterns"""
    print("\n=== Advanced Patterns Demo ===")
    
    # Nested comprehensions
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for row in matrix for item in row]
    print(f"Flattened matrix: {flattened}")
    
    # Dictionary comprehension with conditions
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    filtered = {k: v for k, v in data.items() if v > 2}
    print(f"Filtered dict: {filtered}")
    
    # Multiple conditions
    result = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
    print(f"Multiple conditions: {result}")

def demonstrate_real_world_examples():
    """Show real-world examples"""
    print("\n=== Real-World Examples Demo ===")
    
    # Data processing
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78}
    ]
    
    # List comprehension
    names = [student['name'] for student in students]
    print(f"Student names: {names}")
    
    # Dictionary comprehension
    grade_dict = {student['name']: student['grade'] for student in students}
    print(f"Grade dictionary: {grade_dict}")

# =============================================================================
# EXERCISE 1: Basic Comprehensions
# =============================================================================

def exercise_1_list_comprehensions():
    """
    TODO: Practice basic list comprehensions
    
    Instructions:
    1. Create a list comprehension that squares all numbers from 0 to 9
    2. Create a list comprehension that gets only even numbers from 0 to 19
    3. Create a list comprehension that gets squares of even numbers
    4. Create a list comprehension that gets numbers divisible by 3 or 5
    5. Test all your comprehensions
    """
    # Your code here
    pass

def exercise_1_dict_comprehensions():
    """
    TODO: Practice basic dictionary comprehensions
    
    Instructions:
    1. Create a dictionary comprehension that maps numbers to their squares
    2. Create a dictionary comprehension that maps words to their lengths
    3. Create a dictionary comprehension that filters a dictionary by value
    4. Create a dictionary comprehension that transforms keys and values
    5. Test all your comprehensions
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Advanced Patterns
# =============================================================================

def exercise_2_nested_comprehensions():
    """
    TODO: Practice nested comprehensions
    
    Instructions:
    1. Create a nested list comprehension to flatten a 2D list
    2. Create a nested list comprehension to transpose a matrix
    3. Create a nested dictionary comprehension for grouped data
    4. Create a comprehension with multiple conditions
    5. Test all your comprehensions
    """
    # Your code here
    pass

def exercise_2_complex_transformations():
    """
    TODO: Practice complex data transformations
    
    Instructions:
    1. Create a list of dictionaries with student data
    2. Use comprehensions to extract specific information
    3. Use comprehensions to filter and transform data
    4. Use comprehensions to create summary statistics
    5. Test your transformations
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Performance Analysis
# =============================================================================

def exercise_3_performance_comparison():
    """
    TODO: Compare performance of different approaches
    
    Instructions:
    1. Create a large dataset
    2. Implement the same logic using loops and comprehensions
    3. Measure execution time for each approach
    4. Compare memory usage
    5. Create a performance report
    """
    # Your code here
    pass

def exercise_3_memory_efficiency():
    """
    TODO: Analyze memory efficiency of comprehensions
    
    Instructions:
    1. Create large datasets using different methods
    2. Measure memory usage with sys.getsizeof()
    3. Compare list comprehensions vs generator expressions
    4. Test with different data sizes
    5. Create a memory usage report
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: Real-World Applications
# =============================================================================

def exercise_4_data_processing():
    """
    TODO: Process real-world data using comprehensions
    
    Instructions:
    1. Create a dataset representing sales data
    2. Use comprehensions to filter and analyze data
    3. Create summary statistics using comprehensions
    4. Implement data cleaning using comprehensions
    5. Test your data processing pipeline
    """
    # Your code here
    pass

def exercise_4_text_processing():
    """
    TODO: Process text data using comprehensions
    
    Instructions:
    1. Create a text processing function using comprehensions
    2. Implement word frequency counting
    3. Implement text filtering and transformation
    4. Create a text analysis pipeline
    5. Test with sample text data
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_comprehension_optimization():
    """
    PRO TASK: Optimize comprehensions for performance
    
    Instructions:
    1. Create a complex data processing task
    2. Implement it using different comprehension approaches
    3. Optimize for performance and memory usage
    4. Create benchmarks for different approaches
    5. Document best practices
    """
    # Your code here
    pass

def pro_task_custom_comprehensions():
    """
    PRO TASK: Create custom comprehension-like functionality
    
    Instructions:
    1. Create a class that supports comprehension-like syntax
    2. Implement filtering and transformation methods
    3. Add support for nested operations
    4. Test your implementation
    5. Compare with built-in comprehensions
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 7: List vs Dict Comprehensions Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_comprehensions()
    demonstrate_performance()
    demonstrate_advanced_patterns()
    demonstrate_real_world_examples()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_list_comprehensions()
    # exercise_1_dict_comprehensions()
    # exercise_2_nested_comprehensions()
    # exercise_2_complex_transformations()
    # exercise_3_performance_comparison()
    # exercise_3_memory_efficiency()
    # exercise_4_data_processing()
    # exercise_4_text_processing()
    # pro_task_comprehension_optimization()
    # pro_task_custom_comprehensions()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")
 