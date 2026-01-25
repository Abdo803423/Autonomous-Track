
# Concept 19: Namespaces (::)

## 1. Deep Explanation (The Logic)
Imagine a school with two students named "Ahmed".
* If the teacher calls out *"Ahmed!"*, both students look up. Confusion happens. 😕
* To fix this, we use their **Family Names**: "Ahmed **Ali**" vs. "Ahmed **Mohamed**".

**Namespaces** are the "Family Names" for your code.



### The Problem:
You write a function `connect()` for your Wi-Fi. You download a library for Bluetooth that *also* has a function named `connect()`. The compiler panics because it doesn't know which one to pick.

### The Solution:
You wrap your code in a namespace. Now you have `Wifi::connect()` and `Bluetooth::connect()`.

* **The Symbol (`::`):** This is called the **Scope Resolution Operator**. It translates to *"Belongs to"*.

---

## 2. Why do we use it?
1.  **Collision Prevention:** In a robot, you might have Motor control for the wheels and Motor control for a robotic arm. Namespaces (`Wheels::Motor` vs `Arm::Motor`) keep them separate.
2.  **Organization:** ROS2 is massive. It organizes code into logical groups:
    * `std::` $\rightarrow$ Standard C++ Tools.
    * `rclcpp::` $\rightarrow$ ROS Client Library Tools.
    * `sensor_msgs::` $\rightarrow$ Sensor Data Tools.

---

## 3. Syntax & Rules

### A. Creating a Namespace
You wrap your variables and functions inside a `namespace` block.
```cpp
namespace RobotArm {
    int speed = 50;
    void move() { ... }
}

```

### B. Accessing the Code

You must use the `::` operator from outside.

```cpp
RobotArm::move();
int s = RobotArm::speed;

```

### C. The `using` Keyword (The Shortcut)

If you get tired of typing `RobotArm::`, you can write:

```cpp
using namespace RobotArm;
move(); // Now works without the prefix

```

* **Warning:** Use this carefully! If you use `using namespace std;`, you dump thousands of names into your code, increasing the risk of collision.

---

## 4. Code Example

```cpp
#include <iostream>

// --- Family 1: The Drive System ---
namespace Drive {
    int speed = 0;
    
    void stop() {
        speed = 0;
        std::cout << "[Drive] Motors Stopped.\n";
    }
}

// --- Family 2: The Camera System ---
namespace Camera {
    int shutter_speed = 100; // Same name part 'speed', but different variable
    
    void stop() {
        std::cout << "[Camera] Recording Stopped.\n";
    }
}

int main() {
    // 1. Setting Variables
    Drive::speed = 50;
    
    // 2. Calling Functions
    // We have two 'stop' functions, but no conflict!
    Drive::stop();   // Stops the wheels
    Camera::stop();  // Stops the video

    return 0;
}

```

---

## 5. ROS2 Context: "The Message Hierarchy"

In ROS2, you never just see `Twist` or `Image`. You see long names like:
`geometry_msgs::msg::Twist`

This tells you the exact family tree:

1. **`geometry_msgs`**: The Package (Grandparent).
2. **`msg`**: The Folder (Parent).
3. **`Twist`**: The Message Type (Child).

*This structure ensures that if you create a message named `Twist` in your own project, it won't break the standard ROS2 one.*

---

## 6. Task: "The Twin Sensors" ✅

**Scenario:**
You are merging code from two different teams.

* **Team A (Lidar Team)** uses a variable `int range = 100;`.
* **Team B (Sonar Team)** uses a variable `int range = 5;`.

**Requirements:**

1. Create a namespace `Lidar` containing `int range = 100;` and a function `print()` that prints "Lidar Range: [value]".
2. Create a namespace `Sonar` containing `int range = 5;` and a function `print()` that prints "Sonar Range: [value]".

**In Main:**

1. Call `Lidar::print()`.
2. Call `Sonar::print()`.

**Observation:**
Prove that you can have two variables with the exact same name (`range`) existing in the same file without errors.
