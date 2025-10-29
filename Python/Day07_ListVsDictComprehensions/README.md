# Day 7 – List vs Dict Comprehensions: Pythonic Data Transformation

### 🎯 Question
> **"What's the difference between list comprehensions and dictionary comprehensions in Python? When would you use each? Can you show me examples of complex comprehensions and explain their performance characteristics?"**

---

### 🧒 Beginner Answer

**List comprehensions** create lists in a concise way.

**Dictionary comprehensions** create dictionaries in a concise way.

```python
# List comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# With conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

**When to use:**
- Use **list comprehensions** to create lists
- Use **dictionary comprehensions** to create dictionaries
- Both are more readable than loops

---

### 👩‍💻 Intermediate Answer

Comprehensions are more efficient and readable than traditional loops:

**Performance Comparison:**
```python
import time

# Traditional loop
start = time.time()
result1 = []
for i in range(100000):
    if i % 2 == 0:
        result1.append(i**2)
loop_time = time.time() - start

# List comprehension
start = time.time()
result2 = [i**2 for i in range(100000) if i % 2 == 0]
comp_time = time.time() - start

print(f"Loop time: {loop_time:.6f}s")
print(f"Comprehension time: {comp_time:.6f}s")
print(f"Comprehension is {loop_time/comp_time:.1f}x faster")

# Expected output (approximate):
# Loop time: 0.080000s
# Comprehension time: 0.060000s
# Comprehension is 1.3x faster
```

**Advanced Patterns:**
```python
# Nested comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary comprehension with conditions
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered = {k: v for k, v in data.items() if v > 2}
print(filtered)  # {'c': 3, 'd': 4}

# Multiple conditions
result = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(result)  # [0, 6, 12, 18]
```

**Real-World Examples:**
```python
# Data processing
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# List comprehension
names = [student['name'] for student in students]
print(names)  # ['Alice', 'Bob', 'Charlie']

# Dictionary comprehension
grade_dict = {student['name']: student['grade'] for student in students}
print(grade_dict)  # {'Alice': 85, 'Bob': 92, 'Charlie': 78}
```

---

### 🧠 Pro Developer Answer

Comprehensions are powerful tools for **data transformation, filtering, and creating efficient data structures**:

**Advanced Comprehension Patterns:**
```python
from typing import List, Dict, Any, Tuple
import time

def advanced_comprehension_patterns():
    """Show advanced comprehension patterns"""
    
    # Pattern 1: Nested comprehensions with complex logic
    data = [
        {'name': 'Alice', 'scores': [85, 90, 78]},
        {'name': 'Bob', 'scores': [92, 88, 95]},
        {'name': 'Charlie', 'scores': [78, 85, 80]}
    ]
    
    # Get average scores for each student
    avg_scores = {
        student['name']: sum(student['scores']) / len(student['scores'])
        for student in data
    }
    
    # Get students with average score > 85
    top_students = [
        student['name'] for student in data
        if sum(student['scores']) / len(student['scores']) > 85
    ]
    
    print(f"Average scores: {avg_scores}")
    print(f"Top students: {top_students}")
    
    # Expected output:
    # Average scores: {'Alice': 84.33333333333333, 'Bob': 91.66666666666667, 'Charlie': 81.0}
    # Top students: ['Bob']
    
    # Pattern 2: Complex filtering and transformation
    numbers = list(range(100))
    
    # Get squares of even numbers that are divisible by 3
    result = [
        x**2 for x in numbers
        if x % 2 == 0 and x % 3 == 0
    ]
    
    # Pattern 3: Dictionary comprehension with multiple conditions
    config = {
        'debug': True,
        'port': 8080,
        'host': 'localhost',
        'timeout': 30,
        'retries': 3
    }
    
    # Filter and transform configuration
    filtered_config = {
        k.upper(): v for k, v in config.items()
        if isinstance(v, (int, str)) and v is not None
    }
    
    print(f"Filtered config: {filtered_config}")
    
    # Expected output:
    # Filtered config: {'PORT': 8080, 'HOST': 'localhost', 'TIMEOUT': 30, 'RETRIES': 3}

advanced_comprehension_patterns()
```

**Performance Analysis and Optimization:**
```python
def performance_analysis():
    """Analyze performance of different approaches"""
    
    # Test data
    size = 100000
    data = list(range(size))
    
    # Method 1: Traditional loop
    start = time.time()
    result1 = []
    for x in data:
        if x % 2 == 0:
            result1.append(x**2)
    loop_time = time.time() - start
    
    # Method 2: List comprehension
    start = time.time()
    result2 = [x**2 for x in data if x % 2 == 0]
    comp_time = time.time() - start
    
    # Method 3: Generator expression
    start = time.time()
    result3 = list(x**2 for x in data if x % 2 == 0)
    gen_time = time.time() - start
    
    # Method 4: Filter + map
    start = time.time()
    result4 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))
    func_time = time.time() - start
    
    print(f"Loop: {loop_time:.6f}s")
    print(f"Comprehension: {comp_time:.6f}s")
    print(f"Generator: {gen_time:.6f}s")
    print(f"Filter+Map: {func_time:.6f}s")
    
    # Performance ratios
    print(f"\nPerformance ratios (relative to comprehension):")
    print(f"Loop: {loop_time/comp_time:.1f}x slower")
    print(f"Generator: {gen_time/comp_time:.1f}x slower")
    print(f"Filter+Map: {func_time/comp_time:.1f}x slower")
    
    # Expected output (approximate):
    # Loop: 0.100000s
    # Comprehension: 0.080000s
    # Generator: 0.085000s
    # Filter+Map: 0.120000s
    # 
    # Performance ratios (relative to comprehension):
    # Loop: 1.3x slower
    # Generator: 1.1x slower
    # Filter+Map: 1.5x slower

performance_analysis()
```

**Advanced Dictionary Comprehension Patterns:**
```python
def advanced_dict_comprehensions():
    """Show advanced dictionary comprehension patterns"""
    
    # Pattern 1: Grouping data
    data = [
        ('apple', 'fruit'),
        ('banana', 'fruit'),
        ('carrot', 'vegetable'),
        ('broccoli', 'vegetable'),
        ('orange', 'fruit')
    ]
    
    # Group by category
    grouped = {}
    for item, category in data:
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    
    # Using dictionary comprehension (more complex)
    from collections import defaultdict
    grouped_comp = defaultdict(list)
    for item, category in data:
        grouped_comp[category].append(item)
    grouped_comp = dict(grouped_comp)
    
    print(f"Grouped data: {grouped_comp}")
    
    # Expected output:
    # Grouped data: {'fruit': ['apple', 'banana', 'orange'], 'vegetable': ['carrot', 'broccoli']}
    
    # Pattern 2: Transforming nested data
    nested_data = {
        'user1': {'name': 'Alice', 'age': 25, 'city': 'New York'},
        'user2': {'name': 'Bob', 'age': 30, 'city': 'Boston'},
        'user3': {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    }
    
    # Extract specific fields
    user_names = {uid: user['name'] for uid, user in nested_data.items()}
    adult_users = {
        uid: user for uid, user in nested_data.items()
        if user['age'] >= 30
    }
    
    print(f"User names: {user_names}")
    print(f"Adult users: {adult_users}")
    
    # Expected output:
    # User names: {'user1': 'Alice', 'user2': 'Bob', 'user3': 'Charlie'}
    # Adult users: {'user2': {'name': 'Bob', 'age': 30, 'city': 'Boston'}, 'user3': {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}}
    
    # Pattern 3: Complex key-value transformations
    text = "hello world python programming"
    word_lengths = {word: len(word) for word in text.split()}
    long_words = {word: len(word) for word in text.split() if len(word) > 5}
    
    print(f"Word lengths: {word_lengths}")
    print(f"Long words: {long_words}")
    
    # Expected output:
    # Word lengths: {'hello': 5, 'world': 5, 'python': 6, 'programming': 11}
    # Long words: {'python': 6, 'programming': 11}

advanced_dict_comprehensions()
```

**Memory-Efficient Patterns:**
```python
def memory_efficient_patterns():
    """Show memory-efficient comprehension patterns"""
    
    # Pattern 1: Generator expressions for large datasets
    def process_large_dataset(filename):
        """Process large dataset using generator expression"""
        with open(filename, 'r') as file:
            return (line.strip().upper() for line in file)
    
    # Pattern 2: Conditional comprehensions
    def filter_and_transform(data, condition, transform):
        """Filter and transform data efficiently"""
        return [transform(item) for item in data if condition(item)]
    
    # Pattern 3: Nested comprehensions with early termination
    def find_first_match(data, condition):
        """Find first match using comprehension"""
        matches = [item for item in data if condition(item)]
        return matches[0] if matches else None
    
    # Pattern 4: Dictionary comprehension with default values
    def create_lookup_table(keys, default_value=0):
        """Create lookup table with default values"""
        return {key: default_value for key in keys}
    
    # Example usage
    numbers = list(range(1000))
    even_squares = [x**2 for x in numbers if x % 2 == 0]
    print(f"Even squares count: {len(even_squares)}")
    
    # Expected output:
    # Even squares count: 500

memory_efficient_patterns()
```

**Common Pitfalls and Best Practices:**
```python
def common_pitfalls():
    """Demonstrate common pitfalls and best practices"""
    
    # Pitfall 1: Overly complex comprehensions
    # Bad: Hard to read and understand
    bad_comprehension = [
        x**2 for x in range(100)
        if x % 2 == 0
        if x % 3 == 0
        if x > 10
        if x < 50
    ]
    
    # Good: Break into steps or use functions
    def is_valid_number(x):
        return x % 2 == 0 and x % 3 == 0 and 10 < x < 50
    
    good_comprehension = [x**2 for x in range(100) if is_valid_number(x)]
    
    # Pitfall 2: Side effects in comprehensions
    # Bad: Side effects in comprehension
    counter = 0
    bad_side_effect = [counter := counter + 1 for _ in range(5)]
    
    # Good: Avoid side effects
    good_no_side_effect = [i + 1 for i in range(5)]
    
    # Pitfall 3: Not considering memory usage
    # Bad: Creates large list in memory
    large_list = [x**2 for x in range(1000000)]
    
    # Good: Use generator expression for large datasets
    large_generator = (x**2 for x in range(1000000))
    
    # Best Practice: Use comprehensions for simple transformations
    def best_practices():
        """Show best practices for comprehensions"""
        
        # Use comprehensions for:
        # 1. Simple transformations
        squares = [x**2 for x in range(10)]
        
        # 2. Filtering
        evens = [x for x in range(10) if x % 2 == 0]
        
        # 3. Creating dictionaries
        square_dict = {x: x**2 for x in range(10)}
        
        # 4. Nested data processing
        data = [{'name': f'user{i}', 'score': i*10} for i in range(5)]
        scores = [user['score'] for user in data if user['score'] > 20]
        
        return squares, evens, square_dict, scores

common_pitfalls()
```

**When to Use Each:**

**Use List Comprehensions When:**
- You need to create a list from an iterable
- You want to filter and transform data
- You need a concise, readable solution
- Performance is important
- The logic is simple enough to fit in one line

**Use Dictionary Comprehensions When:**
- You need to create a dictionary from an iterable
- You want to transform key-value pairs
- You need to filter dictionary data
- You want to create lookup tables
- You need to group or aggregate data

**Use Generator Expressions When:**
- You're working with large datasets
- Memory usage is a concern
- You only need to iterate once
- You want lazy evaluation

**Pro Tip:** Use comprehensions for **simple transformations and filtering**. For complex logic, consider using regular loops or helper functions for better readability.

---

## 💡 Pro Tip
> **Use comprehensions for simple transformations and filtering. For complex logic, consider using regular loops or helper functions for better readability.**

---

## 💬 Reference Links

* [Python Docs – List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [RealPython – List Comprehensions](https://realpython.com/list-comprehension-python/)
* [GeeksForGeeks – List Comprehensions](https://www.geeksforgeeks.org/python-list-comprehension/)
* [StackOverflow – List vs Dict Comprehensions](https://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python)

---

