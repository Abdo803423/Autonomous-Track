
# Git & GitHub: Team Structure & Rules (Part 2)

Now that you know the basics, we need to agree on how we organize our files. A messy repository makes it impossible to review code or track progress.

## 1. Repository Structure (Where to put your code?)

To prevent conflicts and keep things organized, we will follow a strict folder structure. **Do not create files in the root directory** (outside folders) unless it's a documentation file.

### The Structure Tree
We will use a "Member-Based" structure for this phase. Each member has their own dedicated workspace.

```text
├── README.md          # Project documentation
├── Docs/              # General learning resources
└── Team_Workspace/    # 📂 THIS IS WHERE YOU WORK
    ├── Ammar_Yasser/  # Your personal folder
    │   ├── Task_01/
    │   │   ├── solution.cpp
    │   │   └── notes.txt
    │   └── Task_02/
    ├── Ahmed_Ali/
    │   └── Task_01/
    └── [Your_Name]/   # Create a folder with your name here

```

### 📝 Instructions for Members:

1. Navigate to `Team_Workspace`.
2. Create a folder with your name (e.g., `John_Doe`) if it doesn't exist.
3. Inside your folder, create a sub-folder for the current task (e.g., `Task_01_Calculator`).
4. Put all your source code there.

---

## 2. The `.gitignore` File (Keep it Clean)

You might notice a file named `.gitignore` in the repo. This file tells Git **what NOT to upload**.

**Why?**
We only want **Source Code** (e.g., `.cpp`, `.py`, `.java`). We do NOT want:

* Compiled files (`.exe`, `.o`, `.class`).
* IDE settings (`.vscode/`, `.idea/`).
* System files (`.DS_Store`, `Thumbs.db`).

> **Rule:** If you see generated files in your `git status`, do NOT add them. If `.gitignore` is missing something, notify the Team Leader.

---

## 3. The "Golden Rules" of Collaboration

To keep the repository healthy, every team member must follow these commandments:

### 🚫 Rule #1: Never Push Broken Code

Before you `git push`, make sure your code compiles and runs locally. The repository should always contain working code.

### ⚠️ Rule #2: Descriptive Naming

* **Bad:** `file.cpp`, `test.c`, `folder1`
* **Good:** `sensor_reading.cpp`, `led_control.c`, `Task_01_PWM`

### 🔄 Rule #3: Pull Before You Push

Someone might have updated the repo while you were working. Always update your local version before sending your changes (we will explain how to do this in Part 3).

---

*End of Part 2. Next: The Collaborator Workflow (Branching & Pull Requests).*
