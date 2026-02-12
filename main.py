import argparse
import json
import os
from participant import PC, NPC
from battle import simulate_battle
from stats import StatsTracker

def load_participants(*, data, cls):
    """
    Creates participant objects from configuration data.
    
    Args:
        data (list): List of dictionaries containing participant attributes.
        cls (class): The class to instantiate (PC or NPC).
        
    Returns:
        list: A list of instantiated objects.
    """
    return [cls(**item) for item in data]

def main():
    """
    Main entry point for the battle simulator.
    Parses CLI arguments, loads config, and runs the simulation loop.
    """
    parser = argparse.ArgumentParser(description="Battle Simulator")
    parser.add_argument("--config", type=str, help="Path to config file (defaults to config.json or default_config.json)")
    parser.add_argument("--iterations", type=int, help="Number of battles to simulate (overrides config)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Output detailed logs for the first battle")
    
    args = parser.parse_args()

    # Load config
    config_path = args.config
    if not config_path:
        if os.path.exists("config.json"):
            config_path = "config.json"
        else:
            config_path = "default_config.json"

    if not os.path.exists(config_path):
        print(f"Error: Config file {config_path} not found.")
        return

    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Resolve parameters
    iterations = args.iterations or config.get("iterations", 100)
    pc_data = config.get("pcs", [])
    npc_data = config.get("npcs", [])
    pc_strategy = config.get("pc_strategy", "random_attack")
    npc_strategy = config.get("npc_strategy", "random_attack")

    if not pc_data or not npc_data:
        print("Error: Config must contain 'pcs' and 'npcs' definitions.")
        return

    print(f"Starting simulation: {iterations} iterations using {config_path}")

    # Initialize stats
    tracker = StatsTracker()

    for i in range(iterations):
        # We need fresh objects for each battle
        pcs = load_participants(data=pc_data, cls=PC)
        npcs = load_participants(data=npc_data, cls=NPC)
        
        # Only be verbose for the first battle if flag is set
        is_verbose = args.verbose and (i == 0)
        
        result = simulate_battle(
            pcs=pcs, 
            npcs=npcs, 
            pc_strategy=pc_strategy, 
            npc_strategy=npc_strategy,
            verbose=is_verbose
        )
        tracker.track_battle(result=result)

    # Output stats
    print("\n" + tracker.report())

if __name__ == "__main__":
    main()
