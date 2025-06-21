import random


class Chest:
    """
    Represents a treasure chest with a color rarity and gold value.

    Attributes:
        weights (dict): Probability weights for each chest color.
        gold (dict): Base gold values for each chest color.
    """
    weights = {
        'green': 75,
        'orange': 20,
        'purple': 4,
        'golden': 1
    }

    gold = {
        'green': 1000,
        'orange': 4000,
        'purple': 9000,
        'golden': 16000
    }

    def __init__(self):
        """
        Initialize a Chest instance with a randomly selected color 
        based on weights
        and set its base gold value accordingly.
        """
        colors = list(self.weights.keys())
        weights = list(self.weights.values())
        self.color = random.choices(colors, weights)[0]
        self.base_gold = self.gold[self.color]

    def find_approx_value(self):
        """
        Calculate an approximate gold value for the chest 
        within ±10% of the base gold.

        Returns:
            int: Random gold amount near the base gold value.
        """
        lowest_value = int(self.base_gold * 0.9)
        highest_value = int(self.base_gold * 1.1)
        return random.randint(lowest_value, highest_value)
