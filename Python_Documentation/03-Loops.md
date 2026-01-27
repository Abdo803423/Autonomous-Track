
# Concept 3: Loops (Iteration) & Lists

## 1. Deep Explanation (The Logic)

Before we talk about **Loops**, we need to understand a **List**.

* **List:** Imagine you have 5 sensors. Instead of creating `sensor1`, `sensor2`, `sensor3`, ..., you create **one collection** called `sensors` that holds 5 numbers.
* **Loop:** A tool that allows you to repeat a block of code. It is mostly used to "walk through" a list, checking one item at a time.

**The Main Types:**

1. **For Loop (Item-Based):** This is the standard in Python. It says: "For every item inside this list, do X."
2. **While Loop:** You act like a **watchman**. "Keep doing this **while** the condition is true." (Used for waiting).
3. **For Loop (Index-Based):** Used when you need to know the *position* number (0, 1, 2...) rather than just the value. We use the `range()` function for this.

---

## 2. Why do we use it?

* **Efficiency:** If a robot has 1000 scan points from a laser, we cannot write 1000 lines of code. We write **one loop** that runs 1000 times.
* **Waiting:** We use `while` loops to pause the robot logic until a specific event happens (e.g., "Wait while the system is connecting").

---

## 3. Syntax & Rules

### A. The List

Python lists are dynamic—you don't need to specify the size or type beforehand.

```python
# variable_name = [values]
readings = [10, 20, 30]

```

### B. Standard For Loop (The "For-Each" Loop)

This is the modern shortcut logic. You don't manage a counter; Python handles it for you.

```python
# "For each 'number' inside the 'readings' list..."
for number in readings:
    print(number)

```

### C. While Loop (The Waiter)

```python
while battery < 5:
    charge() # Repeats forever until battery >= 5

```

### D. Index Loop (The Counter)

If you specifically need the index number (0, 1, 2...), use `range()`.

* `len(readings)` gives the size of the list (e.g., 3).
* `range(3)` creates a sequence: 0, 1, 2.

```python
# Start at 0; Keep going up to the length of readings
for i in range(len(readings)):
    # Access list using index [i]
    print(readings[i])

```

---

## 4. The Trap: "The Infinite Loop" ⚠️

A loop must always have an **exit condition**.

* **The Bug:** If you write `while True:` or a condition that never becomes `False`, the program gets stuck there forever.
* **Consequence:** The robot freezes, stops reading sensors, and stops listening to safety commands.

---

## 5. Code Example

```python
# 1. Setup a simple list of sensor data
sensor_data = [1.2, 5.5, 0.4, 9.1]

# --- Type 1: Standard Loop (Cleanest) ---
print("--- Reading Sensors ---")
# "val" will automatically become 1.2, then 5.5, etc.
for val in sensor_data:
    if val > 5.0:
        print(f"Far Object: {val}")

# --- Type 2: Index Based Loop ---
# Use this if you need to know WHICH sensor triggered (Index 0, 1, 2...)
# len(sensor_data) is 4. range(4) creates 0, 1, 2, 3.
for i in range(len(sensor_data)):
    if sensor_data[i] < 1.0:
        print(f"CRITICAL: Obstacle at sensor index [{i}]")

# --- Type 3: While Loop ---
retry_count = 0
while retry_count < 3:
    print(f"Trying to connect... Attempt {retry_count}")
    retry_count += 1 # Important! If you forget this, it loops forever.

```

---

## 6. ROS2 Context: "Handling Laser Scans"

In ROS2, data rarely comes as a single number. It almost always comes as a **List**.

* **Example:** A `LaserScan` message contains a list called `ranges` with 360 distances (one for every degree).
* **The Workflow:**
1. The message arrives.
2. You use a **For Loop** to iterate through all 360 numbers in the list.
3. You check: *"Is any of these numbers less than 0.5 meters?"*
4. If yes, you stop the robot.



---

## 7. Task: The "Average Temperature" ✅

**Scenario:**
You have a list representing the temperature of 5 battery cells. You need to calculate the **average temperature** to see if the battery pack is overheating.

**Given Data:**

* List: `temps = [35.5, 30.0, 32.2, 40.0, 38.1]`
* Variable: `total_sum = 0.0`

**Requirements:**

1. Define the list and the sum variable.
2. **The Logic Puzzle:**
* Use a **Standard For loop** (`for t in temps:`) to visit every number.
* Inside the loop, add `t` to `total_sum`.
* After the loop finishes, calculate the average (`total_sum / 5` or `total_sum / len(temps)`).


3. **Output:** Print the Average Temperature.

**Verification:**

* The sum is `175.8`.
* The average should be `35.16`.
* *Why this matters:* This is exactly how we filter noisy sensor data (Moving Average Filter).
