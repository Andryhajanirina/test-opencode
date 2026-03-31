"""Plant class module."""


class Plant:
    """Represents a plant with name, height, and watering needs.

    Attributes:
        name: The name of the plant species.
        height: Current height of the plant in cm.
        water_need: How often the plant needs water (days).
        is_alive: Whether the plant is still alive.
    """

    def __init__(
        self,
        name: str,
        height: float = 0.0,
        water_need: int = 7,
    ) -> None:
        """Initialize a Plant instance.

        Args:
            name: The name of the plant species.
            height: Initial height in cm (default 0.0).
            water_need: Watering frequency in days (default 7).

        Raises:
            ValueError: If name is empty, height is negative, or water_need is not positive.
        """
        if not name or not name.strip():
            raise ValueError("Plant name cannot be empty")
        if height < 0:
            raise ValueError("Height cannot be negative")
        if water_need <= 0:
            raise ValueError("Water need must be positive")

        self.name: str = name.strip()
        self.height: float = height
        self.water_need: int = water_need
        self.is_alive: bool = True
        self._days_since_watered: int = 0

    def grow(self, amount: float = 1.0) -> None:
        """Increase the plant height.

        Args:
            amount: Growth amount in cm (default 1.0).

        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Growth amount cannot be negative")
        if not self.is_alive:
            return
        self.height += amount

    def water(self) -> None:
        """Water the plant, resetting the days since last watering."""
        self._days_since_watered = 0

    def pass_day(self) -> None:
        """Simulate a day passing. Plant may die if not watered enough."""
        self._days_since_watered += 1
        if self._days_since_watered > self.water_need * 2:
            self.is_alive = False

    def needs_water(self) -> bool:
        """Check if the plant needs watering.

        Returns:
            True if the plant should be watered, False otherwise.
        """
        return self._days_since_watered >= self.water_need

    def __str__(self) -> str:
        """Return a string representation of the plant.

        Returns:
            Formatted string with plant details.
        """
        status = "alive" if self.is_alive else "dead"
        return f"Plant(name={self.name}, height={self.height:.1f}cm, status={status})"

    def __repr__(self) -> str:
        """Return a detailed string representation.

        Returns:
            Formatted string with all attributes.
        """
        return (
            f"Plant(name={self.name!r}, height={self.height}, "
            f"water_need={self.water_need}, is_alive={self.is_alive})"
        )
