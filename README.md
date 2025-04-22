# Let's create the README.md file based on the detailed explanation.

readme_content = """\
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
