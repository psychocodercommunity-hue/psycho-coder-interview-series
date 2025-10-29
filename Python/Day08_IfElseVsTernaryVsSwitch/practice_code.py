"""
Day 8: If/Else vs Ternary vs Switch - Practice Exercises
Psycho Coder Interview Series

Hands-on practice with Python control flow

Note: Match statements require Python 3.10+. 
The code includes fallbacks for older Python versions.
"""

import time
import sys
from typing import Callable, Any, Dict

# Check Python version for match statements
if sys.version_info < (3, 10):
    print("⚠️  Warning: Match statements require Python 3.10+. Using fallback implementations.")
    print("   Upgrade to Python 3.10+ for full match statement support.\n")

# =============================================================================
# EXAMPLE EXPLANATION CODE
# =============================================================================

def demonstrate_basic_control_flow():
    """Show basic control flow patterns"""
    print("=== Basic Control Flow Demo ===")
    
    # If/else statement
    age = 18
    if age >= 18:
        status = "adult"
    else:
        status = "minor"
    print(f"If/else: {status}")
    
    # Ternary operator
    status = "adult" if age >= 18 else "minor"
    print(f"Ternary: {status}")
    
    # Switch-like behavior
    day = "Monday"
    if day == "Monday":
        message = "Start of work week"
    elif day == "Friday":
        message = "TGIF!"
    elif day == "Saturday" or day == "Sunday":
        message = "Weekend!"
    else:
        message = "Regular day"
    print(f"Switch-like: {message}")
    
    # Match statement (Python 3.10+) with fallback
    day = "Monday"
    if sys.version_info >= (3, 10):
        match day:
            case "Monday":
                message = "Start of work week"
            case "Friday":
                message = "TGIF!"
            case "Saturday" | "Sunday":
                message = "Weekend!"
            case _:
                message = "Regular day"
    else:
        # Fallback for Python < 3.10
        if day == "Monday":
            message = "Start of work week"
        elif day == "Friday":
            message = "TGIF!"
        elif day in ("Saturday", "Sunday"):
            message = "Weekend!"
        else:
            message = "Regular day"
    print(f"Match statement: {message}")

def demonstrate_performance():
    """Show performance differences"""
    print("\n=== Performance Demo ===")
    
    test_values = [1, 2, 3, 4, 5] * 1000
    
    # If/else
    start = time.time()
    result1 = []
    for x in test_values:
        if x == 1:
            result1.append("one")
        elif x == 2:
            result1.append("two")
        elif x == 3:
            result1.append("three")
        else:
            result1.append("other")
    if_time = time.time() - start
    
    # Ternary
    start = time.time()
    result2 = ["one" if x == 1 else "two" if x == 2 else "three" if x == 3 else "other" for x in test_values]
    ternary_time = time.time() - start
    
    # Dictionary lookup
    start = time.time()
    mapping = {1: "one", 2: "two", 3: "three"}
    result3 = [mapping.get(x, "other") for x in test_values]
    dict_time = time.time() - start
    
    # Match statement (Python 3.10+) with fallback
    def match_value(x):
        if sys.version_info >= (3, 10):
            match x:
                case 1:
                    return "one"
                case 2:
                    return "two"
                case 3:
                    return "three"
                case _:
                    return "other"
        else:
            # Fallback for Python < 3.10
            if x == 1:
                return "one"
            elif x == 2:
                return "two"
            elif x == 3:
                return "three"
            else:
                return "other"
    
    start = time.time()
    result4 = [match_value(x) for x in test_values]
    match_time = time.time() - start
    
    print(f"If/else time: {if_time:.6f}s")
    print(f"Ternary time: {ternary_time:.6f}s")
    print(f"Dictionary time: {dict_time:.6f}s")
    print(f"Match time: {match_time:.6f}s")

def demonstrate_advanced_patterns():
    """Show advanced control flow patterns"""
    print("\n=== Advanced Patterns Demo ===")
    
    # Nested ternary
    score = 85
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    print(f"Nested ternary: {grade}")
    
    # Function-based switch
    def handle_monday():
        return "Start of work week"
    
    def handle_friday():
        return "TGIF!"
    
    def handle_weekend():
        return "Weekend!"
    
    def handle_default():
        return "Regular day"
    
    day_handlers = {
        "Monday": handle_monday,
        "Friday": handle_friday,
        "Saturday": handle_weekend,
        "Sunday": handle_weekend
    }
    
    def get_day_message(day):
        handler = day_handlers.get(day, handle_default)
        return handler()
    
    print(f"Function-based switch: {get_day_message('Monday')}")
    
    # Match statement with pattern matching
    def get_day_message_match(day):
        match day:
            case "Monday":
                return "Start of work week"
            case "Friday":
                return "TGIF!"
            case "Saturday" | "Sunday":
                return "Weekend!"
            case _:
                return "Regular day"
    
    print(f"Match statement: {get_day_message_match('Monday')}")
    
    # Advanced match patterns
    def process_data(data):
        match data:
            case [x, y]:
                return f"Two elements: {x}, {y}"
            case [x, y, z]:
                return f"Three elements: {x}, {y}, {z}"
            case [x, *rest]:
                return f"First element: {x}, rest: {rest}"
            case {"name": name, "age": age}:
                return f"Person: {name}, age {age}"
            case _:
                return "Unknown data structure"
    
    print(f"Match pattern [1, 2]: {process_data([1, 2])}")
    print(f"Match pattern [1, 2, 3, 4]: {process_data([1, 2, 3, 4])}")
    print(f"Match pattern dict: {process_data({'name': 'Alice', 'age': 30})}")
    
    # Advanced match with guard clauses
    def process_number(x):
        match x:
            case n if n < 0:
                return "Negative number"
            case 0:
                return "Zero"
            case n if n > 0 and n < 10:
                return "Single digit positive"
            case n if n >= 10 and n < 100:
                return "Double digit positive"
            case _:
                return "Large number"
    
    print(f"Number -5: {process_number(-5)}")
    print(f"Number 0: {process_number(0)}")
    print(f"Number 7: {process_number(7)}")
    print(f"Number 42: {process_number(42)}")
    
    # Match with class patterns
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class Circle:
        def __init__(self, center, radius):
            self.center = center
            self.radius = radius
    
    def describe_shape(shape):
        match shape:
            case Point(x, y):
                return f"Point at ({x}, {y})"
            case Circle(Point(x, y), radius):
                return f"Circle centered at ({x}, {y}) with radius {radius}"
            case _:
                return "Unknown shape"
    
    point = Point(3, 4)
    circle = Circle(Point(0, 0), 5)
    print(f"Point: {describe_shape(point)}")
    print(f"Circle: {describe_shape(circle)}")

def demonstrate_real_world_examples():
    """Show real-world examples"""
    print("\n=== Real-World Examples Demo ===")
    
    # Multiple conditions
    def get_discount(customer_type, order_amount):
        if customer_type == "premium" and order_amount > 100:
            return 0.15
        elif customer_type == "premium" or order_amount > 200:
            return 0.10
        elif customer_type == "regular" and order_amount > 50:
            return 0.05
        else:
            return 0.0
    
    discount = get_discount("premium", 150)
    print(f"Discount: {discount}")
    
    # Match statement for business logic
    def process_order(order):
        match order:
            case {"type": "standard", "amount": amount} if amount < 100:
                return f"Standard order: ${amount}, shipping: $5"
            case {"type": "standard", "amount": amount} if amount >= 100:
                return f"Standard order: ${amount}, free shipping"
            case {"type": "premium", "amount": amount}:
                return f"Premium order: ${amount}, free shipping + priority"
            case {"type": "express", "amount": amount}:
                return f"Express order: ${amount}, next-day delivery"
            case _:
                return "Unknown order type"
    
    order1 = {"type": "standard", "amount": 50}
    order2 = {"type": "premium", "amount": 200}
    print(f"Order 1: {process_order(order1)}")
    print(f"Order 2: {process_order(order2)}")

# =============================================================================
# EXERCISE 1: Basic Control Flow
# =============================================================================

def exercise_1_if_else_statements():
    """
    TODO: Practice if/else statements
    
    Instructions:
    1. Create a function that determines if a number is positive, negative, or zero
    2. Create a function that determines the grade based on a score
    3. Create a function that determines if a year is a leap year
    4. Create a function that determines the season based on a month
    5. Test all your functions
    """
    # Your code here
    pass

def exercise_1_ternary_operators():
    """
    TODO: Practice ternary operators
    
    Instructions:
    1. Convert simple if/else statements to ternary operators
    2. Create a function that returns the maximum of two numbers using ternary
    3. Create a function that returns the absolute value using ternary
    4. Create a function that determines if a number is even or odd using ternary
    5. Test all your functions
    """
    # Your code here
    pass

def exercise_1_match_statements():
    """
    TODO: Practice match statements (Python 3.10+)
    
    Instructions:
    1. Create a function that uses match to process different data types
    2. Create a function that uses match with guard clauses
    3. Create a function that uses match to process nested data structures
    4. Create a function that uses match to handle different HTTP responses
    5. Test all your functions
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 2: Switch-Like Behavior
# =============================================================================

def exercise_2_switch_implementation():
    """
    TODO: Implement switch-like behavior
    
    Instructions:
    1. Create a function that handles different HTTP status codes
    2. Create a function that handles different file extensions
    3. Create a function that handles different user roles
    4. Use both if/elif/else and dictionary approaches
    5. Compare the approaches
    """
    # Your code here
    pass

def exercise_2_advanced_switch():
    """
    TODO: Create advanced switch-like functionality
    
    Instructions:
    1. Create a class that implements switch-like behavior
    2. Add support for default cases
    3. Add support for multiple values per case
    4. Add support for range-based cases
    5. Test your implementation
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
    1. Create a large dataset for testing
    2. Implement the same logic using different approaches
    3. Measure execution time for each approach
    4. Compare memory usage
    5. Create a performance report
    """
    # Your code here
    pass

def exercise_3_optimization():
    """
    TODO: Optimize control flow for performance
    
    Instructions:
    1. Identify performance bottlenecks in control flow
    2. Implement optimizations
    3. Measure performance improvements
    4. Test with different data sizes
    5. Document optimization techniques
    """
    # Your code here
    pass

# =============================================================================
# EXERCISE 4: Real-World Applications
# =============================================================================

def exercise_4_business_logic():
    """
    TODO: Implement business logic using control flow
    
    Instructions:
    1. Create a function that calculates shipping costs
    2. Create a function that determines user permissions
    3. Create a function that processes different order types
    4. Create a function that handles different payment methods
    5. Test your business logic
    """
    # Your code here
    pass

def exercise_4_error_handling():
    """
    TODO: Implement error handling using control flow
    
    Instructions:
    1. Create a function that validates user input
    2. Create a function that handles different error types
    3. Create a function that implements retry logic
    4. Create a function that handles different file operations
    5. Test your error handling
    """
    # Your code here
    pass

# =============================================================================
# PRO TASK: Advanced Implementation
# =============================================================================

def pro_task_control_flow_framework():
    """
    PRO TASK: Create a control flow framework
    
    Instructions:
    1. Create a framework for implementing complex control flow
    2. Support for state machines
    3. Support for decision trees
    4. Support for rule engines
    5. Test your framework
    """
    # Your code here
    pass

def pro_task_performance_optimization():
    """
    PRO TASK: Optimize control flow for high-performance applications
    
    Instructions:
    1. Create a high-performance control flow system
    2. Implement caching for frequently used conditions
    3. Implement lazy evaluation
    4. Implement parallel processing
    5. Benchmark your system
    """
    # Your code here
    pass

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🔥 Day 8: If/Else vs Ternary vs Switch Practice 🔥")
    print("=" * 50)
    
    # Run examples
    demonstrate_basic_control_flow()
    demonstrate_performance()
    demonstrate_advanced_patterns()
    demonstrate_real_world_examples()
    
    print("\n" + "=" * 50)
    print("📝 EXERCISES - Complete the TODO sections above!")
    print("=" * 50)
    
    # Uncomment these when you complete the exercises
    # exercise_1_if_else_statements()
    # exercise_1_ternary_operators()
    # exercise_1_match_statements()
    # exercise_2_switch_implementation()
    # exercise_2_advanced_switch()
    # exercise_3_performance_comparison()
    # exercise_3_optimization()
    # exercise_4_business_logic()
    # exercise_4_error_handling()
    # pro_task_control_flow_framework()
    # pro_task_performance_optimization()
    
    print("\n🎯 Challenge: Complete all exercises and share your solutions!")

