import random
import re

class PC:
    """Represents a Player Character in the simulation."""
    def __init__(self, *, name, hp, defense, weapon_pool):
        """
        Initialize a PC.
        
        Args:
            name (str): The name of the character.
            hp (int): The hit points of the character.
            defense (int): The defense value to subtract from incoming damage.
            weapon_pool (str): The dice pool for damage (e.g., '2d6').
        """
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.weapon_pool = weapon_pool 
        self.total_damage_dealt = 0
        self.current_battle_damage = 0

    def roll_damage(self):
        """
        Rolls damage based on the weapon_pool (e.g., '2d6').
        
        Returns:
            int: The total damage rolled.
        """
        match = re.match(r"(\d+)d(\d+)", self.weapon_pool)
        if not match:
            return 0
        
        num_dice = int(match.group(1))
        die_size = int(match.group(2))
        
        rolls = [random.randint(1, die_size) for _ in range(num_dice)]
        return sum(rolls)

    def take_damage(self, *, amount):
        """
        Reduces HP by damage exceeding defense.
        
        Args:
            amount (int): The raw damage incoming.
            
        Returns:
            int: The actual damage taken.
        """
        actual_damage = max(0, amount - self.defense)
        self.hp -= actual_damage
        return actual_damage

    def is_alive(self):
        """Checks if the character is still alive."""
        return self.hp > 0

    def reset(self):
        """Resets HP and current battle damage for a new simulation."""
        self.hp = self.max_hp
        self.current_battle_damage = 0

class NPC:
    """Represents a Non-Player Character in the simulation."""
    def __init__(self, *, name, hp, defense, weapon_pool):
        """
        Initialize an NPC.
        
        Args:
            name (str): The name of the NPC.
            hp (int): The hit points of the NPC.
            defense (int): The defense value to subtract from incoming damage.
            weapon_pool (str): The dice pool for damage (e.g., '1d6').
        """
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.weapon_pool = weapon_pool 
        self.total_damage_dealt = 0
        self.current_battle_damage = 0

    def roll_damage(self):
        """
        Rolls damage based on the weapon_pool.
        
        Returns:
            int: The total damage rolled.
        """
        match = re.match(r"(\d+)d(\d+)", self.weapon_pool)
        if not match: return 0
        num_dice, die_size = map(int, match.groups())
        return sum(random.randint(1, die_size) for _ in range(num_dice))

    def take_damage(self, *, amount):
        """
        Reduces HP by damage exceeding defense.
        
        Args:
            amount (int): The raw damage incoming.
            
        Returns:
            int: The actual damage taken.
        """
        actual_damage = max(0, amount - self.defense)
        self.hp -= actual_damage
        return actual_damage

    def is_alive(self):
        """Checks if the NPC is still alive."""
        return self.hp > 0

    def reset(self):
        """Resets HP and current battle damage."""
        self.hp = self.max_hp
        self.current_battle_damage = 0
