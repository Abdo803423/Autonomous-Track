

### **Concept 5: Functions & Memory References (Deep Dive)**

#### **1. Deep Explanation (The Logic & Memory)**

A function is a machine: Input $\rightarrow$ Work $\rightarrow$ Output.
But **how** does the input enter the machine? This is where C++ gives you two completely different options.

**Option A: Pass by Value (The "Clone")**

  * **Definition:** You give the function a **Photocopy** of your variable.
  * **Memory Action:** The computer allocates **NEW** memory. It copies the data from your variable into this new space.
  * **Relationship:** The function's variable and your variable are totally separate. If the function changes the copy, your original is untouched.
  * **Cost:** High. If you pass a 10MB image, the computer pauses to copy 10MB of data.

**Option B: Pass by Reference (The "Link")**

  * **Definition:** You give the function the **Address** of your variable (using `&`).
  * **Memory Action:** No new memory is allocated for data. The function creates a "Link" or "Alias" pointing to your **EXISTING** memory.
  * **Relationship:** They are the same object. If the function changes the data, your original variable changes immediately.
  * **Cost:** Zero. Passing a link takes nanoseconds, even for huge data.

-----

#### **2. Why do we use it? (The Engineering View)**

1.  **Performance (The Main Reason):**

      * In ROS2, we send huge data (Camera Frames: \~3MB, Lidar Clouds: \~5MB).
      * **By Value:** Copying 5MB x 30 times/second = **System Freeze**.
      * **By Reference:** Passing the address x 30 times/second = **Instant**.

2.  **Multiple Outputs:**

      * A function can only `return` one value.
      * But what if you need to calculate both `Speed` and `Direction`?
      * **Solution:** You pass both variables by **Reference**. The function updates them directly, effectively "returning" two results.

-----

#### **3. Syntax & The `const` Trick**

**A. Pass by Value (Clone)**

```cpp
// "int x" creates a NEW box.
void calculate(int x) { ... }
```

**B. Pass by Reference (Link)**

```cpp
// "int &x" creates a LINK to the existing box.
void update(int &x) { ... }
```

**C. Const Reference (The Best of Both Worlds)**

  * *This is standard ROS2 practice.*
  * You want the **speed** of a Reference (no copying), but the **safety** of a Value (read-only).
  * We use `const`.

<!-- end list -->

```cpp
// "Read this huge data instantly, but DO NOT change it."
void analyze_image(const int &image_data) { ... }
```

-----

#### **4. The Proof: Checking Memory Addresses**

To understand this deeply, look at the **Memory Address**. Every variable lives at a specific ID (like `0x7ff...`).

  * **In Pass by Value:** The Main variable and Function variable have **DIFFERENT** addresses.
  * **In Pass by Reference:** The Main variable and Function variable have the **SAME** address.

-----

#### **5. Code Example (The Proof)**

```cpp
#include <iostream>

// Option A: Pass by Value
// 'val' is a CLONE.
void processByValue(int val) {
    std::cout << "   [Func] Address of val: " << &val << " (Different)\n";
    val = 500; // Changes the clone only
}

// Option B: Pass by Reference
// 'ref' is an ALIAS (Another name for the original).
void processByReference(int &ref) {
    std::cout << "   [Func] Address of ref: " << &ref << " (SAME!)\n";
    ref = 500; // Changes the original
}

int main() {
    int my_number = 10;
    
    std::cout << "1. MAIN Start: " << my_number << "\n";
    std::cout << "   [Main] Address of my_number: " << &my_number << "\n\n";

    // --- Test Value ---
    std::cout << "--- Calling PassByValue ---\n";
    processByValue(my_number);
    std::cout << "   [Main] After Call: " << my_number << " (Unchanged)\n\n";

    // --- Test Reference ---
    std::cout << "--- Calling PassByReference ---\n";
    processByReference(my_number);
    std::cout << "   [Main] After Call: " << my_number << " (CHANGED!)\n";

    return 0;
}
```

-----

#### **6. ROS2 Context: "The Subscriber Callback"**

In ROS2, efficient memory management is critical.
When a robot receives a message (e.g., `LaserScan`), ROS2 calls your function.

  * **Bad Practice (Value):** `void topic_callback(msg::LaserScan msg)`
      * ROS2 creates a full copy of the scan data. Slow.
  * **Good Practice (Const Reference):** `void topic_callback(const msg::LaserScan &msg)`
      * ROS2 gives you a pointer to the existing message in memory. Instant. You can read it, but you cannot accidentally delete or change the sensor data (safety).

-----

#### **7. Task: The "Stats Keeper"**

**Scenario:**
You are writing a function to analyze a list of battery voltages. You need to find the **Minimum** and **Maximum** voltage in the list.
Since you need to return *two* results, you cannot use a normal `return`. You must use **Pass by Reference**.

**Given Data:**

  * `std::vector<double> volts = {12.5, 11.8, 13.1, 12.0};`
  * Variables `min_v` and `max_v` initialized to `0.0` in `main()`.

**Requirements:**

1.  Create a function `void find_extremes(...)`.
2.  **The Logic Puzzle (Parameters):**
      * The Input (the list) should be passed by **Const Reference** (Speed + Safety). `(const std::vector<double> &list)`
      * The Outputs (`min` and `max`) should be passed by **Reference** (So we can modify them). `(double &min_out, double &max_out)`
3.  **Inside the function:**
      * Loop through the list.
      * Update `min_out` and `max_out` with the correct values.
4.  **In Main:**
      * Call the function.
      * Print `min_v` and `max_v`.
      * **Success:** If `min_v` becomes `11.8` and `max_v` becomes `13.1`, you successfully used references to return multiple values.
