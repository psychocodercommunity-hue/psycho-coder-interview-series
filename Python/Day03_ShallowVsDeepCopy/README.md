# Day 3 – Shallow vs Deep Copy: Mastering Python's Copy Mechanisms

### 🎯 Question
> **"What's the difference between shallow copy and deep copy in Python? When would you use each? Can you show me examples where using the wrong type of copy leads to bugs?"**

---

### 🧒 Beginner Answer

**Shallow copy** creates a new object but inserts references to the objects found in the original.

**Deep copy** creates a new object and recursively copies all nested objects.

```python
import copy

original = [1, 2, [3, 4]]

# Shallow copy
shallow = copy.copy(original)
shallow[2].append(5)  # Modifies the original!

# Deep copy
deep = copy.deepcopy(original)
deep[2].append(6)  # Doesn't modify the original

print(f"Original: {original}")  # [1, 2, [3, 4, 5]]
print(f"Shallow: {shallow}")    # [1, 2, [3, 4, 5]]
print(f"Deep: {deep}")          # [1, 2, [3, 4, 6]]
```

**When to use:**
- Use **shallow copy** when you only need to copy the top level
- Use **deep copy** when you need to copy nested objects too

---

### 👩‍💻 Intermediate Answer

The difference becomes critical when dealing with nested data structures:

**Understanding the Copy Behavior:**
```python
import copy

# Complex nested structure
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
```

**Performance Implications:**
```python
import copy
import time

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
```

**Common Use Cases:**
- **Shallow copy**: Configuration objects, simple data structures
- **Deep copy**: Complex nested data, objects with references

---

### 🧠 Pro Developer Answer

Understanding copy mechanisms is crucial for **avoiding subtle bugs, optimizing performance, and implementing robust data handling**:

**Advanced Copy Behavior Analysis:**
```python
import copy
from typing import List, Dict, Any

def analyze_copy_behavior():
    """Analyze different copy behaviors in detail"""
    
    # Test 1: Simple lists
    simple_list = [1, 2, 3]
    shallow_simple = copy.copy(simple_list)
    deep_simple = copy.deepcopy(simple_list)
    
    print(f"Simple list - Same object? {simple_list is shallow_simple}")
    print(f"Simple list - Same object? {simple_list is deep_simple}")
    
    # Test 2: Nested structures
    nested = [1, [2, 3], {'a': 4}]
    shallow_nested = copy.copy(nested)
    deep_nested = copy.deepcopy(nested)
    
    print(f"Nested - Top level same? {nested is shallow_nested}")
    print(f"Nested - Inner list same? {nested[1] is shallow_nested[1]}")
    print(f"Nested - Inner dict same? {nested[2] is shallow_nested[2]}")
    
    print(f"Deep - Top level same? {nested is deep_nested}")
    print(f"Deep - Inner list same? {nested[1] is deep_nested[1]}")
    print(f"Deep - Inner dict same? {nested[2] is deep_nested[2]}")

analyze_copy_behavior()
```

**Custom Copy Implementation:**
```python
class CustomObject:
    """Custom class to demonstrate copy behavior"""
    
    def __init__(self, value, nested_data=None):
        self.value = value
        self.nested_data = nested_data or []
        self._private = "secret"
    
    def __copy__(self):
        """Custom shallow copy implementation"""
        new_obj = CustomObject(self.value)
        new_obj.nested_data = self.nested_data  # Reference, not copy
        new_obj._private = self._private
        return new_obj
    
    def __deepcopy__(self, memo):
        """Custom deep copy implementation"""
        import copy
        new_obj = CustomObject(self.value)
        new_obj.nested_data = copy.deepcopy(self.nested_data, memo)
        new_obj._private = self._private
        return new_obj
    
    def __repr__(self):
        return f"CustomObject(value={self.value}, nested={self.nested_data})"

def demonstrate_custom_copy():
    """Show custom copy behavior"""
    original = CustomObject(42, [1, 2, 3])
    
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)
    
    # Modify nested data
    shallow.nested_data.append(4)
    deep.nested_data.append(5)
    
    print(f"Original: {original}")
    print(f"Shallow: {shallow}")
    print(f"Deep: {deep}")

demonstrate_custom_copy()
```

**Performance Optimization Strategies:**
```python
def performance_optimization():
    """Show performance optimization techniques"""
    import time
    import copy
    
    # Large nested structure
    large_data = {
        'users': [
            {
                'id': i,
                'profile': {
                    'name': f'User{i}',
                    'settings': {
                        'theme': 'dark',
                        'notifications': True,
                        'data': list(range(100))
                    }
                }
            }
            for i in range(1000)
        ]
    }
    
    # Method 1: Full deep copy
    start = time.time()
    full_deep = copy.deepcopy(large_data)
    full_deep_time = time.time() - start
    
    # Method 2: Selective deep copy
    start = time.time()
    selective_copy = {
        'users': [
            {
                'id': user['id'],
                'profile': {
                    'name': user['profile']['name'],
                    'settings': copy.deepcopy(user['profile']['settings'])
                }
            }
            for user in large_data['users']
        ]
    }
    selective_time = time.time() - start
    
    # Method 3: Lazy copying
    start = time.time()
    lazy_copy = copy.copy(large_data)
    lazy_time = time.time() - start
    
    print(f"Full deep copy: {full_deep_time:.6f}s")
    print(f"Selective copy: {selective_time:.6f}s")
    print(f"Lazy copy: {lazy_time:.6f}s")

performance_optimization()
```

**Common Pitfalls and Bug Prevention:**
```python
def common_pitfalls():
    """Demonstrate common copy-related pitfalls"""
    
    # Pitfall 1: Assuming shallow copy is safe for nested data
    def bad_function(data):
        """This function modifies the original data!"""
        data_copy = data.copy()  # Shallow copy
        data_copy['items'].append('new item')  # Modifies original!
        return data_copy
    
    # Pitfall 2: Not understanding when deep copy is needed
    def process_user_data(users):
        """Process user data without modifying original"""
        processed = []
        for user in users:
            user_copy = user.copy()  # Shallow copy
            user_copy['processed'] = True
            user_copy['scores'].sort()  # Modifies original scores!
            processed.append(user_copy)
        return processed
    
    # Pitfall 3: Circular references
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []
            self.parent = None
    
    def create_circular_reference():
        """Create circular reference and test copy behavior"""
        parent = Node('parent')
        child = Node('child')
        parent.children.append(child)
        child.parent = parent
        
        # This will work with deep copy
        try:
            deep_copy = copy.deepcopy(parent)
            print("Deep copy with circular reference: Success")
        except RecursionError:
            print("Deep copy with circular reference: Failed")
    
    create_circular_reference()

common_pitfalls()
```

**Best Practices and Design Patterns:**
```python
def best_practices():
    """Show best practices for copy operations"""
    
    # Pattern 1: Immutable data structures
    from dataclasses import dataclass
    from typing import List
    
    @dataclass(frozen=True)
    class ImmutableConfig:
        """Immutable configuration class"""
        database_url: str
        api_keys: List[str]
        debug_mode: bool
    
    # Pattern 2: Copy-on-write
    class CopyOnWriteList:
        """List that copies only when modified"""
        
        def __init__(self, data=None):
            self._data = data or []
            self._copied = False
        
        def __getitem__(self, index):
            return self._data[index]
        
        def __setitem__(self, index, value):
            if not self._copied:
                self._data = self._data.copy()
                self._copied = True
            self._data[index] = value
        
        def append(self, item):
            if not self._copied:
                self._data = self._data.copy()
                self._copied = True
            self._data.append(item)
    
    # Pattern 3: Factory methods for safe copying
    class DataProcessor:
        """Data processor with safe copy methods"""
        
        def __init__(self, data):
            self.data = data
        
        def get_safe_copy(self):
            """Returns a safe copy for modification"""
            return copy.deepcopy(self.data)
        
        def get_reference_copy(self):
            """Returns a reference copy (use with caution)"""
            return copy.copy(self.data)
        
        def process_with_copy(self, processor_func):
            """Process data with a copy to avoid side effects"""
            data_copy = self.get_safe_copy()
            return processor_func(data_copy)

best_practices()
```

**When to Use Each:**

**Use Shallow Copy When:**
- You only need to modify the top level
- Performance is critical
- You're working with simple data structures
- You want to share references to nested objects

**Use Deep Copy When:**
- You need to modify nested structures
- You want complete independence from the original
- You're working with complex nested data
- You need to ensure no side effects

**Pro Tip:** Always consider the **data structure complexity** and **modification requirements**. When in doubt, use deep copy to avoid subtle bugs, but optimize with shallow copy when performance matters.

---

## 💡 Pro Tip
> **Use deep copy for complex nested data structures to avoid subtle bugs. For performance-critical code, consider selective copying or immutable data structures.**

---

## 💬 Reference Links

* [Python Docs – copy module](https://docs.python.org/3/library/copy.html)
* [RealPython – Shallow vs Deep Copy](https://realpython.com/copying-python-objects/)
* [GeeksForGeeks – Shallow vs Deep Copy](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)
* [StackOverflow – When to use deep copy](https://stackoverfow.com/questions/184710/what-is-the-difference-between-a-deep-copy-and-a-shallow-copy)

---

