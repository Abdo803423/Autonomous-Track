
# Git & GitHub: The Survival Guide (Part 1)

Welcome to the team! To ensure we work efficiently and avoid losing code, we use **Git** and **GitHub**. This guide will take you from "What is this?" to pushing your first code.

## 1. The Philosophy: Why do we need this?

Imagine working on a project and saving files like this:
- `code_final.cpp`
- `code_final_v2.cpp`
- `code_final_REALLY_final.cpp`

This is messy and dangerous. **Git** solves this.

### What is Git?
Git is a **Version Control System**. Think of it as a "Time Machine" for your code. It records changes to a file or set of files over time so that you can recall specific versions later.
* **It runs locally** on your machine.
* **It tracks history:** Who changed what, and when.

### Git vs. GitHub
It is crucial to understand the difference:
* **Git:** The tool installed on your laptop (The Camera that takes snapshots).
* **GitHub:** The website where we upload our code (The Photo Album / Cloud Storage).

---

## 2. First Time Setup

Before writing code, you must introduce yourself to Git. This ensures that every contribution you make is tagged with your name.

1.  **Download Git:** [Download Link](https://git-scm.com/downloads)
2.  **Open your Terminal (CMD / PowerShell / Git Bash).**
3.  **Run these commands** (Replace with your actual name and email):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

```

> **Note:** Use the same email you used to sign up for GitHub.

---

## 3. The Workflow: How to Save & Upload

When working with Git, your file goes through **3 Stages** before it reaches GitHub. Understanding this cycle is the key to success.

### The 3 Stages:

1. **Working Directory:** Where you are currently editing files (VS Code, etc.).
2. **Staging Area:** A "waiting room" where you pick which files are ready to be saved.
3. **Repository (.git):** The permanent database where "snapshots" (Commits) are stored.

### The "Golden Commands" Cycle

Whenever you finish a task (e.g., solved a problem, added a feature), follow this exact sequence:

#### Step 1: `git add` (Move to Staging)

Tell Git specifically which files you want to include in the next snapshot.

```bash
# To add a specific file
git add filename.cpp

# OR to add ALL changed files (Recommended for beginners)
git add .

```

#### Step 2: `git commit` (Take the Snapshot)

This saves the file permanently in your local history. **Always write a clear message.**

```bash
git commit -m "Added solution for task 1"

```

* *Bad message:* `git commit -m "update"`
* *Good message:* `git commit -m "Fixed logic error in sensor reading function"`

#### Step 3: `git push` (Upload to GitHub)

Send your committed changes to the cloud so the team can see them.

```bash
git push origin main

```

*(Note: `main` is the default branch name. It might be different depending on our repo structure).*

---

## Summary Cheat Sheet

| Command | Description |
| --- | --- |
| `git status` | Checks which files are changed or staged. (Use this often!) |
| `git add .` | Moves changes to the Staging Area. |
| `git commit -m "msg"` | Saves the snapshot locally. |
| `git push` | Uploads changes to GitHub. |
| `git log` | Shows the history of previous commits. |

---

*End of Part 1. Next: Branching and Team Workflow.*
