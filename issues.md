# Static Analysis Issue Documentation

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| B324 - Weak MD5 hash | Security - High | 47 | MD5 is a weak hashing algorithm and should not be used where security is expected. | Replace MD5 with SHA-256. |
| B605 - Shell command execution | Security - High | 58 | `os.system()` starts a shell command and may allow command injection when user-controlled input is included. | Remove the shell command and use normal Python output instead. |
| B307 - Unsafe eval | Security - Medium | 42 | `eval()` executes arbitrary Python expressions and can execute malicious input. | Replace expression evaluation with a safe numerical discount calculation. |
| B110 - Bare exception with pass | Security / Reliability - Low | 26-27 | The program catches every exception and silently ignores it, hiding unexpected errors. | Avoid the exception by safely removing the order with `pop()`. |
| B311 - Insecure random generator | Security - Low | 51 | The `random` module is not suitable for security-sensitive values such as a POS PIN. | Use Python's `secrets` module. |
| W0102 - Mutable default argument | Code Quality | 15 | `order_log=[]` is created once and shared between function calls, which may cause unexpected data to persist. | Use `None` as the default and create a new list inside the function. |
| C0103 - Invalid function naming | Code Quality | 15, 23, 30, 40 | Several function names use camelCase instead of Python's recommended snake_case naming convention. | Rename the functions to snake_case and update their calls. |
| W0702 / E722 - Bare except | Code Quality / Style | 26 | The `except:` statement catches all exceptions without identifying the expected error. | Replace the exception-based approach with safe dictionary removal. |
| F401 - Unused import | Style | 6 | The `math` module is imported but never used. | Remove the unused import. |
| F841 - Unused variable | Style | 31 | `service_tax` is assigned but never used in the calculation. | Remove the unused variable. |
| E711 - Incorrect None comparison | Style | 32 | The code compares a value with `None` using `==` rather than `is None`. | Replace `== None` with `is None`. |
| E501 - Long lines | Style | 18, 19, 75 | Several lines exceed the recommended Flake8 line length. | Split long statements across multiple lines. |
