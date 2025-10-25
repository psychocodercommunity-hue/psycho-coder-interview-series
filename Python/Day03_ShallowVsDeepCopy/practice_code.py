"""
Day 3: Shallow vs Deep Copy - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with Python's copy mechanisms
"""

import copy
import time
import sys
from typing import List, Dict, Any

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_copying():
    """Show basic shallow vs deep copy behavior"""
    print("=== Basic Copying Demo ===")
    
    original = [1, 2, [3, 4]]
    
    # Shallow copy
    shallow = copy.copy(original)
    shallow[2].append(5)  # Modifies the original!
    
    # Deep copy
    deep = copy.deepcopy(original)
    deep[2].append(6)  # Doesn't modify the original
    
    print(f"Original: {original}")
    print(f"Shallow: {shallow}")
    print(f"Deep: {deep}")

def demonstrate_nested_structures():
    """Show copying behavior with nested structures"""
    print("\n=== Nested Structures Demo ===")
    
    original = {
        'name': 'John',
        'scores': [85, 90, 78],
        'address': {
            'street': '123 Main St',
            'city': 'New York'
        }
    }
    
    # Shallow copy
    shallow = copy.copy(original)
    shallow['scores'].append(95)  # Modifies original!
    shallow['address']['city'] = 'Boston'  # Modifies original!
    
    # Deep copy
    deep = copy.deepcopy(original)
    deep['scores'].append(88)  # Doesn't modify original
    deep['address']['city'] = 'Chicago'  # Doesn't modify original
    
    print(f"Original: {original}")
    print(f"Shallow: {shallow}")
    print(f"Deep: {deep}")

def demonstrate_performance():
    """Show performance differences between copy types"""
    print("\n=== Performance Demo ===")
    
    # Large nested structure
    large_data = {
        'items': [{'id': i, 'data': list(range(100))} for i in range(1000)]
    }
    
    # Time shallow copy
    start = time.time()
    shallow_copy = copy.copy(large_data)
    shallow_time = time.time() - start
    
    # Time deep copy
    start = time.time()
    deep_copy = copy.deepcopy(large_data)
    deep_time = time.time() - start
    
    print(f"Shallow copy time: {shallow_time:.6f}s")
    print(f"Deep copy time: {deep_time:.6f}s")
    print(f"Deep copy is {deep_time/shallow_time:.1f}x slower")

def demonstrate_object_identity():
    """Show object identity differences"""
    print("\n=== Object Identity Demo ===")
    
    original = [1, [2, 3], {'a': 4}]
    
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    
    print(f"Original is shallow: {original is shallow}")
    print(f"Original is deep: {original is deep}")
    print(f"Original[1] is shallow[1]: {original[1] is shallow[1]}")
    print(f"Original[1] is deep[1]: {original[1] is deep[1]}")
    print(f"Original[2] is shallow[2]: {original[2] is shallow[2]}")
    print(f"Original[2] is deep[2]: {original[2] is deep[2]}")

# =============================================================================
# EXERCISE 1: Basic Copy Operations
# =============================================================================

def exercise_1_simple_copying():
    """
    TODO: Practice basic copy operations
    
    Instructions:
    1. Create a list with nested elements
    2. Create both shallow and deep copies
    3. Modify the nested elements in both copies
    4. Show how the original list is affected
    5. Explain the differences
    """
    # Your code here
    pass

def exercise_1_copy_methods():
    """
    TODO: Explore different copy methods
    
    Instructions:
    1. Create a list and try different copy methods:
       - list.copy()
       - list[:]
       - copy.copy()
       - copy.deepcopy()
    2. Test with nested structures
    3. Show which methods create shallow vs deep copies
    4. Compare the results
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Complex Data Structures
# =============================================================================

def exercise_2_dictionary_copying():
    """
    TODO: Practice copying dictionaries with nested data
    
    Instructions:
    1. Create a dictionary with nested lists and dictionaries
    2. Create shallow and deep copies
    3. Modify nested elements in both copies
    4. Show how the original dictionary is affected
    5. Create a function that safely modifies a copy
    """
    # Your code here
    pass

def exercise_2_list_of_objects():
    """
    TODO: Work with lists containing objects
    
    Instructions:
    1. Create a simple class with mutable attributes
    2. Create a list of instances of this class
    3. Create shallow and deep copies of the list
    4. Modify the objects in both copies
    5. Show how the original objects are affected
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Performance Analysis
# =============================================================================

def exercise_3_performance_comparison():
    """
    TODO: Compare performance of different copy methods
    
    Instructions:
    1. Create data structures of different sizes
    2. Measure time for shallow vs deep copy
    3. Test with different nesting levels
    4. Create a performance report
    5. Identify when each method is most appropriate
    """
    # Your code here
    pass

def exercise_3_memory_usage():
    """
    TODO: Analyze memory usage of copy operations
    
    Instructions:
    1. Create large data structures
    2. Measure memory usage before and after copying
    3. Compare memory usage between shallow and deep copies
    4. Use sys.getsizeof() to measure memory
    5. Create a memory usage report
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: Common Pitfalls
# =============================================================================

def exercise_4_copy_pitfalls():
    """
    TODO: Demonstrate common copy-related pitfalls
    
    Instructions:
    1. Create a function that unintentionally modifies original data
    2. Show how shallow copy can cause bugs
    3. Create a corrected version using deep copy
    4. Test both versions and compare results
    5. Explain how to avoid these pitfalls
    """
    # Your code here
    pass

def exercise_4_circular_references():
    """
    TODO: Handle circular references in copying
    
    Instructions:
    1. Create objects with circular references
    2. Try to create deep copies
    3. Handle any errors that occur
    4. Implement a solution for circular references
    5. Test your solution
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_custom_copy():
    """
    PRO TASK: Implement custom copy behavior
    
    Instructions:
    1. Create a class with custom __copy__ and __deepcopy__ methods
    2. Implement different copy behaviors for different attributes
    3. Test your custom copy implementation
    4. Compare with default copy behavior
    5. Document when to use custom copy methods
    """
    # Your code here
    pass

def pro_task_copy_optimization():
    """
    PRO TASK: Optimize copy operations for performance
    
    Instructions:
    1. Create a data structure that's expensive to copy
    2. Implement lazy copying (copy only when needed)
    3. Implement selective copying (copy only specific parts)
    4. Measure performance improvements
    5. Create a copy optimization framework
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 3: Shallow vs Deep Copy Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_copying()
    demonstrate_nested_structures()
    demonstrate_performance()
    demonstrate_object_identity()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_simple_copying()
    # exercise_1_copy_methods()
    # exercise_2_dictionary_copying()
    # exercise_2_list_of_objects()
    # exercise_3_performance_comparison()
    # exercise_3_memory_usage()
    # exercise_4_copy_pitfalls()
    # exercise_4_circular_references()
    # pro_task_custom_copy()
    # pro_task_copy_optimization()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")
    print("💬 Comment 'Day 3' on our social media for the solution!")