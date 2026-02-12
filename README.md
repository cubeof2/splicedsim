# SplicedSim

A battle simulator for the Spliced TTRPG. This tool allows game designers to simulate combat encounters between Players (PCs) and Non-Player Characters (NPCs) to test balance, mechanics, and strategies.

## Features

- **Multi-Round Combat**: Simulates full battles with randomized initiative.
- **Weapon Mechanics**: Supports dice pools (e.g., `2d6`), auto-hits on max rolls, and the `crushing` tag.
- **Strategies**: Basic AI behaviors like `random_attack`, `attack_weak`, and `attack_strong`.
- **Statistical Analysis**: Aggregates win rates, average rounds, and damage distribution across multiple iterations.
- **Weapon Analyzer**: A standalone tool to compare the mathematical performance of different weapon configurations.

## Usage

### 1. Battle Simulator

The main simulator reads configurations from JSON files and outputs statistical results.

```bash
python main.py [OPTIONS]
```

**Options:**
- `--config PATH`: Path to a config JSON file (defaults to `config.json` or `default_config.json`).
- `--iterations N`: Number of battles to simulate (overrides config value).
- `--verbose`, `-v`: Output detailed, round-by-round logs for the **first** battle in the simulation.

#### Sample Simulator Output

```text
Starting simulation: 5 iterations using config.json

--- Round 1 ---
  Goblin 1 attacks Rogue: Rolls [5] vs Def 2 -> 1 dmg (HP: 19)
  Orc attacks Rogue (Crushing): Rolls [2] vs Def 2 -> 1 dmg (HP: 18)
  ...
Battle Over! Winner: PCs

=== SIMULATION RESULTS ===
Total Battles: 5
PC Wins: 4 (80.0%)
NPC Wins: 1 (20.0%)
Avg Rounds per Battle: 21.8

Total Damage Distribution:
  - Fighter        :      186 total (avg   37.2 per battle)
  - Orc            :      159 total (avg   31.8 per battle)
  - Rogue          :       37 total (avg    7.4 per battle)
```

### 2. Weapon Analyzer

A dedicated script for comparing damage output across a matrix of weapon sizes, quantities, and target defenses.

```bash
python analyze_weapons.py
```

#### Sample Analyzer Output

```text
============================================================
DI DAMAGE MATRIX (Crushing: False)
============================================================

Target Defense: 4
---------------------------------
Qty | d4  | d6  | d8  | d10 | d12
---------------------------------
1   | 0.25 | 0.51 | 0.62 | 0.70 | 0.74
2   | 0.49 | 1.01 | 1.25 | 1.40 | 1.50
3   | 0.75 | 1.49 | 1.88 | 2.10 | 2.27
```

## Configuration

Participants and battle settings are defined in JSON. Example structure:

```json
{
  "iterations": 100,
  "pcs": [
    { "name": "Fighter", "hp": 30, "defense": 4, "weapon_pool": "1d10", "tags": ["crushing"] }
  ],
  "npcs": [
    { "name": "Goblin", "hp": 10, "defense": 2, "weapon_pool": "1d6" }
  ]
}
```
