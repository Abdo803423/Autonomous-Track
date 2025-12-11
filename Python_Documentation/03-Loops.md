# Concept 3: Loops (Iteration) & Arrays

## 1. Deep Explanation (The Logic)
Before we talk about **Loops**, we need to understand an **Array**.

* **Array:** Imagine you have 5 sensors. Instead of creating `sensor1`, `sensor2`, `sensor3`, ..., you create **one list** called `sensors` that holds 5 numbers.
* **Loop:** A tool that allows you to repeat a block of code. It is mostly used to "walk through" an array, checking one item at a time.



**The Three Types:**
1.  **Standard `for` loop:** You act like a **counter**. "Start at 0, count up to 10, and do this action every time."
2.  **`while` loop:** You act like a **watchman**. "Keep doing this **while** the condition is true." (Used for waiting).
3.  **Range-based `for` loop:** The modern shortcut. It says: "For every item inside this list, do X."

---

## 2. Why do we use it?
* **Efficiency:** If a robot has 1000 scan points from a laser, we cannot write 1000 lines of code. We write **one loop** that runs 1000 times.
* **Waiting:** We use `while` loops to pause the robot logic until a specific event happens (e.g., "Wait while the system is connecting").

---

## 3. Syntax & Rules

### A. The Array (The List)
```cpp
// Type name[size] = {values};
int readings[3] = {10, 20, 30};
````

### B. Standard For Loop (The Counter)

Used when you need the **index number** (0, 1, 2...).

```cpp
// Start at 0; Keep going if i < 3; Increase i by 1
for (int i = 0; i < 3; i++) {
    // Access array using index [i]
    std::cout << readings[i]; 
}
```

### C. While Loop (The Waiter)

```cpp
while (battery < 5) {
    charge(); // Repeats forever until battery >= 5
}
```

### D. Range-based For Loop (The Shortcut)

Used when you just want to check every item in a list and don't care about the index number.

  * **`auto`**: Tells C++ "You figure out the type (int/double) automatically."

<!-- end list -->

```cpp
// "For each 'number' inside 'readings'..."
for (auto number : readings) {
    std::cout << number;
}
```

-----

## 4\. The Trap: "The Infinite Loop" ⚠️

A loop must always have an **exit condition**.

  * **The Bug:** If you write `while(true)` or a condition that never becomes false, the program gets stuck there forever.
  * **Consequence:** The robot freezes, stops reading sensors, and stops listening to safety commands.

-----

## 5\. Code Example

```cpp
#include <iostream>

int main() {
    // 1. Setup a simple list of sensor data (Array)
    double sensor_data[4] = {1.2, 5.5, 0.4, 9.1};

    // --- Type 1: Range-Based Loop (Cleanest) ---
    std::cout << "--- Reading Sensors ---\n";
    // "val" will automatically become 1.2, then 5.5, etc.
    for (auto val : sensor_data) {
        if (val > 5.0) {
            std::cout << "Far Object: " << val << "\n";
        }
    }

    // --- Type 2: Standard For Loop (Index Based) ---
    // Use this if you need to know WHICH sensor triggered (0, 1, 2...)
    for (int i = 0; i < 4; i++) {
        if (sensor_data[i] < 1.0) {
            std::cout << "CRITICAL: Obstacle at sensor index [" << i << "]\n";
        }
    }

    // --- Type 3: While Loop ---
    int retry_count = 0;
    while (retry_count < 3) {
        std::cout << "Trying to connect... Attempt " << retry_count << "\n";
        retry_count++; // Important! If you forget this, it loops forever.
    }

    return 0;
}
```

-----

## 6\. ROS2 Context: "Handling Laser Scans"

In ROS2, data rarely comes as a single number. It almost always comes as a **List (Array)**.

  * **Example:** A `LaserScan` message contains a list of 360 distances (one for every degree).
  * **The Workflow:**
    1.  The message arrives.
    2.  You use a **Loop** to iterate through all 360 numbers.
    3.  You check: *"Is any of these numbers less than 0.5 meters?"*
    4.  If yes, you stop the robot.

-----

## 7\. Task: The "Average Temperature" ✅

**Scenario:**
You have an array representing the temperature of 5 battery cells. You need to calculate the **average temperature** to see if the battery pack is overheating.

**Given Data:**

  * Array: `double temps[5] = {35.5, 30.0, 32.2, 40.0, 38.1};`
  * Variable: `double sum = 0.0;`

**Requirements:**

1.  Define the array and the sum variable.
2.  **The Logic Puzzle:**
      * Use a **Range-based for loop** (`for (auto t : temps)`) to visit every number.
      * Inside the loop, add `t` to `sum`.
      * After the loop finishes, calculate the average (`sum / 5`).
3.  **Output:** Print the Average Temperature.

**Verification:**

  * The sum is `175.8`.
  * The average should be `35.16`.
  * *Why this matters:* This is exactly how we filter noisy sensor data (Moving Average Filter).
