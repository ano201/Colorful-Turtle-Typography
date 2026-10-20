# 🐢 Colorful Turtle Typography

A custom Python project built using Turtle graphics to dynamically render text strings with individual character functions, automated loops, and vibrant color cycling.

## 📸 Preview
![Colorful Turtle Typography Output](Screenshot.png)

## ✨ Supported Characters (Current)
The engine currently supports a robust set of uppercase characters and spacing, with more letters coming soon:
- **`a`**, **`b`**, **`d`**, **`e`**, **`f`**, **`h`**, **`i`**, **`l`**, **`n`**, **`p`**, **`r`**, **`t`**, **`v`**, **`x`**, **`z`**
- **`space`** (for word spacing)
- **`line_break`** (for multi-line rendering)

## 🚀 Features
- **Modular Architecture:** Cleanly separated character drawing logic into an external `characters.py` module for improved maintainability.
- **Dynamic Character Rendering:** Automatically loops through input strings and invokes matching functions dynamically using Python's `globals()`.
- **Automated Color Cycling:** Loops through a diverse list of vibrant colors using modulo arithmetic (`idx % len(colors)`).
- **Custom Primitives:** Built from scratch using foundational movement functions like vertical lines (`vl`), horizontal lines (`hl`), and half-circle curves (`hcr`).
- **Heading Control:** Standardized turtle heading control to prevent positional drift during rendering.

## 🛠️ How to Run
1. Ensure you have Python installed.
2. Keep `main.py` and `characters.py` in the same directory.
3. Run the main script:
   ```bash
   python main.py
