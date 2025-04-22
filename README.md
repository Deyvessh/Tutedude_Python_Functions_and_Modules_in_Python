# 📘 Factorial & Math Operations - Python Examples

This project contains **three small Python scripts** that demonstrate different ways of calculating **factorials** and performing **basic mathematical operations** like square root, logarithm, and trigonometric functions using the built-in and `math` libraries in Python.

---

## 📌 Contents

1. [Factorial using Iteration](#1-factorial-using-iteration)
2. [Factorial using Recursion](#2-factorial-using-recursion)
3. [Basic Math Functions using `math` Module](#3-basic-math-functions-using-math-module)

---

## 1. 📈 Factorial using Iteration

```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

sample_number = int(input('Enter a number: '))
output = factorial(sample_number)
print(f'Factorial of {sample_number} is: {output}')
```

### 🔍 How it Works

- **`factorial(n)`**: This function calculates the factorial of a number `n` using a **loop** (iteration).
- It starts with a `result` of `1` and **multiplies** it by every number from `2` to `n`.
- **User input** is taken and passed to the `factorial()` function.
- The final result is printed.

### ✅ Example
If you enter `5`, it will calculate:
```
1 * 2 * 3 * 4 * 5 = 120
```

---

## 2. 🔁 Factorial using Recursion

```python
def factoraial(n):
    if n < 2:
        return 1
    else:
        return n * factoraial(n - 1)

sample_number = int(input('Enter a number: '))
output = factoraial(sample_number)
print(f'Factorial of {sample_number} is: {output}')
```

### 🔍 How it Works

- **Recursive approach**: The function calls itself to solve the smaller sub-problem.
- **Base Case**: If `n` is less than `2`, it returns `1`.
- **Recursive Case**: Otherwise, it returns `n * factorial(n - 1)`.

### ✅ Example
For input `5`, the call stack will look like:
```
factoraial(5)
= 5 * factoraial(4)
= 5 * 4 * factoraial(3)
= 5 * 4 * 3 * factoraial(2)
= 5 * 4 * 3 * 2 * factoraial(1)
= 5 * 4 * 3 * 2 * 1 = 120
```

### ⚠️ Note
There's a typo in the function name: `factoraial` instead of `factorial`. It's still valid but could lead to confusion in real-world projects.

---

## 3. 🔬 Basic Math Functions using `math` Module

```python
from math import *

number = int(input('Enter a number: '))

square_root = sqrt(number)
logarithm = log(number)
sine = sin(number)

print(f'Square root: {square_root}')
print(f'Logarithm: {logarithm}')
print(f'Sine: {sine}')
```

### 🔍 How it Works

This script performs three mathematical operations using functions from the Python `math` module:

- **`sqrt(number)`**: Returns the square root of the input.
- **`log(number)`**: Returns the natural logarithm (base `e`) of the number.
- **`sin(number)`**: Returns the sine of the number **in radians**.

### ✅ Example
For input `number = 4`, output will be:
```
Square root: 2.0
Logarithm: 1.3862943611198906
Sine: -0.7568024953079282
```

### 📎 Import Tip
We use `from math import *` to import **all** functions in the `math` module so we can use them directly without `math.` prefix.

---
