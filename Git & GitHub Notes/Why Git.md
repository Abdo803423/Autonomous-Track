# Git & GitHub Course Summary

## 📌 Introduction
This document serves as a high-level summary of our Git & GitHub course. It covers the core mental models required before we start using commands.

### Why learn this?
* **Industry Standard:** Proficiency in Git is expected by almost every engineering employer.
* **Workflow Hygiene:** It prevents the chaos of managing multiple file versions manually.

---

## 1. The Problem: "The Save-As Loop"
Without Version Control, managing a project usually looks like this:
> `Design_Final_v1.doc`
> `Design_Final_v2.doc`
> `Design_Final_REAL_v3.doc`

**The Issue:** This creates file clutter and makes it impossible to know *what* specifically changed between versions.

## 2. The Solution: Snapshots
Git solves this by taking **Snapshots**.
* Instead of saving multiple copies of a file, Git records the changes made to a single file over time.
* **The Lab Notebook:** Every snapshot includes a "Commit Message" explaining *what* changed and *why*, creating a clear history log of the project.

## 3. Key Concepts for the Team
| Concept | Explanation |
| :--- | :--- |
| **Time Travel** | If we break the code, we can "rewind" the project to a specific snapshot where everything was working. |
| **Collaboration** | Multiple members can work on the same file at the same time without overwriting each other. |
| **Branching** | We can create safe "playgrounds" to test experimental features without breaking the main code. |

---

### ✅ Next Step
**Git is our safety net.** It allows us to experiment and collaborate without fear of losing work.
