# Day 6 – Sets vs Dicts vs Lists: Choosing the Right Data Structure

### 🎯 Question
> **"When would you use a set, dictionary, or list in Python? Can you explain the time complexity of common operations for each? Show me examples where choosing the wrong data structure leads to performance issues."**

---

### 🧒 Beginner Answer

**Lists** are ordered collections that can contain duplicates and are mutable.

**Dictionaries** are key-value pairs that are unordered and mutable.

**Sets** are unordered collections of unique elements that are mutable.

```python
# List - ordered, allows duplicates
my_list = [1, 2, 3, 2, 1]
print(my_list)  # [1, 2, 3, 2, 1]

# Dictionary - key-value pairs
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # John

# Set - unique elements only
my_set = {1, 2, 3, 2, 1}
print(my_set)  # {1, 2, 3}
```

**When to use:**
- Use **lists** for ordered data with duplicates
- Use **dictionaries** for key-value relationships
- Use **sets** for unique elements and fast lookups

---

### 👩‍💻 Intermediate Answer

Understanding the performance characteristics is crucial for choosing the right data structure:

**Time Complexity Comparison:**
```python
import time

# Test data
large_list = list(range(10000))
large_set = set(range(10000))
large_dict = {i: f"value_{i}" for i in range(10000)}

# Test 1: Membership testing
target = 5000

# List membership (O(n))
start = time.time()
result1 = target in large_list
list_time = time.time() - start

# Set membership (O(1))
start = time.time()
result2 = target in large_set
set_time = time.time() - start

# Dict membership (O(1))
start = time.time()
result3 = target in large_dict
dict_time = time.time() - start

print(f"List membership: {list_time:.6f}s")
print(f"Set membership: {set_time:.6f}s")
print(f"Dict membership: {dict_time:.6f}s")
print(f"Set is {list_time/set_time:.1f}x faster than list")

# Expected output (approximate):
# List membership: 0.000150s
# Set membership: 0.000005s
# Dict membership: 0.000005s
# Set is 30.0x faster than list
```

**Common Operations:**
```python
# List operations
my_list = [1, 2, 3, 4, 5]
my_list.append(6)        # O(1)
my_list.insert(0, 0)     # O(n)
my_list.remove(3)        # O(n)
my_list[2]               # O(1) - indexing

# Set operations
my_set = {1, 2, 3, 4, 5}
my_set.add(6)            # O(1)
my_set.remove(3)         # O(1)
my_set.union({7, 8})     # O(n)
my_set.intersection({4, 5, 6})  # O(min(len(s1), len(s2)))

# Dictionary operations
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4         # O(1)
del my_dict['a']         # O(1)
my_dict.get('b')         # O(1)
```

**Use Cases:**
```python
# List: When order matters and duplicates are allowed
shopping_cart = ['apple', 'banana', 'apple', 'orange']
print(f"Total items: {len(shopping_cart)}")  # 4

# Set: When you need unique elements and fast lookups
unique_items = set(shopping_cart)
print(f"Unique items: {unique_items}")  # {'apple', 'banana', 'orange'}

# Dictionary: When you need key-value relationships
inventory = {'apple': 10, 'banana': 5, 'orange': 8}
print(f"Apples in stock: {inventory['apple']}")  # 10
```

---

### 🧠 Pro Developer Answer

Choosing the right data structure is crucial for **performance, memory efficiency, and code maintainability**:

**Advanced Performance Analysis:**
```python
import time
import sys
from typing import List, Dict, Set, Any
from collections import defaultdict, Counter

def comprehensive_performance_analysis():
    """Comprehensive analysis of data structure performance"""
    
    # Test data
    size = 100000
    test_data = list(range(size))
    
    # Memory usage
    list_memory = sys.getsizeof(test_data)
    set_memory = sys.getsizeof(set(test_data))
    dict_memory = sys.getsizeof({i: i for i in test_data})
    
    print(f"Memory usage for {size} elements:")
    print(f"List: {list_memory} bytes")
    print(f"Set: {set_memory} bytes")
    print(f"Dict: {dict_memory} bytes")
    
    # Expected output (approximate):
    # Memory usage for 100000 elements:
    # List: 800064 bytes
    # Set: 4194528 bytes
    # Dict: 4194528 bytes
    
    # Performance tests
    test_list = list(range(size))
    test_set = set(range(size))
    test_dict = {i: i for i in range(size)}
    
    # Membership testing
    target = size // 2
    
    start = time.time()
    for _ in range(1000):
        target in test_list
    list_time = time.time() - start
    
    start = time.time()
    for _ in range(1000):
        target in test_set
    set_time = time.time() - start
    
    start = time.time()
    for _ in range(1000):
        target in test_dict
    dict_time = time.time() - start
    
    print(f"\nMembership testing (1000 iterations):")
    print(f"List: {list_time:.6f}s")
    print(f"Set: {set_time:.6f}s")
    print(f"Dict: {dict_time:.6f}s")
    
    # Expected output (approximate):
    # Membership testing (1000 iterations):
    # List: 0.150000s
    # Set: 0.005000s
    # Dict: 0.005000s

comprehensive_performance_analysis()
```

**Advanced Data Structure Patterns:**
```python
def advanced_patterns():
    """Show advanced patterns for each data structure"""
    
    # Pattern 1: List as stack and queue
    class Stack:
        def __init__(self):
            self._items = []
        
        def push(self, item):
            self._items.append(item)
        
        def pop(self):
            return self._items.pop()
        
        def peek(self):
            return self._items[-1]
        
        def is_empty(self):
            return len(self._items) == 0
    
    # Pattern 2: Set for fast lookups and operations
    def find_common_elements(list1, list2):
        """Find common elements between two lists efficiently"""
        set1 = set(list1)
        set2 = set(list2)
        return list(set1.intersection(set2))
    
    # Pattern 3: Dictionary for caching and memoization
    def memoize(func):
        """Memoization decorator using dictionary"""
        cache = {}
        
        def wrapper(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            cache[args] = result
            return result
        
        return wrapper
    
    # Pattern 4: DefaultDict for grouping
    def group_by_key(data, key_func):
        """Group data by a key function"""
        groups = defaultdict(list)
        for item in data:
            groups[key_func(item)].append(item)
        return dict(groups)
    
    # Pattern 5: Counter for frequency analysis
    def analyze_frequency(text):
        """Analyze character frequency in text"""
        return Counter(text.lower())

advanced_patterns()
```

**Real-World Use Cases:**
```python
def real_world_examples():
    """Show real-world examples of data structure usage"""
    
    # Example 1: Web scraping data processing
    class WebScraper:
        def __init__(self):
            self.visited_urls = set()  # Fast lookup for visited URLs
            self.url_data = {}         # Store scraped data
            self.url_queue = []        # Queue for URLs to visit
        
        def add_url(self, url):
            if url not in self.visited_urls:
                self.url_queue.append(url)
        
        def process_url(self, url):
            if url in self.visited_urls:
                return
            # Process URL
            self.visited_urls.add(url)
            self.url_data[url] = "scraped_data"
    
    # Example 2: Database query optimization
    class QueryOptimizer:
        def __init__(self):
            self.query_cache = {}      # Cache for query results
            self.index_cache = set()   # Cache for indexed columns
        
        def optimize_query(self, query):
            if query in self.query_cache:
                return self.query_cache[query]
            
            # Optimize query
            optimized = self._optimize(query)
            self.query_cache[query] = optimized
            return optimized
        
        def _optimize(self, query):
            # Simple optimization logic
            return query.upper()
    
    # Example 3: Social media analytics
    class SocialMediaAnalytics:
        def __init__(self):
            self.user_followers = defaultdict(set)  # User -> set of followers
            self.user_posts = defaultdict(list)     # User -> list of posts
            self.hashtag_count = Counter()          # Hashtag frequency
        
        def add_follower(self, user, follower):
            self.user_followers[user].add(follower)
        
        def add_post(self, user, post):
            self.user_posts[user].append(post)
            # Extract hashtags
            hashtags = [word for word in post.split() if word.startswith('#')]
            self.hashtag_count.update(hashtags)
        
        def get_trending_hashtags(self, n=10):
            return self.hashtag_count.most_common(n)

real_world_examples()
```

**Performance Optimization Strategies:**
```python
def optimization_strategies():
    """Show optimization strategies for different scenarios"""
    
    # Strategy 1: Choose the right data structure for the operation
    def find_duplicates_inefficient(data):
        """Inefficient way to find duplicates"""
        duplicates = []
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] == data[j]:
                    duplicates.append(data[i])
        return duplicates
    
    def find_duplicates_efficient(data):
        """Efficient way to find duplicates using set"""
        seen = set()
        duplicates = set()
        for item in data:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        return list(duplicates)
    
    # Strategy 2: Use appropriate data structures for different operations
    class EfficientDataProcessor:
        def __init__(self):
            self.data = []
            self.index = {}  # For fast lookups
            self.unique_items = set()  # For uniqueness checks
        
        def add_item(self, item):
            self.data.append(item)
            self.index[item] = len(self.data) - 1
            self.unique_items.add(item)
        
        def find_item(self, item):
            return self.index.get(item, -1)
        
        def is_unique(self, item):
            return item not in self.unique_items
    
    # Strategy 3: Memory optimization
    def memory_optimized_processing():
        """Show memory optimization techniques"""
        
        # Use generators for large datasets
        def process_large_dataset(filename):
            with open(filename, 'r') as file:
                for line in file:
                    yield line.strip().split(',')
        
        # Use sets for membership testing
        def filter_data(data, filter_set):
            return [item for item in data if item in filter_set]
        
        # Use dictionaries for sparse data
        def sparse_matrix(rows, cols):
            return defaultdict(lambda: defaultdict(int))

optimization_strategies()
```

**Common Pitfalls and Best Practices:**
```python
def common_pitfalls():
    """Demonstrate common pitfalls and best practices"""
    
    # Pitfall 1: Using list for membership testing
    def bad_membership_test(data, target):
        return target in data  # O(n) for lists
    
    def good_membership_test(data, target):
        return target in set(data)  # O(1) for sets
    
    # Pitfall 2: Not considering memory usage
    def bad_memory_usage():
        large_list = [i for i in range(1000000)]  # High memory usage
        return large_list
    
    def good_memory_usage():
        large_generator = (i for i in range(1000000))  # Low memory usage
        return large_generator
    
    # Pitfall 3: Inefficient data structure operations
    def bad_operations():
        data = [1, 2, 3, 4, 5]
        # Inefficient: O(n) for each operation
        data.insert(0, 0)  # O(n)
        data.remove(3)     # O(n)
        return data
    
    def good_operations():
        data = [1, 2, 3, 4, 5]
        # Efficient: O(1) for append, O(n) for remove
        data.append(0)     # O(1)
        data.pop()         # O(1)
        return data
    
    # Best Practice: Choose data structure based on operations
    def choose_data_structure():
        """Guidelines for choosing data structures"""
        
        # Use list when:
        # - Order matters
        # - Duplicates are allowed
        # - You need indexing
        # - You frequently append/remove from end
        
        # Use set when:
        # - You need unique elements
        # - You frequently check membership
        # - You need set operations (union, intersection)
        # - Order doesn't matter
        
        # Use dict when:
        # - You need key-value relationships
        # - You need fast lookups by key
        # - You need to store metadata
        # - You need to count frequencies

common_pitfalls()
```

**When to Use Each:**

**Use Lists When:**
- Order matters
- Duplicates are allowed
- You need indexing
- You frequently append/remove from the end
- You need to iterate in order

**Use Sets When:**
- You need unique elements
- You frequently check membership
- You need set operations (union, intersection, difference)
- Order doesn't matter
- You need fast lookups

**Use Dictionaries When:**
- You need key-value relationships
- You need fast lookups by key
- You need to store metadata
- You need to count frequencies
- You need to group data

**Pro Tip:** Always consider the **operations you'll perform most frequently**. Choose the data structure that optimizes for your most common operations.

---

## 💡 Pro Tip
> **Choose your data structure based on the operations you'll perform most frequently. Use sets for membership testing, lists for ordered data, and dictionaries for key-value relationships.**

---

## 💬 Reference Links

* [Python Docs – Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
* [RealPython – Python Data Structures](https://realpython.com/python-data-structures/)
* [GeeksForGeeks – Data Structures](https://www.geeksforgeeks.org/python-data-structures/)
* [StackOverflow – List vs Set vs Dict](https://stackoverflow.com/questions/3489071/in-python-when-to-use-a-dictionary-list-or-set)

---


