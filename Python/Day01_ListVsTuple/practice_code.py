"""
Day 1: List vs Tuple - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with lists and tuples including performance analysis
"""

import sys
import time
from collections import namedtuple
from typing import List, Tuple, Union, Optional

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_differences():
    """Show basic differences between lists and tuples"""
    print("=== Basic Differences Demo ===")
    
    # List - mutable
    my_list = [1, 2, 3]
    print(f"Original list: {my_list}")
    my_list.append(4)
    my_list[0] = 10
    print(f"Modified list: {my_list}")
    
    # Tuple - immutable
    my_tuple = (1, 2, 3)
    print(f"Original tuple: {my_tuple}")
    # my_tuple.append(4)  # This would cause an error
    # my_tuple[0] = 10    # This would also cause an error
    print(f"Tuple remains: {my_tuple}")

def demonstrate_memory_usage():
    """Compare memory usage between lists and tuples"""
    print("\n=== Memory Usage Comparison ===")
    
    # Small collections
    small_list = [1, 2, 3, 4, 5]
    small_tuple = (1, 2, 3, 4, 5)
    
    print(f"Small list: {sys.getsizeof(small_list)} bytes")
    print(f"Small tuple: {sys.getsizeof(small_tuple)} bytes")
    
    # Large collections
    large_list = list(range(1000))
    large_tuple = tuple(range(1000))
    
    print(f"Large list: {sys.getsizeof(large_list)} bytes")
    print(f"Large tuple: {sys.getsizeof(large_tuple)} bytes")
    
    # Memory efficiency ratio
    ratio = sys.getsizeof(large_list) / sys.getsizeof(large_tuple)
    print(f"Memory efficiency: Tuple uses {ratio:.2f}x less memory")

def demonstrate_performance():
    """Compare performance between lists and tuples"""
    print("\n=== Performance Comparison ===")
    
    # Test data size
    size = 100000
    
    # List performance
    start_time = time.time()
    my_list = [i for i in range(size)]
    list_creation_time = time.time() - start_time
    
    start_time = time.time()
    for item in my_list:
        pass  # Just iterate
    list_iteration_time = time.time() - start_time
    
    # Tuple performance
    start_time = time.time()
    my_tuple = tuple(i for i in range(size))
    tuple_creation_time = time.time() - start_time
    
    start_time = time.time()
    for item in my_tuple:
        pass  # Just iterate
    tuple_iteration_time = time.time() - start_time
    
    print(f"List creation time: {list_creation_time:.6f}s")
    print(f"Tuple creation time: {tuple_creation_time:.6f}s")
    print(f"List iteration time: {list_iteration_time:.6f}s")
    print(f"Tuple iteration time: {tuple_iteration_time:.6f}s")
    
    # Performance improvement
    if list_iteration_time > 0:
        improvement = (list_iteration_time - tuple_iteration_time) / list_iteration_time * 100
        print(f"Tuple iteration is {improvement:.1f}% faster")

def demonstrate_use_cases():
    """Show real-world use cases for lists and tuples"""
    print("\n=== Real-World Use Cases ===")
    
    # Tuple for fixed data (coordinates, database records)
    coordinates = (10, 20)
    person_record = ("John", 25, "Engineer", "New York")
    
    print(f"Coordinates: {coordinates}")
    print(f"Person record: {person_record}")
    
    # Tuple unpacking
    x, y = coordinates
    name, age, job, city = person_record
    print(f"X: {x}, Y: {y}")
    print(f"Name: {name}, Age: {age}, Job: {job}, City: {city}")
    
    # List for dynamic data
    shopping_cart = []
    shopping_cart.append("Laptop")
    shopping_cart.extend(["Mouse", "Keyboard"])
    print(f"Shopping cart: {shopping_cart}")
    
    # Dictionary with tuple keys
    locations = {
        (0, 0): "Origin",
        (10, 20): "Point A",
        (30, 40): "Point B"
    }
    print(f"Locations: {locations}")

def demonstrate_advanced_patterns():
    """Show advanced patterns with named tuples and type hints"""
    print("\n=== Advanced Patterns ===")
    
    # Named tuples
    Person = namedtuple('Person', ['name', 'age', 'email'])
    person = Person("Alice", 30, "alice@example.com")
    print(f"Person: {person.name}, {person.age}, {person.email}")
    
    # Type hints with tuples
    def get_coordinates() -> Tuple[float, float]:
        return (10.5, 20.3)
    
    def process_users(users: List[Tuple[str, int]]) -> List[str]:
        return [name for name, age in users if age >= 18]
    
    # Test the functions
    coords = get_coordinates()
    print(f"Coordinates: {coords}")
    
    users = [("John", 25), ("Jane", 17), ("Bob", 30)]
    adults = process_users(users)
    print(f"Adult users: {adults}")

# =============================================================================
# EXERCISE 1: Basic Operations
# =============================================================================

def exercise_1_list_operations():
    """
    TODO: Create a list and perform various operations
    
    Instructions:
    1. Create a list with numbers 1-5
    2. Add number 6 to the end
    3. Insert number 0 at the beginning
    4. Remove the number 3
    5. Print the final list and its length
    """
    # Your code here
    pass

def exercise_1_tuple_operations():
    """
    TODO: Create a tuple and demonstrate immutability
    
    Instructions:
    1. Create a tuple with numbers 1-5
    2. Try to add number 6 (this will fail - catch the error)
    3. Try to change the first element (this will fail - catch the error)
    4. Print appropriate error messages
    5. Show that you can still access elements
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Performance Analysis
# =============================================================================

def exercise_2_memory_analysis():
    """
    TODO: Create a comprehensive memory analysis
    
    Instructions:
    1. Create lists and tuples of different sizes (10, 100, 1000, 10000)
    2. Measure memory usage for each
    3. Calculate the memory efficiency ratio
    4. Create a summary report
    """
    # Your code here
    pass

def exercise_2_performance_benchmark():
    """
    TODO: Create a performance benchmark
    
    Instructions:
    1. Create large lists and tuples (100,000+ elements)
    2. Measure creation time, access time, and iteration time
    3. Compare the results
    4. Identify which operations are faster for each type
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Real-World Applications
# =============================================================================

def exercise_3_function_returns():
    """
    TODO: Create functions that return multiple values using tuples
    
    Instructions:
    1. Create a function that calculates area and perimeter of a rectangle
    2. Create a function that returns min, max, and average of a list
    3. Use tuple unpacking to get the results
    4. Print the results in a formatted way
    """
    # Your code here
    pass

def exercise_3_data_structures():
    """
    TODO: Create a student database using tuples and lists
    
    Instructions:
    1. Create a list of student tuples (name, age, grade)
    2. Add at least 5 students
    3. Find the student with the highest grade
    4. Calculate the average grade
    5. Print all students' information in a table format
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_named_tuples():
    """
    PRO TASK: Implement a more advanced solution using named tuples
    
    Instructions:
    1. Create a Person named tuple with fields: name, age, email, department
    2. Create a list of Person objects
    3. Implement a function to find the oldest person
    4. Implement a function to filter people by department
    5. Implement a function to get average age by department
    """
    # Your code here
    pass

def pro_task_performance_optimization():
    """
    PRO TASK: Create a performance optimization analysis
    
    Instructions:
    1. Create a scenario where you need to store coordinates-
    2. Compare using lists vs tuples for 1 million coordinates
    3. Measure memory usage, creation time, and access time
    4. Create a detailed comparison report
    5. Recommend the best approach with justification
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 1: List vs Tuple Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_differences()
    demonstrate_memory_usage()
    demonstrate_performance()
    demonstrate_use_cases()
    demonstrate_advanced_patterns()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_list_operations()
    # exercise_1_tuple_operations()
    # exercise_2_memory_analysis()
    # exercise_2_performance_benchmark()
    # exercise_3_function_returns()
    # exercise_3_data_structures()
    # pro_task_named_tuples()
    # pro_task_performance_optimization()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")
