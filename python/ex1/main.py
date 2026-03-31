"""Main module demonstrating Plant class usage."""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ex0.ft_class_plant import Plant


def main() -> None:
    """Demonstrate Plant class operations."""
    fern = Plant("Fern", height=10.0, water_need=5)
    cactus = Plant("Cactus", height=5.0, water_need=14)

    print(fern)
    print(cactus)

    fern.grow(2.5)
    cactus.grow(1.0)

    for _ in range(6):
        fern.pass_day()

    print(f"Fern needs water: {fern.needs_water()}")

    fern.water()
    print(f"After watering, fern needs water: {fern.needs_water()}")

    for _ in range(12):
        cactus.pass_day()
    print(f"Cactus alive after 12 days: {cactus.is_alive}")

    for _ in range(20):
        cactus.pass_day()
    print(f"Cactus alive after 32 days total: {cactus.is_alive}")
    cactus.grow(5.0)
    print(f"Cactus height (dead plants don't grow): {cactus.height:.1f}cm")

    print(repr(fern))
    print(repr(cactus))


if __name__ == "__main__":
    main()
