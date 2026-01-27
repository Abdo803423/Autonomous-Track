
# Concept 20: Modules & Imports (Splitting Files)

## 1. Deep Explanation (The Logic)
In Python, we don't have separate Header (`.hpp`) and Source (`.cpp`) files like in C++. Instead, we use **Modules** and **Packages**.

So far, we have written everything in one file.
In a real robot, the code is massive (thousands of lines). If you put it all in one script, it becomes unreadable.

We split code into two types of files:



### A. The Module (`robot_lib.py`): The Tool 🛠️
* **Content:** Class definitions and functions.
* **Function:** It contains the logic (the "Recipe"), but it **does not run itself**. It sits there waiting to be used.
* **Analogy:** A **Dictionary**. You don't read it cover to cover; you look up words when you need them.

### B. The Script (`main.py`): The Worker 👷
* **Content:** Imports and Execution logic.
* **Function:** It pulls tools from the Module and actually **does the work**.
* **Analogy:** The **Writer**. The writer uses the Dictionary (Module) to write a story.

---

## 2. Why do we use it?
1.  **Organization:** You separate the "What" (The Robot Class) from the "When" (The logic that starts the robot).
2.  **Reusability:** You can write a `Lidar` module **once**. Then, 5 different robots can import that same file and use it. You don't copy-paste code.

---

## 3. Syntax & Rules

### Step 1: The Module (`calculator.py`)
This file just defines the tools. Note the special `if` block at the bottom.

```python
# This file is named 'calculator.py'

class Calculator:
    def add(self, a, b):
        return a + b

# --- Safety Guard ---
# This block runs ONLY if you run this file directly.
# It does NOT run if you Import this file into another script.
if __name__ == "__main__":
    print("This is a library. Please run main.py instead.")

```

### Step 2: The Script (`main.py`)

You import the filename (without `.py`) to use the class.

```python
# This file is named 'main.py'

# Syntax: from [Filename] import [ClassName]
from calculator import Calculator

def main():
    calc = Calculator()
    result = calc.add(5, 5)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

```

---

## 4. The Trap: "Circular Imports" ⚠️

* **The Bug:** File A imports File B. File B imports File A.
* **The Result:** Python gets stuck in an infinite loop trying to load the files and crashes with `ImportError`.
* **The Fix:** Structure your code like a **Tree**, not a Circle. Main imports A and B. But A and B should ideally not import each other.

---

## 5. ROS2 Context: "The Python Package Structure"

Every ROS2 Python package follows this structure.

```plaintext
my_robot_pkg/
├── package.xml
├── setup.py           (Tells ROS2 how to install your code)
└── my_robot_pkg/      (The Source Folder)
    ├── __init__.py    (Marks this folder as a Package)
    ├── my_node.py     (Your Node Class Logic)
    └── utils.py       (Helper functions)

```

**The Entry Point:**
In `setup.py`, you tell ROS2: *"When I run `ros2 run my_pkg start`, please go to `my_node.py` and run the `main()` function."*

---

## 6. Task: "The File Splitter" ✅

**Scenario:**
You have a math helper class. You need to separate the logic from the execution.

**Requirements:**

**1. Create a file named `my_math.py`:**

* Define a class `MathHelper`.
* Add a method `multiply(a, b)` that returns the product.

**2. Create a file named `app.py`:**

* Import the `MathHelper` class.
* Create an object.
* Print the result of `multiply(10, 5)`.

**Goal:**

* Run `python app.py`. It should work perfectly.
* If you run `python my_math.py`, nothing should happen (or it should print a safety message if you added the `if __name__` block).
