
# Concept 19: Namespaces (Modules & Packages)

## 1. Deep Explanation (The Logic)
Imagine a school with two students named "Ahmed".
* If the teacher calls out *"Ahmed!"*, both students look up. Confusion happens. 😕
* To fix this, we use their **Family Names**: "Ahmed **Ali**" vs. "Ahmed **Mohamed**".

**Namespaces** are the "Family Names" for your code.

### The Problem:
You write a function `connect()` for your Wi-Fi. You download a library for Bluetooth that *also* has a function named `connect()`. Python panics (or simply overwrites one with the other) because it doesn't know which one you want.

### The Solution:
In Python, **every File (`.py`) acts as its own namespace** (called a **Module**). You can also use **Classes** to group related names together inside a single file.



* **The Symbol (`.`):** This is the **Dot Operator**. It translates to *"Belongs to"*.
* `wifi.connect()` means *"The connect function that **belongs to** wifi"*.

---

## 2. Why do we use it?
1.  **Collision Prevention:** In a robot, you might have Motor control for the wheels and Motor control for a robotic arm. Separating them (`wheels.motor` vs `arm.motor`) prevents bugs.
2.  **Organization:** ROS2 is massive. It organizes code into logical groups:
    * `math.` $\rightarrow$ Standard Math Tools.
    * `rclpy.` $\rightarrow$ ROS Client Library Tools.
    * `sensor_msgs.` $\rightarrow$ Sensor Data Tools.

---

## 3. Syntax & Rules

### A. Creating a Namespace
In Python, you usually create a new file (e.g., `drive.py`). Everything inside that file belongs to the `drive` namespace.

However, for simple grouping **inside one file**, we can simulate a namespace using a **Class**.

```python
class RobotArm:
    speed = 50
    
    @staticmethod # Allows us to call this without creating an object
    def move():
        print("Arm moving")

```

### B. Accessing the Code

You must use the `.` operator.

```python
RobotArm.move()
s = RobotArm.speed

```

### C. The Import Shortcuts

If you get tired of typing `RobotArm.`, you can import specific parts.

* **Safe:** `from RobotArm import move` (You can call `move()` directly).
* **Unsafe:** `from RobotArm import *` (This dumps **everything** into your main code. If you have a `speed` variable, it will be overwritten! **Avoid this**).

---

## 4. Code Example

```python
# --- Family 1: The Drive System ---
# We use a Class to group these variables together, simulating a Namespace
class Drive:
    speed = 0
    
    @staticmethod
    def stop():
        Drive.speed = 0
        print("[Drive] Motors Stopped.")

# --- Family 2: The Camera System ---
class Camera:
    shutter_speed = 100 # Same name part 'speed', but different variable
    
    @staticmethod
    def stop():
        print("[Camera] Recording Stopped.")

# --- Main Execution ---
def main():
    # 1. Setting Variables
    # We access them using the "Dot Notation"
    Drive.speed = 50
    
    # 2. Calling Functions
    # We have two 'stop' functions, but no conflict!
    Drive.stop()   # Stops the wheels
    Camera.stop()  # Stops the video

if __name__ == "__main__":
    main()

```

---

## 5. ROS2 Context: "The Import Chain"

In ROS2 Python, you never just see `Twist`. You see long import chains like:

`from geometry_msgs.msg import Twist`

This tells you the exact family tree:

1. **`geometry_msgs`**: The Package (Grandparent Folder).
2. **`msg`**: The Module (Parent Folder).
3. **`Twist`**: The Class (Child).

*This structure ensures that if you create a message named `Twist` in your own project, it won't break the standard ROS2 one.*

---

## 6. Task: "The Twin Sensors" ✅

**Scenario:**
You are merging code from two different teams in one file.

* **Team A (Lidar Team)** uses a variable `range = 100`.
* **Team B (Sonar Team)** uses a variable `range = 5`.

**Requirements:**

1. Create a class `Lidar` containing `range = 100` and a static function `print_data()` that prints "Lidar Range: [value]".
2. Create a class `Sonar` containing `range = 5` and a static function `print_data()` that prints "Sonar Range: [value]".

**In Main:**

1. Call `Lidar.print_data()`.
2. Call `Sonar.print_data()`.

**Observation:**
Prove that you can have two variables with the exact same name (`range`) existing in the same file without errors.
