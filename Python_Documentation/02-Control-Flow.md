# Concept 2: Control Flow (If-Elif & Match-Case)

## 1\. Deep Explanation (The Logic)

By default, code runs linearly: line 1, then line 2, then line 3.
**Control Flow** allows the program to make decisions and "branch" into different paths based on the current situation.

There are two main tools for this in Python:

  * **If / Elif / Else:** Checks a **Boolean Condition** (True or False). It is used for complex logic, ranges, or multiple variables.
      * *Logic:* "Is the distance less than 5? If yes, stop."
  * **Match / Case:** Checks a **Discrete Value** (Pattern Matching). It compares a single variable against a list of specific "labels" (Cases). *Note: This was introduced in Python 3.10.*
      * *Logic:* "What is the current gear? Is it 1, 2, or R?"

-----

## 2\. Why do we use it?

  * **Reactivity:** A robot without control flow is just a scripted machine. Control flow allows the robot to react to sensors (e.g., "If obstacle detected, turn left").
  * **State Management:** Robots often have states (Idle, Docking, Charging). **Match Cases** are the standard way to organize these distinct behaviors.

-----

## 3\. Syntax & Rules

### A. If / Elif / Else

Used when conditions are ranges (`<`, `>`) or complex logic (`and`, `or`).
**Crucial Rule:** Python uses **Indentation** (spaces/tabs) to define blocks of code, not curly braces.

```python
if condition:
    # Runs if true (Indented block)
    pass
elif other_condition:
    # Runs if first is false AND this is true
    pass
else:
    # Runs if everything else is false
    pass
```

### B. Match / Case (The Modern "Switch")

Used when checking a single variable against specific values.

  * **Safety:** Unlike older languages, Python's `match` statement **does not** "fall through". You do not need a `break` keyword. Once a match is found, it runs that code and exits the block automatically.
  * **Default:** The case `case _:` acts as the "Default" or "Else" catch-all.

<!-- end list -->

```python
match variable:
    case 1:
        # Code for 1
    case 2:
        # Code for 2
    case _:
        # Default (Runs if no other case matches)
```

-----

## 4\. The "Trap": Indentation & Fall-Through ⚠️

### The "Forgotten Break" (Fixed in Python)

In many older languages, if you forget to tell the code to stop inside a switch case, it keeps running the next case automatically (a bug called "fall-through").
**Python protects you from this.** In a `match` statement, Python automatically stops after one successful case.

### The Real Python Trap: Indentation

Because Python relies on spaces to know what code belongs where, a single wrong space can break your logic.

  * **Scenario:** You have an `if` statement for "Obstacle Detected".
  * **Bug:** You accidentally un-indent the "Stop Motors" line.
  * **Result:** The robot "Stops Motors" **every time**, regardless of whether there is an obstacle or not, because that line is no longer part of the `if` block.

-----

## 5\. Code Example

```python
robot_mode = 2       # 1=Idle, 2=Auto, 3=Manual
battery_level = 15.5

# --- Part 1: Match (State Management) ---
# We check a specific integer value
match robot_mode:
    case 1:
        print("State: IDLE. Waiting...")

    case 2:
        print("State: AUTONOMOUS DRIVING.")
        
        # --- Part 2: If-Else (Logic Check inside a case) ---
        # We check a range/condition
        if battery_level < 20.0:
            print("WARNING: Low Battery! Returning to dock.")
        else:
            print("Battery OK. Continuing mission.")
            
    case 3:
        print("State: MANUAL CONTROL.")

    case _:
        print("ERROR: Unknown Mode ID!")
```

-----

## 6\. ROS2 Context: "State Machines & Callbacks"

1.  **Lifecycle Management:** ROS2 nodes have a specific "Lifecycle" (Unconfigured, Inactive, Active, Finalized). Developers use **Match Cases** (or if/elif chains in older Python) to handle what the node should do in each state.
2.  **Subscriber Logic:** Inside a callback function (when data arrives), you use **If-Else** to filter bad data.
      * *Example:* "If the Lidar gives a value of `float('inf')` (infinity), ignore it. Else, process it."

-----

## 7\. Task: The "Robot Gearbox" ✅

**Scenario:**
You are writing the transmission logic for a rover. The rover has a variable `gear` (string) and a variable `speed` (float).

**Requirements:**

1.  Define `gear = "D"` (Options: "P" for Park, "D" for Drive, "R" for Reverse).
2.  Define `speed = 0.0`.
3.  **The Logic Puzzle:**
    Use a **Match Statement** to check the gear.
      * **Case "P":** Set speed to 0. Print "Parking".
      * **Case "D":** Set speed to 10. Print "Driving Forward".
      * **Case "R":** Set speed to -5. Print "Reversing".
      * **Case \_ (Default):** Set speed to 0. Print "Error: Unknown Gear".

**Verification:**
Unlike older languages, you don't need to add `break`. Run the code and verify that it prints "Driving Forward" and the speed is 10. It should **not** print "Reversing".

```python
gear = "D"
speed = 0.0

match gear:
    case "P":
        speed = 0.0
        print("Parking")
    case "D":
        speed = 10.0
        print("Driving Forward")
    case "R":
        speed = -5.0
        print("Reversing")
    case _:
        speed = 0.0
        print("Error: Unknown Gear")

print(f"Final Speed: {speed}")
```
