
# Concept 13: Scope & Lifetime (The LEGB Rule)

**Note:** This concept is where Python behaves **very differently** from many other strict languages (like C++).

## 1. Deep Explanation (The Logic)

While **Scope** and **Lifetime** are related, they are not the same thing.

### Scope (Visibility - "The View") 👀
* **Definition:** The region of the code where you can **see and use** a variable by its name.
* **Python's Unique Rule:** Unlike other languages where curly braces `{ }` define a private scope, Python uses the **LEGB Rule**:
    1.  **L**ocal (Inside a function)
    2.  **E**nclosing (Nested functions)
    3.  **G**lobal (Top level)
    4.  **B**uilt-in (Python keywords)



### Lifetime (Duration - "The Pulse") 💓
* **Definition:** The time period during which the object actually **exists in Memory (RAM)**.
* **Rule:** An object stays alive as long as **at least one variable** (in a valid scope) is pointing to it.

---

## 2. The Big Difference: "No Block Scope" ⚠️

This is the biggest shock for new Python developers coming from C++.

* **In Strict Languages:** If you define a variable inside an `if` block or a `for` loop, it is destroyed when the block ends.
* **In Python:** Variables defined inside `if`, `for`, or `while` blocks **leak out** into the surrounding function. They remain visible and alive even after the loop finishes.



---

## 3. Syntax & Rules

### A. Local Scope (Function Scope)
Variables created inside a function are private to that function.

```python
def my_func():
    x = 100  # Local Scope
    print(x)

# print(x) # ERROR! 'x' is not visible here.

```

### B. The "Leak" (Loop Scope)

Variables inside loops are **NOT** private.

```python
for i in range(3):
    secret = 99

# SURPRISE: Both 'i' and 'secret' are still alive and visible here!
print(i)      # Prints 2
print(secret) # Prints 99

```

### C. Static Lifetime (The Python Way) ⚡

Python does not have a `static` keyword for variables inside functions.
To simulate a variable that "remembers" its value between function calls (like a static variable), we use a **Class** and `self`.

```python
class Counter:
    def __init__(self):
        self.count = 0  # Persists as long as the Object is alive

    def increment(self):
        self.count += 1

```

---

## 4. The Trap: "UnboundLocalError" ⚠️

This happens when you try to modify a **Global** variable inside a **Local** scope without permission.

* **Scenario:** You have a global `score = 0`. Inside a function, you write `score += 1`.
* **The Crash:** Python assumes `score` is local because you are writing to it, but then realizes you haven't defined it locally yet.
* **The Fix:** Use the `global` keyword (though in Robotics, we prefer using Classes instead).

---

## 5. Code Example

```python
# 1. Global Scope
global_config = "192.168.1.1"

def show_scope_leak():
    # 2. Local Scope (The "Leak" Demo)
    print("--- Inside Function ---")
    
    # In other languages, 'temp_val' would die after this loop.
    # In Python, it stays alive.
    for i in range(3):
        temp_val = i * 10
    
    print(f"Loop finished, but I can still see temp_val: {temp_val}")

class CallCounter:
    # 3. Simulating "Static" behavior using a Class
    def __init__(self):
        self.count = 0 
        
    def click(self):
        self.count += 1
        print(f"Function called {self.count} times.")

# --- Main Execution ---
print(f"Global: {global_config}")

show_scope_leak()
# print(temp_val) # ERROR! The leak stops at the function border.

print("\n--- Static Behavior Test ---")
# We create an object to hold the 'memory' of the count
tracker = CallCounter()
tracker.click() # Prints 1
tracker.click() # Prints 2
tracker.click() # Prints 3

```

---

## 6. ROS2 Context: "The Callback Trap"

In ROS2, beginners often try to save data in a simple variable inside a callback function.

**Bad Code (Variable resets every time):**

```python
def timer_callback(self):
    counter = 0  # Local variable created NEW every time
    counter += 1
    # Result: Counter is ALWAYS 1. It never counts up.

```

**The Fix (Class Attribute):**
You must make `counter` a member of the class (`self.counter`).

```python
class MyNode(Node):
    def __init__(self):
        self.counter = 0 # Created once when Node starts

    def timer_callback(self):
        self.counter += 1 # Remembers value from last time

```

---

## 7. Task: "The Scope Test" ✅

**Scenario:**
You need to verify exactly when variables die in Python. Since `if` blocks don't kill variables, we must use a **Function** to create a limited scope.

**Requirements:**

1. Create a class `Tracker`.
* **Constructor:** Print "Tracker Born".
* **Destructor (`__del__`):** Print "Tracker Died".


2. **In Main:**
* Print "Start".
* Define a function `def test_scope():`.
* Inside the function, create a `Tracker` object named `t1`.
* Print "Inside Scope".
* Call the function.
* Print "End".



**Observation:**
Does "Tracker Died" print **before** "End"?

* **Note:** Because `test_scope` is a function, `t1` is a Local Variable. When the function finishes, the Local Scope is destroyed, `t1` disappears, the Reference Count hits 0, and the object dies.
* **Contrast:** If you just indented `t1` inside an `if True:` block in the main script, it would **not** die.

*Goal: Understand that Functions are the primary boundary for variable lifetime in Python.*
