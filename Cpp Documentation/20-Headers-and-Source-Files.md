
# Concept 20: Header Files vs Source Files (.hpp & .cpp)

## 1. Deep Explanation (The Logic)
So far, we have written everything in one file (`main.cpp`).
In a real robot, the code is massive (thousands of lines). If you put it all in one file, it becomes unreadable and slow to compile.

We split code into two types of files:



### A. The Header File (`.hpp` or `.h`): The Menu 
* **Content:** Declarations.
* **Function:** It says **what** functions exist, but **not how** they work.
* **Analogy:** A **Restaurant Menu**. It lists "Burger", but it doesn't contain the recipe for making the burger.

### B. The Source File (`.cpp`): The Kitchen 
* **Content:** Definitions (Implementation).
* **Function:** It contains the actual code logic.
* **Analogy:** The **Chef's Recipe Book**. This is where the burger is actually cooked.

---

## 2. Why do we use it?
1.  **Compilation Speed:** If you change the logic in the `.cpp` file (the Kitchen), you don't need to update everyone who just looks at the `.hpp` file (the Menu). This makes building large ROS2 projects much faster.
2.  **Organization:** You give your teammate the Header File so they know **how to use** your code, without distracting them with the complex math inside the Source File.

---

## 3. Syntax & Rules

### Step 1: The Header (`Robot.hpp`)
Use `#pragma once` to prevent the file from being loaded twice (a common error).

```cpp
#pragma once // Safety Guard

class Robot {
public:
    void move(int speed); // Just the name. No code.
    int getBattery();     // Just the name.
};

```

### Step 2: The Source (`Robot.cpp`)

You must include the header so the compiler knows what you are building.

```cpp
#include "Robot.hpp"
#include <iostream>

// Syntax: ClassName::FunctionName
// We use Robot:: to tell C++ "This code belongs to the header declaration"
void Robot::move(int speed) {
    std::cout << "Moving at " << speed << " m/s\n";
}

int Robot::getBattery() {
    return 100;
}

```

### Step 3: The Main (`main.cpp`)

You include the header to use the class.

```cpp
#include "Robot.hpp"

int main() {
    Robot r;
    r.move(50);
    return 0;
}

```

---

## 4. The Trap: "The Linker Error" ⚠️

* **The Bug:** You declared `void move();` in the Header, but you forgot to write the code for it in the `.cpp` file.
* **The Result:** The code compiles (because the syntax is right), but the **Linker** fails later because it can't find the "Recipe" for the function.
* **The Error Message:** `undefined reference to 'Robot::move'`

---

## 5. ROS2 Context: "The Standard Package Structure"

Every ROS2 package follows this structure strictly. If you don't understand Concept 20, you won't know where to write your code.

```text
my_robot_pkg/
├── CMakeLists.txt         (Tells the compiler how to combine files)
├── package.xml
├── include/
│   └── my_robot_pkg/
│       └── my_node.hpp    (The Class Declaration)
└── src/
    ├── my_node.cpp        (The Logic)
    └── main.cpp           (Starts the Node)

```

---

## 6. Task: "The File Splitter" ✅

**Scenario:**
You have a Calculator class. You need to split it into 3 files.

**Requirements:**

**1. Create `Calculator.hpp`:**

* Declare `class Calculator`.
* Declare method `int add(int a, int b);`.

**2. Create `Calculator.cpp`:**

* Include `"Calculator.hpp"`.
* Write the code for `add` (`return a + b`).

**3. Create `main.cpp`:**

* Include `"Calculator.hpp"`.
* Create an object and print the result of `add(5, 5)`.

*Goal: Understand that code is distributed across files, not just dumped in one place.*
