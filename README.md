# 🔢 BSM Numerical Analysis Toolkit

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13.6-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Course](https://img.shields.io/badge/Course-Numerical_Analysis-orange.svg)

*A comprehensive computational mathematics toolkit for solving linear systems, finding roots, and numerical integration*

</div>

---

## 📋 Overview

This project implements fundamental numerical analysis algorithms with an interactive terminal-based interface. Built for educational purposes, it provides robust implementations of classical numerical methods taught in computational mathematics courses.

## ✨ Features

### 🔷 Linear System Solvers
- **Gaussian Elimination** - Forward elimination with back substitution
- **Gauss-Jordan** - Row reduction to reduced row echelon form
- **GEMPS** (Gaussian Elimination with Maximum Partial Pivoting and Scaling)
- **MOSS** (Method of Successive Substitutions)

### 🎯 Root Finding Methods
- **Half-Interval Method** (Bisection Method)
- **Newton's Method** (Newton-Raphson)
- **Method of Successive Substitution** (Fixed-Point Iteration)

### 📊 Numerical Integration
- **Trapezoidal Rule** - Composite trapezoidal approximation
- **Romberg's Method** - Richardson extrapolation for high accuracy

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+ 
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Charles787205/BSMProject.git
   cd BSMProject
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   .\Scripts\activate
   
   # Linux/Mac
   source Scripts/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
cd project_files
python main.py
```

The application will launch in fullscreen mode with an interactive menu system.

---

## 🎮 Usage

Navigate through the terminal interface using:
- **Arrow keys** or number keys to select methods
- **Enter** to confirm selection
- Follow on-screen prompts for input

---

## 📦 Dependencies

- `pyautogui` - GUI automation and fullscreen control
- `windows-curses` - Terminal UI library (Windows)
- `prettytable` / `tabulate` - Formatted output tables
- `Pillow` - Image processing support
- Additional utilities for enhanced terminal experience

See [requirements.txt](requirements.txt) for complete list.

---

## 🎓 Educational Context

Developed as part of a **Numerical Analysis** course, this project demonstrates:
- Implementation of classical numerical algorithms
- Computational complexity considerations
- Error analysis and numerical stability
- Interactive educational software design

---

## 👥 Authors

**BSM Project Team**
- Repository: [Charles787205/BSMProject](https://github.com/Charles787205/BSMProject)

---

## 📝 License

This project is available for educational purposes.

---

<div align="center">

**Built with 💻 for Numerical Analysis**

*Learning mathematics through code*

</div>
