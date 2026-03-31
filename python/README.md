# Plant Python

A Python project implementing a `Plant` class with watering simulation and growth mechanics.

## Project Structure

```
python/
├── ex0/
│   └── ft_class_plant.py   # Plant class definition
├── ex1/
│   └── main.py             # Demo script
└── requirements.txt        # Dependencies (empty)
```

## Plant Class

The `Plant` class (`ex0/ft_class_plant.py`) represents a plant with:

- **name** - Species name
- **height** - Current height in cm
- **water_need** - Watering frequency in days
- **is_alive** - Survival status

### Methods

| Method | Description |
|---|---|
| `grow(amount)` | Increase plant height |
| `water()` | Water the plant, reset days counter |
| `pass_day()` | Simulate a day; plant dies if unwatered past `water_need * 2` |
| `needs_water()` | Returns `True` if watering is due |

## Usage

### Run the demo

```bash
cd python/ex1
python main.py
```

### Use the class directly

```python
from ex0.ft_class_plant import Plant

fern = Plant("Fern", height=10.0, water_need=5)
fern.pass_day()
print(fern.needs_water())  # False until 5+ days pass
```

## Validation

The class raises `ValueError` for:
- Empty plant name
- Negative height or growth amount
- Non-positive water need

## Development

```bash
# Install dependencies
pip install -r requirements.txt

# Format code
black --line-length 79 .

# Sort imports
isort .

# Lint
flake8 .

# Type check
mypy .

# Run all checks
flake8 . && mypy . && pytest
```
