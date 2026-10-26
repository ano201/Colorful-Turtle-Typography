# 🐢 Colorful Turtle Typography

A custom Python project built using Turtle graphics to dynamically render text strings with individual character functions, automated loops, and vibrant color cycling.

## 📸 Preview
![Colorful Turtle Typography Output](Screenshot.png)

## ✨ Supported Characters (Current)
The engine currently supports a robust set of uppercase characters and spacing, with more letters coming soon:
- **`a`**, **`b`**, **`d`**, **`e`**, **`f`**, **`h`**, **`i`**, **`l`**, **`m`**, **`n`**, **`p`**, **`r`**, **`t`**, **`u`**, **`v`**, **`w`**, **`x`**, **`z`**
- **`space`** (for word spacing)

## 🚀 Features
- **Modular Architecture:** Cleanly separated character drawing logic into an external `patterns.py` module for improved maintainability.
- **Dynamic Character Rendering:** Automatically loops through input strings and invokes matching functions dynamically using Python's `globals()`.
- **Auto Line-Wrapping:** Automatically detects screen margins (`_x > 230`) and seamlessly shifts text to the next line (`_y -= 60`) when it reaches the right boundary.
- **Automated Color Cycling:** Loops through a diverse list of vibrant colors using modulo arithmetic (`idx % len(colors)`).
- **Custom Primitives:** Built from scratch using foundational movement functions like vertical lines (`vl`), horizontal lines (`hl`), and half-circle curves (`hcr`).
- **Heading Control:** Standardized turtle heading control to prevent positional drift during rendering.

## 🛠️ How to Run
1. Ensure you have Python installed.
2. Keep `main.py` and `patterns.py` in the same directory.
3. Run the main script:
   ```bash
   python main.py
