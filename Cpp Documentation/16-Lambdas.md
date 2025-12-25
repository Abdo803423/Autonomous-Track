
# Concept 16: Lambdas (Anonymous Functions)

## 1. Deep Explanation (The Logic)
A **Lambda** is a function that has **no name**.

* **The Old Way:** If you want a function to handle a button press, you define `void onButtonPress() {...}` at the top of your file.
* **The Modern Way:** With a Lambda, you write the function logic **inline**, right at the spot where it is needed.



### Structure: `[]() { ... }`
1.  **`[]` Capture Clause:** Determines what variables from the "outside world" the lambda can see.
2.  **`()` Parameters:** Just like a normal function (e.g., `int x`).
3.  **`{}` Body:** The code to execute.

---

## 2. Why do we use it?
1.  **Cleaner Code:** If a function is only used once (like a sort condition or a specific timer), why pollute your class with a separate named function? Just write it where you use it.
2.  **Access to Local Variables:** Normal functions cannot see variables inside `main()`. Lambdas can **"Capture"** them, allowing you to use local data inside a callback easily.

---

## 3. Syntax & Rules

### A. Basic Lambda
```cpp
auto say_hello = []() {
    std::cout << "Hello directly from Lambda!\n";
};
say_hello(); // Calls the code

```

### B. The Capture Clause `[...]`

The code inside `{}` is isolated. The `[]` is the bridge to the outside.

* **`[]`**: No access to outside variables (Isolated).
* **`[&]`**: Access everything by **Reference** (Dangerous but powerful).
* **`[=]`**: Access everything by **Copy** (Safe, read-only).
* **`[this]`**: Access **class member variables** (Crucial for ROS2).

---

## 4. The Trap: "The Dangling Reference" ⚠️

If you use `[&]` to capture a local variable by reference, and then the lambda runs **after** that variable has been destroyed (e.g., inside a timer), the program will crash.

* **Fix:** In async callbacks, usually capture by value `[=]` or be very careful about lifetime.

---

## 5. Code Example

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // For std::sort

int main() {
    // 1. Simple Lambda
    // We assign the function to a variable named 'add'
    auto add = [](int a, int b) {
        return a + b;
    };
    std::cout << "Sum: " << add(5, 3) << "\n";

    // 2. Capturing Variables
    int threshold = 50;
    std::vector<int> readings = {10, 80, 30, 90, 40};

    std::cout << "--- Filtering Readings > " << threshold << " ---\n";

    // "for_each" loops through the list. 
    // We pass a Lambda to define what to do with each item.
    // We use [threshold] to let the lambda see our local variable.
    std::for_each(readings.begin(), readings.end(), [threshold](int val) {
        if (val > threshold) {
            std::cout << "High Value: " << val << "\n";
        }
    });

    return 0;
}

```

---

## 6. ROS2 Context: "The Inline Timer"

In ROS2, creating a timer often looks like this. Instead of creating a separate function `timer_callback`, we put the logic right inside the create function.

```cpp
// Create a wall timer that runs every 500ms
timer_ = this->create_wall_timer(
    500ms, 
    [this]() {  // Lambda starts here
        // We captured [this], so we can use the Node's logger and publishers
        RCLCPP_INFO(this->get_logger(), "Timer Tick!"); 
        this->publish_data();
    }           // Lambda ends here
);

```

*Note the `[this]` capture: It allows the lambda to access the Node's functions like `publish_data`.*

---

## 7. Task: "The Custom Sorter" ✅

**Scenario:**
You have a list of robot speeds. You want to sort them, but not just typically (Low to High). You want to sort them **High to Low** (Fastest first).

**Requirements:**

1. Create a vector: `{1.5, 5.5, 0.5, 3.2}`.
2. **The Logic Puzzle:**
* Use `std::sort(begin, end, comparison_function)`.
* Instead of a normal function, pass a **Lambda** as the 3rd argument.
* The lambda takes two floats (`float a, float b`) and returns `true` if `a > b` (this triggers the High-to-Low sort).



**Output:**
Print the sorted list.

**Expected Result:**
`5.5, 3.2, 1.5, 0.5`

*Goal: This proves you can inject custom logic into standard algorithms using Lambdas.*
