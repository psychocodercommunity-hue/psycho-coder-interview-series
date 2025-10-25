# Day 4 – Lambda vs Regular Functions: When to Use Each

### 🎯 Question
> **"What's the difference between lambda functions and regular functions in Python? When would you use each? Can you show me examples where lambda functions are more appropriate and where they might be problematic?"**

---

### 🧒 Beginner Answer

**Lambda functions** are anonymous functions (functions without a name) that can be created in a single line.

**Regular functions** are defined with the `def` keyword and have a name.

```python
# Regular function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

# Both do the same thing
print(add(5, 3))        # 8
print(add_lambda(5, 3)) # 8
```

**When to use:**
- Use **lambda** for simple, one-line functions
- Use **regular functions** for complex logic or reusable code

```python
# Common use with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

---

### 👩‍💻 Intermediate Answer

Lambda functions are more powerful when used with **functional programming** concepts:

**Advanced Usage Patterns:**
```python
# 1. Sorting with custom key
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda x: x['grade'])
print(sorted_students)

# 2. Filtering data
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 3. Multiple conditions
adults = list(filter(lambda x: x['age'] >= 18 and x['active'], users))
```

**Performance Considerations:**
```python
import time

# Test lambda vs regular function performance
def regular_square(x):
    return x ** 2

lambda_square = lambda x: x ** 2

# Time both approaches
numbers = list(range(1000000))

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

# Expected output (approximate):
# Regular function: 0.150000s
# Lambda function: 0.160000s
# 
# Note: Lambda functions are typically 5-10% slower due to 
# the overhead of creating anonymous function objects
```

**Use Cases:**
- **Lambda**: Data processing, sorting, filtering, simple transformations
- **Regular functions**: Complex logic, reusable code, debugging

---

### 🧠 Pro Developer Answer

The choice between lambda and regular functions goes beyond syntax - it's about **readability, maintainability, and performance**:

**Advanced Lambda Patterns:**
```python
from functools import reduce
from typing import List, Callable, Any

def demonstrate_advanced_lambda():
    """Show advanced lambda usage patterns"""
    
    # 1. Higher-order functions with lambda
    def create_multiplier(factor):
        return lambda x: x * factor
    
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"Double 5: {double(5)}")  # 10
    print(f"Triple 5: {triple(5)}")  # 15
    
    # 2. Lambda with reduce for complex operations
    numbers = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, numbers)
    print(f"Product: {product}")  # 120
    
    # 3. Lambda with complex data structures
    data = [
        {'name': 'Alice', 'scores': [85, 90, 78]},
        {'name': 'Bob', 'scores': [92, 88, 95]},
        {'name': 'Charlie', 'scores': [78, 85, 80]}
    ]
    
    # Find student with highest average
    best_student = max(data, key=lambda x: sum(x['scores']) / len(x['scores']))
    print(f"Best student: {best_student['name']}")

demonstrate_advanced_lambda()
```

**Lambda vs Regular Functions - When to Use Each:**
```python
def lambda_vs_regular_analysis():
    """Analyze when to use lambda vs regular functions"""
    
    # ✅ Good use of lambda - simple, one-time operation
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    
    # ✅ Good use of lambda - sorting with custom key
    items = [('apple', 3), ('banana', 1), ('cherry', 2)]
    sorted_items = sorted(items, key=lambda x: x[1])
    
    # ❌ Bad use of lambda - complex logic
    # This should be a regular function
    complex_lambda = lambda x: x**2 if x > 0 else 0 if x == 0 else -x**2
    
    # ✅ Better approach - regular function
    def complex_function(x):
        if x > 0:
            return x**2
        elif x == 0:
            return 0
        else:
            return -x**2
    
    # ✅ Good use of lambda - event handling
    button_handlers = {
        'save': lambda: save_data(),
        'cancel': lambda: cancel_operation(),
        'reset': lambda: reset_form()
    }

lambda_vs_regular_analysis()
```

**Common Pitfalls and Best Practices:**
```python
def common_pitfalls():
    """Demonstrate common lambda pitfalls"""
    
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
    
    # Pitfall 2: Overly complex lambda expressions
    # ❌ Bad - hard to read and debug
    complex_lambda = lambda x: x**2 if x > 0 else 0 if x == 0 else -x**2
    
    # ✅ Good - use regular function
    def complex_function(x):
        if x > 0:
            return x**2
        elif x == 0:
            return 0
        else:
            return -x**2

common_pitfalls()
```

**When to Use Each:**

**Use Lambda Functions When:**
- Simple, one-line operations
- Functional programming with map, filter, reduce
- Sorting with custom keys
- Event handling and callbacks
- Quick data transformations
- The logic is simple enough to understand at a glance

**Use Regular Functions When:**
- Complex logic or multiple statements
- The function needs to be reused
- You need docstrings or type hints
- The function has side effects
- You need to debug or test the function
- The logic is complex enough to warrant a name

**Pro Tip:** Lambda functions should be **simple, readable, and single-purpose**. If you find yourself writing complex lambda expressions, consider using a regular function instead.

---

## 💡 Pro Tip
> **Use lambda functions for simple, one-line operations and functional programming. For complex logic, always prefer regular functions with proper names and documentation.**

---

## 💬 Reference Links

* [Python Docs – Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
* [RealPython – Lambda Functions](https://realpython.com/python-lambda/)
* [GeeksForGeeks – Lambda Functions](https://www.geeksforgeeks.org/python-lambda/)
* [StackOverflow – When to use lambda](https://stackoverflow.com/questions/890128/why-are-python-lambdas-useful)

---
