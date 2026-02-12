import random
import re

class Weapon:
    """Represents a weapon with a dice pool for damage and optional tags."""
    def __init__(self, *, dice_pool, tags=None):
        """
        Initialize a Weapon.
        
        Args:
            dice_pool (str): The dice pool (e.g., '3d8', '1d10').
            tags (list, optional): List of weapon tags (e.g., ['crushing']).
        """
        self.dice_pool = dice_pool
        self.tags = tags or []
        self.quantity_max = 0
        self.size_max = 0
        self._parse_pool()

    def _parse_pool(self):
        """Parses the dice pool string into quantity and size."""
        match = re.match(r"(\d+)d(\d+)", self.dice_pool)
        if match:
            self.quantity_max = int(match.group(1))
            self.size_max = int(match.group(2))

    def has_tag(self, tag):
        """Checks if the weapon has a specific tag."""
        return tag in self.tags

    def roll_dice(self):
        """
        Rolls each die in the dice pool individually.
        
        Returns:
            list: A list of individual die results.
        """
        if self.quantity_max <= 0 or self.size_max <= 0:
            return []
        return [random.randint(1, self.size_max) for _ in range(self.quantity_max)]
