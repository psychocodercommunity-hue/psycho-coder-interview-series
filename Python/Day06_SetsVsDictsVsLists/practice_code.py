"""
Day 6: Sets vs Dicts vs Lists - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with Python data structures
"""

import time
import sys
from collections import defaultdict, Counter
from typing import List, Dict, Set, Any

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_usage():
    """Show basic usage of lists, sets, and dictionaries"""
    print("=== Basic Usage Demo ===")
    
    # List - ordered, allows duplicates
    my_list = [1, 2, 3, 2, 1]
    print(f"List: {my_list}")
    
    # Dictionary - key-value pairs
    my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
    print(f"Dictionary: {my_dict}")
    print(f"Name: {my_dict['name']}")
    
    # Set - unique elements only
    my_set = {1, 2, 3, 2, 1}
    print(f"Set: {my_set}")

def demonstrate_performance_differences():
    """Show performance differences between data structures"""
    print("\n=== Performance Demo ===")
    
    # Test data
    size = 10000
    test_data = list(range(size))
    
    # Membership testing
    target = size // 2
    
    # List membership (O(n))
    start = time.time()
    result1 = target in test_data
    list_time = time.time() - start
    
    # Set membership (O(1))
    test_set = set(test_data)
    start = time.time()
    result2 = target in test_set
    set_time = time.time() - start
    
    # Dict membership (O(1))
    test_dict = {i: i for i in test_data}
    start = time.time()
    result3 = target in test_dict
    dict_time = time.time() - start
    
    print(f"List membership: {list_time:.6f}s")
    print(f"Set membership: {set_time:.6f}s")
    print(f"Dict membership: {dict_time:.6f}s")
    print(f"Set is {list_time/set_time:.1f}x faster than list")

def demonstrate_common_operations():
    """Show common operations for each data structure"""
    print("\n=== Common Operations Demo ===")
    
    # List operations
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)
    my_list.insert(0, 0)
    my_list.remove(3)
    print(f"List after operations: {my_list}")
    
    # Set operations
    my_set = {1, 2, 3, 4, 5}
    my_set.add(6)
    my_set.remove(3)
    my_set.union({7, 8})
    print(f"Set after operations: {my_set}")
    
    # Dictionary operations
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict['d'] = 4
    del my_dict['a']
    print(f"Dict after operations: {my_dict}")

def demonstrate_use_cases():
    """Show real-world use cases"""
    print("\n=== Use Cases Demo ===")
    
    # List: Shopping cart with duplicates
    shopping_cart = ['apple', 'banana', 'apple', 'orange']
    print(f"Shopping cart: {shopping_cart}")
    print(f"Total items: {len(shopping_cart)}")
    
    # Set: Unique items
    unique_items = set(shopping_cart)
    print(f"Unique items: {unique_items}")
    
    # Dictionary: Inventory
    inventory = {'apple': 10, 'banana': 5, 'orange': 8}
    print(f"Inventory: {inventory}")
    print(f"Apples in stock: {inventory['apple']}")

# =============================================================================
# EXERCISE 1: Basic Operations
# =============================================================================

def exercise_1_data_structure_creation():
    """
    TODO: Create and manipulate different data structures
    
    Instructions:
    1. Create a list with some duplicate elements
    2. Create a set from the list and show the difference
    3. Create a dictionary with the unique elements as keys
    4. Perform basic operations on each structure
    5. Compare the results
    """
    # Your code here
    pass

def exercise_1_membership_testing():
    """
    TODO: Test membership in different data structures
    
    Instructions:
    1. Create a large list, set, and dictionary
    2. Test membership for different elements
    3. Measure the time for each test
    4. Compare the performance
    5. Explain the differences
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Performance Analysis
# =============================================================================

def exercise_2_performance_comparison():
    """
    TODO: Compare performance of different operations
    
    Instructions:
    1. Create large data structures (list, set, dict)
    2. Test different operations (add, remove, lookup)
    3. Measure execution time for each operation
    4. Create a performance report
    5. Identify the most efficient structure for each operation
    """
    # Your code here
    pass

def exercise_2_memory_usage():
    """
    TODO: Analyze memory usage of different data structures
    
    Instructions:
    1. Create data structures with the same data
    2. Measure memory usage with sys.getsizeof()
    3. Compare memory efficiency
    4. Test with different data sizes
    5. Create a memory usage report
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Advanced Operations
# =============================================================================

def exercise_3_set_operations():
    """
    TODO: Practice set operations
    
    Instructions:
    1. Create two sets with some common elements
    2. Perform union, intersection, and difference operations
    3. Test subset and superset relationships
    4. Use set operations to solve a problem
    5. Compare with list-based solutions
    """
    # Your code here
    pass

def exercise_3_dictionary_operations():
    """
    TODO: Practice advanced dictionary operations
    
    Instructions:
    1. Create a dictionary with nested data
    2. Use defaultdict for automatic key creation
    3. Use Counter for frequency counting
    4. Implement a simple cache using dictionary
    5. Test your implementations
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: Real-World Applications
# =============================================================================

def exercise_4_data_processing():
    """
    TODO: Process data using appropriate data structures
    
    Instructions:
    1. Create a dataset with duplicate values
    2. Use sets to find unique values
    3. Use dictionaries to count frequencies
    4. Use lists to maintain order
    5. Implement a data processing pipeline
    """
    # Your code here
    pass

def exercise_4_algorithm_optimization():
    """
    TODO: Optimize algorithms using appropriate data structures
    
    Instructions:
    1. Implement a function to find duplicates using lists
    2. Implement the same function using sets
    3. Compare the performance
    4. Implement a function to find common elements
    5. Optimize using appropriate data structures
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_custom_data_structure():
    """
    PRO TASK: Create a custom data structure
    
    Instructions:
    1. Create a class that combines the benefits of list, set, and dict
    2. Implement efficient operations for your use case
    3. Add methods for common operations
    4. Test your implementation
    5. Compare with built-in data structures
    """
    # Your code here
    pass

def pro_task_performance_optimization():
    """
    PRO TASK: Optimize a real-world problem
    
    Instructions:
    1. Choose a real-world problem (e.g., social media analytics)
    2. Implement a solution using appropriate data structures
    3. Optimize for performance and memory usage
    4. Test with large datasets
    5. Create a performance benchmark
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 6: Sets vs Dicts vs Lists Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_usage()
    demonstrate_performance_differences()
    demonstrate_common_operations()
    demonstrate_use_cases()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_data_structure_creation()
    # exercise_1_membership_testing()
    # exercise_2_performance_comparison()
    # exercise_2_memory_usage()
    # exercise_3_set_operations()
    # exercise_3_dictionary_operations()
    # exercise_4_data_processing()
    # exercise_4_algorithm_optimization()
    # pro_task_custom_data_structure()
    # pro_task_performance_optimization()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")
