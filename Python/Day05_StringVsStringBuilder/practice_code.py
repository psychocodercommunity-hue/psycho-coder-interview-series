"""
Day 5: String vs StringBuilder - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with efficient string manipulation in Python
"""

import time
from io import StringIO
from typing import List, Iterator

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_concatenation():
    """Show basic string concatenation methods"""
    print("=== Basic Concatenation Demo ===")
    
    # Method 1: + operator
    result1 = "Hello" + " " + "World"
    print(f"+ operator: {result1}")
    
    # Method 2: join()
    words = ["Hello", "World"]
    result2 = " ".join(words)
    print(f"join(): {result2}")
    
    # Method 3: f-strings
    name = "Python"
    result3 = f"Hello, {name}!"
    print(f"f-string: {result3}")

def demonstrate_performance_difference():
    """Show performance difference between methods"""
    print("\n=== Performance Demo ===")
    
    items = [str(i) for i in range(1000)]
    
    # + operator
    start = time.time()
    result1 = ""
    for item in items:
        result1 += item
    time1 = time.time() - start
    
    # join()
    start = time.time()
    result2 = "".join(items)
    time2 = time.time() - start
    
    print(f"+ operator: {time1:.6f}s")
    print(f"join(): {time2:.6f}s")
    print(f"join() is {time1/time2:.1f}x faster")

def demonstrate_string_formatting():
    """Show different string formatting methods"""
    print("\n=== String Formatting Demo ===")
    
    name = "Alice"
    age = 30
    score = 95.5
    
    # % formatting
    message1 = "Hello, %s! You are %d years old with score %.1f" % (name, age, score)
    print(f"% formatting: {message1}")
    
    # .format()
    message2 = "Hello, {}! You are {} years old with score {:.1f}".format(name, age, score)
    print(f".format(): {message2}")
    
    # f-strings
    message3 = f"Hello, {name}! You are {age} years old with score {score:.1f}"
    print(f"f-string: {message3}")

def demonstrate_stringio():
    """Show StringIO usage"""
    print("\n=== StringIO Demo ===")
    
    buffer = StringIO()
    buffer.write("Hello, ")
    buffer.write("World!")
    buffer.write("\nThis is a new line.")
    
    result = buffer.getvalue()
    print(f"StringIO result: {repr(result)}")

# =============================================================================
# EXERCISE 1: Basic String Operations
# =============================================================================

def exercise_1_concatenation_methods():
    """
    TODO: Practice different string concatenation methods
    
    Instructions:
    1. Create a list of strings
    2. Concatenate them using + operator
    3. Concatenate them using join()
    4. Compare the results and performance
    5. Explain when to use each method
    """
    # Your code here
    pass

def exercise_1_string_formatting():
    """
    TODO: Practice different string formatting methods
    
    Instructions:
    1. Create variables for name, age, and score
    2. Format them using % formatting
    3. Format them using .format()
    4. Format them using f-strings
    5. Compare the readability and performance
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Performance Analysis
# =============================================================================

def exercise_2_performance_comparison():
    """
    TODO: Compare performance of different string methods
    
    Instructions:
    1. Create a large list of strings
    2. Test + operator concatenation
    3. Test join() concatenation
    4. Test StringIO concatenation
    5. Measure and compare execution times
    """
    # Your code here
    pass

def exercise_2_memory_usage():
    """
    TODO: Analyze memory usage of string operations
    
    Instructions:
    1. Create large strings using different methods
    2. Measure memory usage with sys.getsizeof()
    3. Compare memory efficiency
    4. Identify the most memory-efficient method
    5. Create a memory usage report
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 3: Advanced String Building
# =============================================================================

def exercise_3_custom_string_builder():
    """
    TODO: Create a custom string builder class
    
    Instructions:
    1. Create a StringBuilder class
    2. Implement append() and append_line() methods
    3. Implement a build() method to get the final string
    4. Test your implementation
    5. Compare with built-in methods
    """
    # Your code here
    pass

def exercise_3_lazy_string_building():
    """
    TODO: Implement lazy string building
    
    Instructions:
    1. Create a class that builds strings only when needed
    2. Implement methods to add strings
    3. Implement a method to get the final string
    4. Test with large amounts of data
    5. Measure performance improvements
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: String Processing
# =============================================================================

def exercise_4_text_processing():
    """
    TODO: Process text data efficiently
    
    Instructions:
    1. Create a function that processes a list of text lines
    2. Use efficient string methods for cleaning and formatting
    3. Implement text filtering and transformation
    4. Use generators for memory efficiency
    5. Test with large text data
    """
    # Your code here
    pass

def exercise_4_template_system():
    """
    TODO: Create a template system for string generation
    
    Instructions:
    1. Create a template class that can substitute variables
    2. Implement validation for required variables
    3. Support different data types
    4. Create a template for a common use case (e.g., email)
    5. Test your template system
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_high_performance_builder():
    """
    PRO TASK: Create a high-performance string builder
    
    Instructions:
    1. Create a string builder optimized for performance
    2. Implement chunked processing for large datasets
    3. Add memory management features
    4. Implement thread-safe operations
    5. Create performance benchmarks
    """
    # Your code here
    pass

def pro_task_string_optimization():
    """
    PRO TASK: Optimize string operations for specific use cases
    
    Instructions:
    1. Create optimized string operations for common patterns
    2. Implement caching for frequently used strings
    3. Add support for different encodings
    4. Create a string optimization framework
    5. Test with real-world data
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 5: String vs StringBuilder Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_concatenation()
    demonstrate_performance_difference()
    demonstrate_string_formatting()
    demonstrate_stringio()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_concatenation_methods()
    # exercise_1_string_formatting()
    # exercise_2_performance_comparison()
    # exercise_2_memory_usage()
    # exercise_3_custom_string_builder()
    # exercise_3_lazy_string_building()
    # exercise_4_text_processing()
    # exercise_4_template_system()
    # pro_task_high_performance_builder()
    # pro_task_string_optimization()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")
    print("💬 Comment 'Day 5' on our social media for the solution!")
