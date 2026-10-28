# Reflection

## 1. What did I learn from using Pylint, Bandit, and Flake8?

I learned that each tool checks a different part of code quality. Pylint mainly helped me improve code structure, naming, documentation, and maintainability. Bandit focused on security problems such as unsafe `eval()`, weak hashing, shell execution, and insecure random number generation. Flake8 helped me correct formatting and style problems such as unused imports, long lines, and incorrect comparisons.

## 2. Which issue did I consider the most important and why?

The most important issue was the use of `eval()` for calculating the discounted bill. `eval()` can execute arbitrary Python code, so using untrusted input with it can create a serious security risk. I replaced it with a normal numerical discount calculation, which performs the same required task without executing arbitrary expressions.

## 3. How did static analysis improve the program?

Static analysis helped identify problems that were easy to miss while simply running the program. The original program worked, but it still contained poor coding practices and security weaknesses. After fixing the reported issues, the Pylint score improved from 4.81/10 to 10.00/10, Bandit reported zero security issues, and Flake8 reported no style violations. This made the code cleaner, safer, and easier to maintain.

## 4. Can static analysis tools detect every problem in a program?

No. Static analysis tools are useful, but they cannot detect every logical or security problem. For example, the program originally displayed the POS terminal secret directly in the output. This was a security concern even though it was not reported in my Bandit results. This showed me that developers still need to manually review program behavior and should not depend only on automated tools.
