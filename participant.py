import random
import re

class PC:
    def __init__(self, name, hp, defense, weapon_pool):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.weapon_pool = weapon_pool # e.g., "2d6" or "1d10"
        self.total_damage_dealt = 0
        self.current_battle_damage = 0

    def roll_damage(self):
        """Rolls damage based on the weapon_pool (e.g., '2d6')."""
        match = re.match(r"(\d+)d(\d+)", self.weapon_pool)
        if not match:
            return 0
        
        num_dice = int(match.group(1))
        die_size = int(match.group(2))
        
        rolls = [random.randint(1, die_size) for _ in range(num_dice)]
        return sum(rolls)

    def take_damage(self, amount):
        """Reduces HP by damage exceeding defense."""
        actual_damage = max(0, amount - self.defense)
        self.hp -= actual_damage
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def reset(self):
        self.hp = self.max_hp
        self.current_battle_damage = 0

class NPC:
    def __init__(self, name, hp, defense, weapon_pool):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.weapon_pool = weapon_pool # e.g., "1d6"
        self.total_damage_dealt = 0
        self.current_battle_damage = 0

    def roll_damage(self):
        match = re.match(r"(\d+)d(\d+)", self.weapon_pool)
        if not match: return 0
        num_dice, die_size = map(int, match.groups())
        return sum(random.randint(1, die_size) for _ in range(num_dice))

    def take_damage(self, amount):
        actual_damage = max(0, amount - self.defense)
        self.hp -= actual_damage
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def reset(self):
        self.hp = self.max_hp
        self.current_battle_damage = 0
