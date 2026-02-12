import random
import re
from weapon import Weapon

class PC:
    """Represents a Player Character in the simulation."""
    def __init__(self, *, name, hp, defense, weapon_pool, tags=None):
        """
        Initialize a PC.
        
        Args:
            name (str): The name of the character.
            hp (int): The hit points of the character.
            defense (int): The defense value to subtract from incoming damage.
            weapon_pool (str): The dice pool for damage (e.g., '2d6').
            tags (list, optional): List of weapon tags.
        """
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.weapon = Weapon(dice_pool=weapon_pool, tags=tags)
        self.total_damage_dealt = 0
        self.current_battle_damage = 0

    def roll_dice(self):
        """
        Rolls each die in the weapon's pool individually.
        
        Returns:
            list: List of individual die results.
        """
        return self.weapon.roll_dice()

    def take_damage(self, *, amount):
        """
        Reduces HP by the damage amount. Defense is handled externally in the success mechanic.
        
        Args:
            amount (int): The damage to take.
            
        Returns:
            int: The damage taken.
        """
        self.hp -= amount
        return amount

    def is_alive(self):
        """Checks if the character is still alive."""
        return self.hp > 0

    def reset(self):
        """Resets HP and current battle damage for a new simulation."""
        self.hp = self.max_hp
        self.current_battle_damage = 0

class NPC:
    """Represents a Non-Player Character in the simulation."""
    def __init__(self, *, name, hp, defense, weapon_pool, tags=None):
        """
        Initialize an NPC.
        
        Args:
            name (str): The name of the NPC.
            hp (int): The hit points of the NPC.
            defense (int): The defense value to subtract from incoming damage.
            weapon_pool (str): The dice pool for damage (e.g., '1d6').
            tags (list, optional): List of weapon tags.
        """
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.weapon = Weapon(dice_pool=weapon_pool, tags=tags)
        self.total_damage_dealt = 0
        self.current_battle_damage = 0

    def roll_dice(self):
        """
        Rolls each die in the NPC's weapon individually.
        
        Returns:
            list: List of individual die results.
        """
        return self.weapon.roll_dice()

    def take_damage(self, *, amount):
        """
        Reduces HP by the damage amount.
        
        Args:
            amount (int): The damage to take.
            
        Returns:
            int: The damage taken.
        """
        self.hp -= amount
        return amount

    def is_alive(self):
        """Checks if the NPC is still alive."""
        return self.hp > 0

    def reset(self):
        """Resets HP and current battle damage."""
        self.hp = self.max_hp
        self.current_battle_damage = 0
