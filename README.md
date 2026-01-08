# ASCII Art to Python Translator 🎨➡️🐍

This project transforms ASCII art into Python code logic.  
Each line of ASCII art is translated into structured loops and conditions, ensuring that every character (`@`, `%`, `#`, `+`, `=`, `-`, `.` etc.) is reproduced exactly in code.

---

## ✨ Features
- Converts ASCII art into Python loops and conditionals.
- Maintains exact column alignment (`act_cols` check).
- Supports complex ASCII patterns with symbols, spacing, and repetition.
- Fun blend of **art + programming abstraction**.

---

## 📂 Project Structure
- Each ASCII line is represented as a Python `if r == N:` block.
- Characters are appended one by one with counters (`cols`) to ensure alignment.
- Validation step: `if(cols == act_cols): line += " -> okay"`

---

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/NandKasar10/ascii-to-python.git