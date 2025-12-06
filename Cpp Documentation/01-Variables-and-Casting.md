# Concept 1: Variables, Data Types & Casting

## 1. Deep Explanation (The Logic)
In C++, a variable is a specific reserved space in the **Memory (RAM)** used to store data.
Unlike some languages (like Python) where a variable can hold anything, C++ is **Statically Typed**. This means you must decide exactly what kind of data you will store—and how much memory it needs—before the program runs.

Think of Memory like a warehouse full of specific-sized boxes:
* **`int` (Integer):** A standard box (4 Bytes). It stores whole numbers only. It completely ignores/deletes decimal points.
* **`double` (Double Precision):** A large, reinforced box (8 Bytes). It stores decimal numbers. It is designed for high-precision physics.
* **`bool` (Boolean):** A tiny box (1 Byte). Stores only `true` (1) or `false` (0).
* **`string`:** A dynamic box that grows to hold text characters.

---

## 2. The Problem: "Integer Math"
Because C++ is strict about these "boxes," it follows a strict math rule: **Integer divided by Integer equals Integer.**

If you try to divide `5 / 2` in C++:
1.  The computer sees two Integers.
2.  It calculates `2.5`.
3.  **The Trap:** Because the result must fit back into an Integer box, it deletes the `.5` immediately.
4.  The result becomes `2`.

> ⚠️ **Major Issue in Robotics:** If your robot moves 0.9 meters, an Integer variable will see 0 meters, causing the robot to stop unexpectedly.

---

## 3. The Solution: Type Casting
To solve the Integer Math problem without changing the variable type globally, we use **Casting**.
Casting is the act of *forcing* the computer to treat a variable as a different type temporarily for a single calculation.

* **Syntax:** `static_cast<NEW_TYPE>(VARIABLE)`
* **Usage:** If we cast one of the numbers to a `double`, the computer switches to "Decimal Math," and the result will be preserved correctly (2.5).

---

## 4. Code Example

```cpp
#include <iostream>
#include <string>

int main() {
    // --- 1. Defining Strict Types ---
    int encoder_ticks = 150;      // Whole number (Count)
    int max_ticks = 1000;         // Whole number (Constant)
    std::string motor_id = "M1";  // Text

    // --- 2. The Problem (Integer Math) ---
    // 150 / 1000 should be 0.15.
    // However, C++ cuts the decimal because both are ints.
    double wrong_result = encoder_ticks / max_ticks; // Result: 0.0 (Data Lost!)

    // --- 3. The Solution (Casting) ---
    // We force 'encoder_ticks' to be treated as a Double strictly for this line.
    // The equation becomes: 150.0 / 1000
    double correct_result = static_cast<double>(encoder_ticks) / max_ticks; // Result: 0.15

    // Output
    std::cout << "Motor: " << motor_id << "\n";
    std::cout << "Wrong (Int Math): " << wrong_result << "\n";
    std::cout << "Correct (Casting): " << correct_result << "\n";

    return 0;
}
```
-----

## 5\. ROS2 Context: "The Data Contract"

In ROS2, independent nodes (like a Camera Node and a Motor Node) talk to each other. They do this by agreeing on a strict Contract called a **Message (.msg)**.

You don't need to write ROS2 code yet, but you must understand the mapping:

1.  **The Contract:** If the message file says the speed is a `float64`, your C++ code must provide a `double`.
2.  **The Bridge:** Often, your hardware gives you `int` data (raw sensor ticks), but the ROS2 message requires `float64` (physical speed).
3.  **Your Job:** You act as the bridge. You take the `int` from the hardware, use **Casting** to convert it to a `double`, and then send it to the ROS2 system.

**Common Mapping:**

  * C++ `double` ↔ ROS2 `float64` (Standard for Physics).
  * C++ `int` ↔ ROS2 `int32`.

-----

## 6\. Task: The "Distance Sensor" Logic ✅

**Scenario:**
You have an ultrasonic sensor. It measures the time (in microseconds) it takes for sound to bounce back. You need to convert this time into a distance in Meters.

**Given Data:**

```cpp
int time_microseconds = 5882;
```

**Conversion Formula:** $Distance (cm) = Time / 58$

**Requirements:**

1.  Define the variable `time_microseconds`.
2.  **The Logic Puzzle:**
      * Calculate the distance in centimeters. Be careful: if you just write `time / 58`, you might lose precision because both are Integers.
      * Convert that result to meters (divide by 100).
      * Store the final result in a variable named `distance_meters`.
3.  **Constraint:** You must use `static_cast<double>(...)` to ensure the decimal precision is kept throughout the calculation.
4.  Print the result. *(The correct answer is approx 1.014 meters. If you get 1.0 or 0, check your casting)*.

<!-- end list -->
