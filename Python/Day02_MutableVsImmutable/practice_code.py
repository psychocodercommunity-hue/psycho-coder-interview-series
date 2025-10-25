"""
Day 2: Mutable vs Immutable - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with mutable and immutable objects in Python
"""

import sys
import time
import copy
from typing import List, Dict, Any

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_differences():
    """Show basic differences between mutable and immutable objects"""
    print("=== Basic Differences Demo ===")
    
    # Immutable objects
    x = 5
    y = x
    print(f"x = {x}, y = {y}")
    y = 10
    print(f"After y = 10: x = {x}, y = {y}")
    
    # Mutable objects
    list1 = [1, 2, 3]
    list2 = list1
    print(f"list1 = {list1}, list2 = {list2}")
    list2.append(4)
    print(f"After list2.append(4): list1 = {list1}, list2 = {list2}")

def demonstrate_memory_behavior():
    """Show how Python handles memory for different object types"""
    print("\n=== Memory Behavior Demo ===")
    
    # Integer caching
    small_int1 = 100
    small_int2 = 100
    large_int1 = 1000
    large_int2 = 1000
    
    print(f"Small ints (100): {small_int1 is small_int2}")
    print(f"Large ints (1000): {large_int1 is large_int2}")
    
    # String interning
    str1 = "hello"
    str2 = "hello"
    print(f"Simple strings: {str1 is str2}")
    
    # Mutable objects
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"Lists with same content: {list1 is list2}")

def demonstrate_function_parameters():
    """Show how mutable and immutable objects behave as function parameters"""
    print("\n=== Function Parameters Demo ===")
    
    def modify_immutable(x):
        x = x + 1
        print(f"Inside function (immutable): {x}")
    
    def modify_mutable(lst):
        lst.append(4)
        print(f"Inside function (mutable): {lst}")
    
    # Test with immutable
    num = 5
    print(f"Before (immutable): {num}")
    modify_immutable(num)
    print(f"After (immutable): {num}")
    
    # Test with mutable
    my_list = [1, 2, 3]
    print(f"Before (mutable): {my_list}")
    modify_mutable(my_list)
    print(f"After (mutable): {my_list}")

def demonstrate_copying():
    """Show different types of copying"""
    print("\n=== Copying Demo ===")
    
    original = [1, 2, [3, 4]]
    
    # Shallow copy
    shallow = copy.copy(original)
    shallow[2].append(5)
    
    # Deep copy
    deep = copy.deepcopy(original)
    deep[2].append(6)
    
    print(f"Original: {original}")
    print(f"Shallow copy: {shallow}")
    print(f"Deep copy: {deep}")

# =============================================================================
# EXERCISE 1: Basic Mutability
# =============================================================================

def exercise_1_immutable_behavior():
    """
    TODO: Demonstrate immutable object behavior
    
    Instructions:
    1. Create two variables with the same integer value
    2. Check if they are the same object using 'is'
    3. Try to modify one and show it doesn't affect the other
    4. Do the same with strings
    5. Print the results with explanations
    """
    # Your code here
    pass

def exercise_1_mutable_behavior():
    """
    TODO: Demonstrate mutable object behavior
    
    Instructions:
    1. Create two lists with the same content
    2. Check if they are the same object using 'is'
    3. Modify one list and show it doesn't affect the other
    4. Create a reference to the first list and modify it
    5. Show how the original list is affected
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Function Parameters
# =============================================================================

def exercise_2_immutable_parameters():
    """
    TODO: Create functions that demonstrate immutable parameter behavior
    
    Instructions:
    1. Create a function that takes an integer parameter
    2. Try to modify the parameter inside the function
    3. Show that the original value is unchanged
    4. Do the same with a string parameter
    5. Explain why this happens
    """
    # Your code here
    pass

def exercise_2_mutable_parameters():
    """
    TODO: Create functions that demonstrate mutable parameter behavior
    
    Instructions:
    1. Create a function that takes a list parameter
    2. Modify the list inside the function
    3. Show that the original list is changed
    4. Create a version that doesn't modify the original
    5. Compare the two approaches
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Copying and References
# =============================================================================

def exercise_3_shallow_vs_deep_copy():
    """
    TODO: Demonstrate shallow vs deep copying
    
    Instructions:
    1. Create a nested list (list containing other lists)
    2. Create a shallow copy and a deep copy
    3. Modify the nested elements in both copies
    4. Show how the original list is affected
    5. Explain the difference between shallow and deep copy
    """
    # Your code here
    pass

def exercise_3_reference_tracking():
    """
    TODO: Track object references and memory usage
    
    Instructions:
    1. Create a large list and measure its memory usage
    2. Create multiple references to the same list
    3. Measure memory usage after creating references
    4. Create a copy of the list and measure memory again
    5. Explain the memory implications
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: Common Pitfalls
# =============================================================================

def exercise_4_mutable_default_arguments():
    """
    TODO: Demonstrate the mutable default argument pitfall
    
    Instructions:
    1. Create a function with a mutable default argument (list)
    2. Call the function multiple times
    3. Show how the default argument accumulates values
    4. Create a corrected version using None as default
    5. Compare the behavior of both versions
    """
    # Your code here
    pass

def exercise_4_tuple_with_mutable_elements():
    """
    TODO: Show that tuples can contain mutable elements
    
    Instructions:
    1. Create a tuple containing a list
    2. Try to modify the list inside the tuple
    3. Show that this is possible
    4. Explain why this works
    5. Discuss the implications for immutability
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_memory_optimization():
    """
    PRO TASK: Implement memory optimization patterns
    
    Instructions:
    1. Create a class with __slots__ to optimize memory
    2. Compare memory usage with a regular class
    3. Create a function that uses generators for large datasets
    4. Measure memory usage for different approaches
    5. Create a report with recommendations
    """
    # Your code here
    pass

def pro_task_performance_analysis():
    """
    PRO TASK: Analyze performance implications of mutability
    
    Instructions:
    1. Compare string concatenation vs list concatenation
    2. Measure time for different approaches
    3. Test with different data sizes
    4. Create a performance benchmark
    5. Provide optimization recommendations
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 2: Mutable vs Immutable Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_differences()
    demonstrate_memory_behavior()
    demonstrate_function_parameters()
    demonstrate_copying()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_immutable_behavior()
    # exercise_1_mutable_behavior()
    # exercise_2_immutable_parameters()
    # exercise_2_mutable_parameters()
    # exercise_3_shallow_vs_deep_copy()
    # exercise_3_reference_tracking()
    # exercise_4_mutable_default_arguments()
    # exercise_4_tuple_with_mutable_elements()
    # pro_task_memory_optimization()
    # pro_task_performance_analysis()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")