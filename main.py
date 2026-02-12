import argparse
import json
import os
from participant import PC, NPC
from battle import simulate_battle
from stats import StatsTracker

def load_participants(data, cls):
    return [cls(**item) for item in data]

def main():
    parser = argparse.ArgumentParser(description="Battle Simulator")
    parser.add_argument("--config", type=str, default="config.json", help="Path to config file")
    parser.add_argument("--iterations", type=int, help="Number of battles to simulate (overrides config)")
    
    args = parser.parse_args()

    # Load config
    if not os.path.exists(args.config):
        print(f"Error: Config file {args.config} not found.")
        return

    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Resolve parameters
    iterations = args.iterations or config.get("iterations", 100)
    pc_data = config.get("pcs", [])
    npc_data = config.get("npcs", [])

    if not pc_data or not npc_data:
        print("Error: Config must contain 'pcs' and 'npcs' definitions.")
        return

    print(f"Starting simulation: {iterations} iterations")

    # Initialize stats
    tracker = StatsTracker()

    for i in range(iterations):
        # We need fresh objects for each battle
        pcs = load_participants(pc_data, PC)
        npcs = load_participants(npc_data, NPC)
        
        result = simulate_battle(pcs, npcs)
        tracker.track_battle(result)

    # Output stats
    print("\n" + tracker.report())

if __name__ == "__main__":
    main()
