# Day 8 – If/Else vs Ternary vs Switch: Control Flow in Python

### 🎯 Question
> **"What's the difference between if/else statements, ternary operators, and switch statements in Python? When would you use each? Can you show me examples of how to implement switch-like behavior in Python?"**

---

### 🧒 Beginner Answer

**If/else statements** are the basic way to make decisions in Python.

**Ternary operators** are a concise way to write simple if/else statements.

**Switch statements** don't exist in Python, but you can simulate them.

**Match statements** (Python 3.10+) provide powerful pattern matching capabilities.

```python
# If/else statement
age = 18
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator
status = "adult" if age >= 18 else "minor"

# Switch-like behavior using if/elif/else
day = "Monday"
if day == "Monday":
    message = "Start of work week"
elif day == "Friday":
    message = "TGIF!"
elif day == "Saturday" or day == "Sunday":
    message = "Weekend!"
else:
    message = "Regular day"

# Match statement (Python 3.10+)
day = "Monday"
match day:
    case "Monday":
        message = "Start of work week"
    case "Friday":
        message = "TGIF!"
    case "Saturday" | "Sunday":
        message = "Weekend!"
    case _:
        message = "Regular day"
```

**When to use:**
- Use **if/else** for complex logic
- Use **ternary** for simple conditions
- Use **if/elif/else** for multiple conditions (switch-like)
- Use **match** for pattern matching and multiple conditions (Python 3.10+)

---

### 👩‍💻 Intermediate Answer

Understanding when to use each approach is crucial for clean, readable code:

**Performance Comparison:**
```python
import time

# Test data
test_values = [1, 2, 3, 4, 5] * 1000

# Method 1: If/else
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

# Method 2: Ternary
start = time.time()
result2 = ["one" if x == 1 else "two" if x == 2 else "three" if x == 3 else "other" for x in test_values]
ternary_time = time.time() - start

# Method 3: Dictionary lookup
start = time.time()
mapping = {1: "one", 2: "two", 3: "three"}
result3 = [mapping.get(x, "other") for x in test_values]
dict_time = time.time() - start

# Method 4: Match statement (Python 3.10+)
def match_value(x):
    match x:
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case _:
            return "other"

start = time.time()
result4 = [match_value(x) for x in test_values]
match_time = time.time() - start

print(f"If/else time: {if_time:.6f}s")
print(f"Ternary time: {ternary_time:.6f}s")
print(f"Dictionary time: {dict_time:.6f}s")
print(f"Match time: {match_time:.6f}s")

# Expected output (approximate):
# If/else time: 0.050000s
# Ternary time: 0.080000s
# Dictionary time: 0.030000s
# Match time: 0.055000s
```

**Advanced Patterns:**
```python
# Pattern 1: Nested ternary (use sparingly)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

# Pattern 2: Multiple conditions
def get_discount(customer_type, order_amount):
    if customer_type == "premium" and order_amount > 100:
        return 0.15
    elif customer_type == "premium" or order_amount > 200:
        return 0.10
    elif customer_type == "regular" and order_amount > 50:
        return 0.05
    else:
        return 0.0

# Pattern 3: Switch-like behavior with functions
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

# Pattern 4: Match statement with pattern matching
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
```

---

### 🧠 Pro Developer Answer

Understanding control flow patterns is essential for **writing maintainable, efficient, and readable code**:

**Advanced Switch-Like Patterns:**
```python
from typing import Callable, Any, Dict
import time

class Switch:
    """Advanced switch-like implementation"""
    
    def __init__(self):
        self.cases = {}
        self.default_case = None
    
    def case(self, value: Any, handler: Callable):
        """Add a case to the switch"""
        self.cases[value] = handler
        return self
    
    def default(self, handler: Callable):
        """Set the default case"""
        self.default_case = handler
        return self
    
    def execute(self, value: Any):
        """Execute the appropriate case"""
        handler = self.cases.get(value, self.default_case)
        if handler:
            return handler()
        return None

def demonstrate_advanced_switch():
    """Show advanced switch-like patterns"""
    
    # Pattern 1: Function-based switch
    def process_user_input(command):
        handlers = {
            'create': lambda: "Creating new item...",
            'read': lambda: "Reading data...",
            'update': lambda: "Updating item...",
            'delete': lambda: "Deleting item...",
            'list': lambda: "Listing all items..."
        }
        return handlers.get(command, lambda: "Unknown command")
    
    # Expected output examples:
    # process_user_input('create') -> "Creating new item..."
    # process_user_input('read') -> "Reading data..."
    # process_user_input('unknown') -> "Unknown command"
    
    # Pattern 2: Class-based switch
    class CommandProcessor:
        def __init__(self):
            self.commands = {
                'create': self._create,
                'read': self._read,
                'update': self._update,
                'delete': self._delete
            }
        
        def _create(self):
            return "Creating..."
        
        def _read(self):
            return "Reading..."
        
        def _update(self):
            return "Updating..."
        
        def _delete(self):
            return "Deleting..."
        
        def process(self, command):
            handler = self.commands.get(command, self._unknown)
            return handler()
        
        def _unknown(self):
            return "Unknown command"
    
    # Expected output examples:
    # processor = CommandProcessor()
    # processor.process('create') -> "Creating..."
    # processor.process('read') -> "Reading..."
    # processor.process('unknown') -> "Unknown command"
    
    # Pattern 3: Advanced switch with conditions
    def advanced_switch(value):
        if value == 1:
            return "One"
        elif value == 2:
            return "Two"
        elif value == 3:
            return "Three"
        elif isinstance(value, str):
            return f"String: {value}"
        elif isinstance(value, (int, float)):
            return f"Number: {value}"
        else:
            return "Unknown type"
    
    # Expected output examples:
    # advanced_switch(1) -> "One"
    # advanced_switch(2) -> "Two"
    # advanced_switch("hello") -> "String: hello"
    # advanced_switch(3.14) -> "Number: 3.14"
    # advanced_switch([1, 2, 3]) -> "Unknown type"

demonstrate_advanced_switch()
```

**Advanced Match Statement Patterns:**
```python
def advanced_match_patterns():
    """Show advanced match statement patterns (Python 3.10+)"""
    
    # Pattern 1: Pattern matching with data structures
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
            case {"type": "user", "id": user_id}:
                return f"User ID: {user_id}"
            case {"type": "admin", "permissions": perms}:
                return f"Admin with permissions: {perms}"
            case _:
                return "Unknown data structure"
    
    # Pattern 2: Guard clauses with match
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
    
    # Pattern 3: Complex pattern matching
    def analyze_response(response):
        match response:
            case {"status": "success", "data": data}:
                return f"Success: {data}"
            case {"status": "error", "message": msg, "code": code}:
                return f"Error {code}: {msg}"
            case {"status": "pending", "id": task_id}:
                return f"Task {task_id} is pending"
            case {"status": "success"}:
                return "Success with no data"
            case _:
                return "Unknown response format"
    
    # Pattern 4: Class pattern matching
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
    
    # Example usage and expected outputs
    print("=== Advanced Match Patterns ===")
    
    # Test data processing
    print(process_data([1, 2]))  # "Two elements: 1, 2"
    print(process_data([1, 2, 3, 4]))  # "First element: 1, rest: [2, 3, 4]"
    print(process_data({"name": "Alice", "age": 30}))  # "Person: Alice, age 30"
    
    # Test number processing
    print(process_number(-5))  # "Negative number"
    print(process_number(0))  # "Zero"
    print(process_number(7))  # "Single digit positive"
    print(process_number(42))  # "Double digit positive"
    
    # Test response analysis
    success_response = {"status": "success", "data": "user_123"}
    error_response = {"status": "error", "message": "Not found", "code": 404}
    print(analyze_response(success_response))  # "Success: user_123"
    print(analyze_response(error_response))  # "Error 404: Not found"
    
    # Test shape analysis
    point = Point(3, 4)
    circle = Circle(Point(0, 0), 5)
    print(describe_shape(point))  # "Point at (3, 4)"
    print(describe_shape(circle))  # "Circle centered at (0, 0) with radius 5"

advanced_match_patterns()
```

**Performance Analysis and Optimization:**
```python
def performance_analysis():
    """Analyze performance of different control flow approaches"""
    
    # Test data
    test_values = list(range(1000))
    
    # Method 1: If/elif/else chain
    start = time.time()
    result1 = []
    for x in test_values:
        if x < 100:
            result1.append("small")
        elif x < 500:
            result1.append("medium")
        elif x < 800:
            result1.append("large")
        else:
            result1.append("huge")
    if_time = time.time() - start
    
    # Method 2: Ternary operator
    start = time.time()
    result2 = [
        "small" if x < 100 else
        "medium" if x < 500 else
        "large" if x < 800 else
        "huge"
        for x in test_values
    ]
    ternary_time = time.time() - start
    
    # Method 3: Dictionary lookup
    start = time.time()
    def categorize(x):
        if x < 100:
            return "small"
        elif x < 500:
            return "medium"
        elif x < 800:
            return "large"
        else:
            return "huge"
    
    result3 = [categorize(x) for x in test_values]
    func_time = time.time() - start
    
    # Method 4: List-based lookup
    start = time.time()
    categories = ["small"] * 100 + ["medium"] * 400 + ["large"] * 300 + ["huge"] * 200
    result4 = [categories[x] for x in test_values]
    list_time = time.time() - start
    
    print(f"If/elif/else: {if_time:.6f}s")
    print(f"Ternary: {ternary_time:.6f}s")
    print(f"Function: {func_time:.6f}s")
    print(f"List lookup: {list_time:.6f}s")
    
    # Performance ratios
    print(f"\nPerformance ratios (relative to if/elif/else):")
    print(f"Ternary: {ternary_time/if_time:.1f}x")
    print(f"Function: {func_time/if_time:.1f}x")
    print(f"List lookup: {list_time/if_time:.1f}x")
    
    # Expected output (approximate):
    # If/elif/else: 0.080000s
    # Ternary: 0.100000s
    # Function: 0.090000s
    # List lookup: 0.020000s
    # 
    # Performance ratios (relative to if/elif/else):
    # Ternary: 1.3x
    # Function: 1.1x
    # List lookup: 0.3x

performance_analysis()
```

**Advanced Control Flow Patterns:**
```python
def advanced_control_flow():
    """Show advanced control flow patterns"""
    
    # Pattern 1: Strategy pattern with functions
    def calculate_tax_standard(income):
        return income * 0.20
    
    def calculate_tax_premium(income):
        return income * 0.15
    
    def calculate_tax_vip(income):
        return income * 0.10
    
    tax_calculators = {
        'standard': calculate_tax_standard,
        'premium': calculate_tax_premium,
        'vip': calculate_tax_vip
    }
    
    def calculate_tax(customer_type, income):
        calculator = tax_calculators.get(customer_type, calculate_tax_standard)
        return calculator(income)
    
    # Expected output examples:
    # calculate_tax('standard', 1000) -> 200.0
    # calculate_tax('premium', 1000) -> 150.0
    # calculate_tax('vip', 1000) -> 100.0
    # calculate_tax('unknown', 1000) -> 200.0 (defaults to standard)
    
    # Pattern 2: State machine
    class StateMachine:
        def __init__(self):
            self.state = 'idle'
            self.transitions = {
                'idle': ['running', 'paused'],
                'running': ['paused', 'stopped'],
                'paused': ['running', 'stopped'],
                'stopped': ['idle']
            }
        
        def transition(self, new_state):
            if new_state in self.transitions.get(self.state, []):
                self.state = new_state
                return True
            return False
        
        def get_state(self):
            return self.state
    
    # Expected output examples:
    # sm = StateMachine()
    # sm.get_state() -> 'idle'
    # sm.transition('running') -> True
    # sm.get_state() -> 'running'
    # sm.transition('stopped') -> True
    # sm.get_state() -> 'stopped'
    
    # Pattern 3: Chain of responsibility
    class Handler:
        def __init__(self):
            self.next_handler = None
        
        def set_next(self, handler):
            self.next_handler = handler
            return handler
        
        def handle(self, request):
            if self.next_handler:
                return self.next_handler.handle(request)
            return None
    
    class ConcreteHandlerA(Handler):
        def handle(self, request):
            if request == 'A':
                return "Handled by A"
            return super().handle(request)
    
    class ConcreteHandlerB(Handler):
        def handle(self, request):
            if request == 'B':
                return "Handled by B"
            return super().handle(request)
    
    # Pattern 4: Command pattern
    class Command:
        def execute(self):
            pass
    
    class LightOnCommand(Command):
        def execute(self):
            return "Light is on"
    
    class LightOffCommand(Command):
        def execute(self):
            return "Light is off"
    
    class RemoteControl:
        def __init__(self):
            self.commands = {}
        
        def set_command(self, slot, command):
            self.commands[slot] = command
        
        def press_button(self, slot):
            command = self.commands.get(slot)
            if command:
                return command.execute()
            return "No command set"
    
    # Expected output examples:
    # remote = RemoteControl()
    # remote.set_command(1, LightOnCommand())
    # remote.press_button(1) -> "Light is on"
    # remote.press_button(2) -> "No command set"

advanced_control_flow()
```

**Common Pitfalls and Best Practices:**
```python
def common_pitfalls():
    """Demonstrate common pitfalls and best practices"""
    
    # Pitfall 1: Overly complex ternary operators
    # Bad: Hard to read
    bad_ternary = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
    
    # Good: Use if/elif/else for complex conditions
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    # Pitfall 2: Not handling edge cases
    # Bad: No validation
    def bad_division(a, b):
        return a / b
    
    # Good: Handle edge cases
    def good_division(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    # Pitfall 3: Inefficient switch-like behavior
    # Bad: Long if/elif chain
    def bad_switch(value):
        if value == 1:
            return "one"
        elif value == 2:
            return "two"
        elif value == 3:
            return "three"
        # ... many more cases
        else:
            return "unknown"
    
    # Good: Use dictionary lookup
    def good_switch(value):
        mapping = {1: "one", 2: "two", 3: "three"}
        return mapping.get(value, "unknown")
    
    # Best Practice: Choose the right tool for the job
    def best_practices():
        """Show best practices for control flow"""
        
        # Use if/elif/else for:
        # - Complex conditions
        # - Multiple conditions
        # - When readability is important
        
        # Use ternary for:
        # - Simple conditions
        # - Assignment operations
        # - When conciseness is important
        
        # Use dictionary lookup for:
        # - Many cases
        # - When performance is important
        # - When cases are simple mappings
        
        # Use functions for:
        # - Complex logic
        # - When reusability is important
        # - When testing is important

common_pitfalls()
```

**When to Use Each:**

**Use If/Else When:**
- You have complex conditions
- You need multiple conditions
- Readability is more important than conciseness
- You need to handle edge cases
- You have complex logic

**Use Ternary When:**
- You have simple conditions
- You need concise assignment
- The condition is easy to understand
- You want to avoid verbose code
- You're working with simple values

**Use Switch-Like Patterns When:**
- You have many cases
- Performance is important
- Cases are simple mappings
- You want to avoid long if/elif chains
- You need to add/remove cases easily

**Use Match Statements When:**
- You're using Python 3.10+
- You need pattern matching capabilities
- You're working with complex data structures
- You want to match against multiple patterns
- You need guard clauses with conditions
- You want more expressive control flow

**Pro Tip:** Choose the control flow pattern that **best fits your use case**. Use if/else for complex logic, ternary for simple conditions, switch-like patterns for multiple cases, and match statements for pattern matching (Python 3.10+).

---

## 💡 Pro Tip
> **Choose the control flow pattern that best fits your use case. Use if/else for complex logic, ternary for simple conditions, switch-like patterns for multiple cases, and match statements for pattern matching (Python 3.10+).**

---

## 💬 Reference Links

* [Python Docs – Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
* [RealPython – Python Control Flow](https://realpython.com/python-conditional-statements/)
* [GeeksForGeeks – Control Flow](https://www.geeksforgeeks.org/python-if-else/)
* [StackOverflow – Switch Statement in Python](https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python)

---

 
