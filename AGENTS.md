# AGENTS.md - Development Guidelines

This file provides coding guidelines for agents operating in this repository.

## Project Structure

```
./python/    # Python project
./c/         # C project (42-style)
```

---

## Build & Test Commands

### Python Project (`./python`)

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run single test
pytest tests/test_file.py::test_function

# Format code (line length 79)
black --line-length 79 .

# Sort imports
isort .

# Lint code
flake8 .

# Type checking
mypy .

# All checks (lint + type check + tests)
flake8 . && mypy . && pytest
```

### C Project (`./c`)

```bash
# Build project
make

# Rebuild from scratch
make re

# Run tests
make test

# Clean build files
make clean

# Clean all (including binaries)
make fclean

# Re-build and run tests
make re && make test

# Norminette check (42 norm)
norminette -R CheckForbiddenSourceHeader .
```

---

## Code Style - Python (PEP 8)

### Formatting
- Line length: **79 characters**
- Use `black --line-length 79 .` for formatting
- Use `isort .` for import sorting (profile=black)

### Imports
- Order: standard library → third-party → local
- Use `isort` to enforce consistent ordering
- Never use wildcard imports (`from module import *`)

### Naming Conventions
- **Functions/variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Private variables**: prefix with `_single_underscore`

### Type Hints
- Always use explicit type annotations
- Use `mypy` for static type checking
- Avoid `Any` when possible

### Error Handling
- Use specific exception types (never bare `except:`)
- Prefer explicit error messages
- Use context managers for resource management
- Example:
  ```python
  try:
      with open(filepath, 'r') as f:
          data = f.read()
  except FileNotFoundError:
      raise MyCustomError(f"File not found: {filepath}") from None
  ```

### Docstrings
- Use Google or NumPy style
- Example:
  ```python
  def function(param: str) -> int:
      """Short summary.

      Args:
          param: Description of parameter.

      Returns:
          Description of return value.

      Raises:
          ValueError: When param is invalid.
      """
  ```

---

## Code Style - C (42 Norm)

### General Rules
- Follow Norminette strictly: `norminette -R CheckForbiddenSourceHeader .`
- **Function naming**: `snake_case`
- **Variable naming**: snake_case
- No forbidden headers in libft (e.g., no `<stdio.h>`, `<stdlib.h>` for libft functions)
- Use only allowed standard functions

### Function Limits
- Maximum **5 functions** per file
- Maximum **20 lines** per function
- Maximum **5 variables** per function

### Control Structures
- **No for loops** - use `while` loops instead
- Use braces even for single-line blocks

### Error Handling
- Return `-1` on error, `0` on success
- Always free allocated memory on failure
- Check return values of functions

### Makefile Requirements
- Must have: `all`, `clean`, `fclean`, `re`, `test` rules
- Use `$(NAME)` for binary name
- CC = cc, CFLAGS = -Wall -Wextra -Werror

---

## Testing Guidelines

### Python
- Place tests in `tests/` directory
- Test file naming: `test_<module>.py`
- Test function naming: `test_<function_name>_<scenario>`
- Use `pytest` fixtures for setup/teardown
- Run single test: `pytest tests/test_file.py::test_function`

### C
- Place test files in root or `tests/` directory
- Implement simple tester via `make test`
- Test should verify function outputs match expected results

---

## Additional Notes

- Always run lint/type checks before committing
- For Python: `flake8 . && mypy .`
- For C: `norminette -R CheckForbiddenSourceHeader . && make re && make test`
- Never commit secrets, keys, or credentials
- Keep responses concise when operating as an agent
