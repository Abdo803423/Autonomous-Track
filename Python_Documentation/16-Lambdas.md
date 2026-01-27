
# Concept 16: Lambdas (Anonymous Functions)

## 1. Deep Explanation (The Logic)
A **Lambda** is a function that has **no name**.

* **The Old Way:** If you want a small calculation, you define `def calculate_area(): ...` at the top of your file.
* **The Modern Way:** With a Lambda, you write the function logic **inline**, right at the spot where it is needed.

### Structure: `lambda arguments: expression`



1.  **`lambda` Keyword:** Tells Python "I am creating a function right now."
2.  **Arguments:** Just like `def` (e.g., `x, y`), but without parentheses.
3.  **Expression:** A **single line** of code that is automatically returned.

> **Limitation:** Python lambdas are restricted to **one single expression**. You cannot write multiple lines, loops, or complex if/else blocks inside them (though simple `if/else` works).

---

## 2. Why do we use it?
1.  **Short & Sweet:** If a function does a simple math operation (`x + y`), writing a full `def` block takes up 2-3 lines unnecessarily.
2.  **Callbacks:** When passing a function as an argument to another function (like sorting rules or GUI button clicks), a lambda allows you to define the behavior right there.
3.  **Access to Scope:** Like standard functions, lambdas automatically see variables in the surrounding code (Closure).

---

## 3. Syntax & Rules

### A. Basic Lambda
```python
# Instead of:
# def add(a, b):
#     return a + b

# We write:
add = lambda a, b: a + b

print(f"Sum: {add(5, 3)}") # Prints 8

```

### B. Capturing Variables (The Closure)

Lambdas automatically "see" variables defined outside of them.

```python
threshold = 10

# This lambda uses 'x' (argument) and 'threshold' (outside variable)
check = lambda x: x > threshold 

print(check(5))  # False
print(check(15)) # True

```

---

## 4. The Trap: "Late Binding" ⚠️

This is a famous Python interview question and a common bug.

* **The Bug:** You create lambdas inside a loop.
* **The Reality:** Python looks up the variable **when the lambda runs**, not when it is created.
* **Result:** All lambdas might end up using the **last value** of the loop variable.

```python
funcs = []
for i in range(3):
    # Bug: 'i' is looked up later. By then, i is 2.
    funcs.append(lambda: i) 

print(funcs[0]()) # Prints 2 (Expected 0)
print(funcs[2]()) # Prints 2 (Expected 2)

```

**The Fix:** Force early binding by setting a default argument: `lambda x=i: x`.

---

## 5. Code Example

```python
# --- 1. Simple Lambda ---
# A function that squares a number
square = lambda x: x * x
print(f"Square of 5: {square(5)}")

# --- 2. Using Lambda with Built-in Functions ---
readings = [10, 80, 30, 90, 40]
threshold = 50

print(f"--- Filtering Readings > {threshold} ---")
# 'filter' takes a function and a list.
# We define the logic inline: "Keep x if x > threshold"
high_values = list(filter(lambda x: x > threshold, readings))

print(f"High Values: {high_values}")

# --- 3. Complex Sorting ---
# Sort a list of tuples based on the SECOND number (Index 1)
robots = [("Rover", 50), ("Drone", 90), ("Arm", 20)]

# Sort key: lambda item: item[1] (The speed)
sorted_robots = sorted(robots, key=lambda item: item[1])

print(f"Sorted by Speed: {sorted_robots}")

```

---

## 6. ROS2 Context: "The Inline Timer"

In ROS2 Python, you typically don't use lambda for complex callbacks because callbacks usually need multiple lines of logic. However, you often see them for simple parameter passing.

```python
# Scenario: You have a button callback that needs an ID, 
# but the standard callback doesn't accept arguments.

button_1.on_click(lambda: self.handle_click(1))
button_2.on_click(lambda: self.handle_click(2))

# Here, the lambda acts as a bridge to call the real function with specific data.

```

---

## 7. Task: "The Custom Sorter" ✅

**Scenario:**
You have a list of robot speeds. You want to sort them, but not just typically (Low to High). You want to sort them **High to Low** (Fastest first).

**Requirements:**

1. Define a list: `speeds = [1.5, 5.5, 0.5, 3.2]`.
2. **The Logic Puzzle:**
* Use the `sorted()` function or `.sort()` method.
* Both accept a `key` argument.
* **Challenge:** Do **NOT** use `reverse=True`. Instead, use a **lambda** for the key.
* *Hint: If you sort by the negative of the number (`-x`), the largest number becomes the smallest (most negative), so it appears first.*


3. **Output:** Print the sorted list.

**Expected Result:**
`[5.5, 3.2, 1.5, 0.5]`

*Goal: This proves you can inject custom logic into standard algorithms using Lambdas.*
