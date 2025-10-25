# Day 2 – Mutable vs Immutable: Understanding Python's Memory Model

### 🎯 Question
> **"Explain the difference between mutable and immutable objects in Python. What happens when you pass a mutable object to a function? Can you show me examples of both and explain the memory implications?"**

---

### 🧒 Beginner Answer

In Python, objects are either **mutable** (can be changed) or **immutable** (cannot be changed).

**Immutable objects:**
- Numbers (int, float, complex)
- Strings
- Tuples
- Booleans
- Frozensets

**Mutable objects:**
- Lists
- Dictionaries
- Sets
- Custom objects

```python
# Immutable - cannot be changed
x = 5
y = x
y = 10  # x is still 5

# Mutable - can be changed
list1 = [1, 2, 3]
list2 = list1
list2.append(4)  # list1 is now [1, 2, 3, 4]
```

**When to use:**
- Use **immutable objects** when data should not change
- Use **mutable objects** when data needs to be modified

---

### 👩‍💻 Intermediate Answer

The key difference affects how Python handles memory and object references:

**Memory and Reference Behavior:**
```python
import sys

# Immutable objects
a = 5
b = 5
print(f"Same object? {a is b}")  # True - Python reuses small integers
print(f"ID of a: {id(a)}, ID of b: {id(b)}")

# Mutable objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"Same object? {list1 is list2}")  # False - different objects
print(f"ID of list1: {id(list1)}, ID of list2: {id(list2)}")
```

**Function Parameter Behavior:**
```python
def modify_immutable(x):
    x = x + 1
    print(f"Inside function: {x}")

def modify_mutable(lst):
    lst.append(4)
    print(f"Inside function: {lst}")

# Test with immutable
num = 5
print(f"Before: {num}")
modify_immutable(num)
print(f"After: {num}")  # Still 5

# Test with mutable
my_list = [1, 2, 3]
print(f"Before: {my_list}")
modify_mutable(my_list)
print(f"After: {my_list}")  # Now [1, 2, 3, 4]
```

**Memory Implications:**
```python
# Immutable objects are cached for small values
a = 256
b = 256
print(f"Small ints same object: {a is b}")  # True

c = 257
d = 257
print(f"Large ints same object: {c is d}")  # False (implementation dependent)

# String interning
str1 = "hello"
str2 = "hello"
print(f"Strings same object: {str1 is str2}")  # True (interning)
```

---

### 🧠 Pro Developer Answer

Understanding mutability is crucial for **memory management, performance optimization, and avoiding bugs**:

**Deep Dive into Python's Memory Model:**
```python
import sys
from typing import List, Dict, Any

def analyze_memory_behavior():
    """Analyze how Python handles memory for mutable vs immutable objects"""
    
    # Integer caching (-5 to 256)
    small_int1 = 100
    small_int2 = 100
    large_int1 = 1000
    large_int2 = 1000
    
    print(f"Small ints (100): {small_int1 is small_int2}")
    print(f"Large ints (1000): {large_int1 is large_int2}")
    
    # String interning
    str1 = "hello"
    str2 = "hello"
    str3 = "hello" + " world"
    str4 = "hello world"
    
    print(f"Simple strings: {str1 is str2}")
    print(f"Concatenated strings: {str3 is str4}")
    
    # Tuple immutability
    tuple1 = (1, 2, [3, 4])  # Contains mutable list
    print(f"Tuple with mutable element: {tuple1}")
    tuple1[2].append(5)  # This works!
    print(f"Modified tuple: {tuple1}")

analyze_memory_behavior()
```

**Advanced Function Parameter Patterns:**
```python
def demonstrate_parameter_passing():
    """Show different ways to handle mutable parameters"""
    
    # Problem: Unintended side effects
    def bad_function(items: List[int]) -> List[int]:
        items.append(999)  # Modifies original list!
        return items
    
    # Solution 1: Create a copy
    def good_function_v1(items: List[int]) -> List[int]:
        items_copy = items.copy()
        items_copy.append(999)
        return items_copy
    
    # Solution 2: Use immutable operations
    def good_function_v2(items: List[int]) -> List[int]:
        return items + [999]  # Creates new list
    
    # Solution 3: Document the behavior
    def documented_function(items: List[int]) -> List[int]:
        """
        Modifies the input list in place.
        Use items.copy() if you need to preserve the original.
        """
        items.append(999)
        return items
    
    # Test the functions
    original = [1, 2, 3]
    print(f"Original: {original}")
    
    result1 = good_function_v1(original)
    print(f"After v1: original={original}, result={result1}")
    
    result2 = good_function_v2(original)
    print(f"After v2: original={original}, result={result2}")

demonstrate_parameter_passing()
```

**Performance and Memory Optimization:**
```python
def performance_analysis():
    """Analyze performance implications of mutability"""
    import time
    
    # Test 1: String concatenation (immutable)
    start = time.time()
    result = ""
    for i in range(10000):
        result += str(i)  # Creates new string each time
    string_time = time.time() - start
    
    # Test 2: List concatenation (mutable)
    start = time.time()
    result_list = []
    for i in range(10000):
        result_list.append(str(i))  # Modifies existing list
    list_time = time.time() - start
    
    print(f"String concatenation: {string_time:.6f}s")
    print(f"List concatenation: {list_time:.6f}s")
    print(f"List is {string_time/list_time:.1f}x faster")

def memory_optimization_patterns():
    """Show memory optimization patterns"""
    
    # Pattern 1: Use tuples for fixed data
    coordinates = (10, 20, 30)  # More memory efficient than [10, 20, 30]
    
    # Pattern 2: Use frozenset for immutable sets
    valid_statuses = frozenset(['active', 'inactive', 'pending'])
    
    # Pattern 3: Use __slots__ for custom classes
    class OptimizedPoint:
        __slots__ = ['x', 'y']  # Prevents __dict__ creation
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    # Pattern 4: Use generators for large datasets
    def large_data_generator():
        for i in range(1000000):
            yield i * 2  # Memory efficient
    
    # Pattern 5: Use copy vs deepcopy appropriately
    import copy
    
    original = [1, 2, [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    
    original[2].append(5)
    print(f"Original: {original}")
    print(f"Shallow copy: {shallow}")  # [1, 2, [3, 4, 5]]
    print(f"Deep copy: {deep}")        # [1, 2, [3, 4]]

performance_analysis()
memory_optimization_patterns()
```

**Common Pitfalls and Best Practices:**
```python
def common_pitfalls():
    """Demonstrate common mutability pitfalls"""
    
    # Pitfall 1: Mutable default arguments
    def bad_function(items=[]):  # DON'T DO THIS!
        items.append("new item")
        return items
    
    def good_function(items=None):
        if items is None:
            items = []
        items.append("new item")
        return items
    
    # Pitfall 2: Shallow vs deep copying
    original = [1, 2, [3, 4]]
    shallow_copy = original.copy()
    shallow_copy[2].append(5)  # Modifies original!
    
    # Pitfall 3: Tuple with mutable elements
    mutable_tuple = ([1, 2], [3, 4])
    mutable_tuple[0].append(3)  # This works!
    
    print("Common pitfalls demonstrated")

common_pitfalls()
```

**When to Use Each:**

**Use Immutable Objects When:**
- Data should not change (constants, configuration)
- Thread safety is required
- You need hashable objects (dictionary keys)
- Memory efficiency is critical
- You want to prevent accidental modifications

**Use Mutable Objects When:**
- Data needs to change frequently
- You need in-place operations for performance
- Building dynamic data structures
- Implementing algorithms that modify data

**Pro Tip:** Always consider the **semantic meaning** of your data. If it represents a value that shouldn't change, use immutable types. If it's a container that grows/shrinks, use mutable types.

---

## 💡 Pro Tip
> **Use immutable objects for function parameters when you don't want side effects. For mutable parameters, document the behavior clearly or create copies to avoid unexpected modifications.**

---

## 💬 Reference Links

* [Python Docs – Objects and Values](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
* [RealPython – Python Mutable vs Immutable](https://realpython.com/python-mutable-vs-immutable-types/)
* [GeeksForGeeks – Mutable vs Immutable](https://www.geeksforgeeks.org/mutable-vs-immutable-objects-in-python/)
* [StackOverflow – Mutable Default Arguments](https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument)

---