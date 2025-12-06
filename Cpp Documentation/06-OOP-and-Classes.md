
### **Concept 6: OOP - Classes & OOP**

#### **1. Deep Explanation (The Logic)**

Up until now, we have used simple variables (`int`, `double`) scattered around the code. But in robotics, we deal with complex physical objects like Motors, Sensors, and Batteries.

**The Concept:**
A **Class** (or **Struct**) is a **Custom Data Type**. It is a "Blueprint" or "Template" that groups two things together:

1.  **Attributes (Data):** Variables that describe the object (e.g., `voltage`, `speed`, `name`).
2.  **Methods (Behaviors):** Functions that the object can perform (e.g., `turnOn()`, `readData()`).

**Struct vs. Class (In C++):**
Technically, they are almost identical, but we use them for different purposes:

  * **Struct:** Used for **Passive Data**. Think of it as a "Bag of Variables" with no complex logic. (Example: A GPS Coordinate point `x, y, z`).
  * **Class:** Used for **Active Objects**. It has "Private" internal logic and "Public" commands. (Example: A `MotorController` that handles safety limits internally).

-----

#### **2. Why do we use it?**

1.  **Organization (Scalability):**
      * Without OOP: If you have 4 motors, you need variables like `motor1_speed`, `motor2_speed`, `motor1_pin`, `motor2_pin`... (Messy).
      * With OOP: You create **one** blueprint called `Motor`. You then create 4 **Objects** from that blueprint.
2.  **Encapsulation (Safety):**
      * A Class allows you to make variables **Private**.
      * *Example:* You can prevent the main code from setting `motor.speed = 10000`. Instead, you force the user to call `motor.setSpeed(10000)`, where the class internally checks if that speed is safe before applying it.

-----

#### **3. Syntax & Rules**

**A. The Struct (Data Holder)**

```cpp
struct Point3D {
    double x; // Public by default
    double y;
    double z;
};
```

**B. The Class (The Logic Machine)**

```cpp
class Motor {
private:
    // "Private" means ONLY functions inside this class can touch this variable.
    // main() cannot access this directly.
    int speed; 

public:
    // "Public" means anyone can call these functions.
    void setSpeed(int s) {
        if (s < 100) speed = s; // Logic/Safety check
    }
};
```

-----

#### **4. The Trap: "The Uninitialized Object"**

When you create a Class or Struct, the variables inside it are **not** automatically set to zero (unless you use a Constructor).

  * **The Bug:** You create `Point3D p;`. You forget to set `p.x`.
  * **The Result:** `p.x` will contain random garbage memory (e.g., `-9.255e+61`), causing your robot to teleport in the map.
  * **The Fix:** Always initialize values or use a Constructor.

-----

#### **5. Code Example**

```cpp
#include <iostream>
#include <string>

// --- 1. Struct: Simple Data Grouping ---
// We use struct because this is just data. No complex logic needed.
struct BatteryStatus {
    double voltage;
    double current;
    double percentage;
};

// --- 2. Class: Object with Logic ---
class RoboticArm {
private:
    // Private: The user cannot mess with these directly.
    std::string name;
    bool is_active;

public:
    // Constructor: Runs automatically when you create the object
    RoboticArm(std::string id) {
        name = id;
        is_active = false; // Safe default
    }

    // Method to modify state safely
    void activate() {
        std::cout << "[" << name << "] Activating Hydraulics...\n";
        is_active = true;
    }

    // Method to read state safely
    bool getStatus() {
        return is_active;
    }
};

int main() {
    // A. Using the Struct
    BatteryStatus bat;
    bat.voltage = 12.5; // Direct access allowed (Public)
    
    // B. Using the Class
    RoboticArm arm1("Arm_Left");
    RoboticArm arm2("Arm_Right");

    // arm1.is_active = true; // ERROR! Private variable.
    
    arm1.activate(); // Correct: Using Public method

    std::cout << "Battery: " << bat.voltage << "V\n";
    std::cout << "Arm 1 Active: " << arm1.getStatus() << "\n";
    std::cout << "Arm 2 Active: " << arm2.getStatus() << "\n";

    return 0;
}
```

-----

#### **6. ROS2 Context: "Everything is a Class"**

This is the most important concept for ROS2 structure.

1.  **Nodes are Classes:** When you write a ROS2 program, you don't write a `void main()` script. You write a **Class** that inherits from `rclcpp::Node`.
      * *Logic:* "My robot code is an object. When I spin it up, the Constructor sets up the sensors."
2.  **Messages are Structs:** Every time you define a `.msg` file in ROS2, the system generates a C++ **Struct** for you to use.
      * *Logic:* `geometry_msgs::msg::Twist` is just a struct containing `Vector3 linear` and `Vector3 angular`.

-----

#### **7. Task: The "Smart Thermostat"**

**Scenario:**
You are building a thermostat for a robot's CPU. You want to ensure the target temperature is never set to a dangerous level.

**Requirements:**

1.  Create a `class` named `Thermostat`.
2.  **Private Data:**
      * `double target_temp`
3.  **Public Methods:**
      * `void setTemperature(double temp)`:
          * **Logic:** If `temp` is greater than `100.0`, print "WARNING: Too Hot\!" and set `target_temp` to `100.0` (Safety limit).
          * Else, set `target_temp` to the input value.
      * `double getTemperature()`: Returns the current value.
4.  **In Main:**
      * Create an object `cpu_monitor`.
      * Try to set temperature to `150.0`.
      * Print the actual temperature using `getTemperature()`.
5.  **Success:** The output should show the warning, and the final temperature should be clamped at `100.0`. This proves your Class protected the robot from bad input.
