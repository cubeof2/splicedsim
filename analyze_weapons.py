import random
import statistics

def calculate_damage(die, size_max, defense, crushing):
    """
    Calculates damage for a single die roll based on combat rules.
    """
    # A die hits if it rolls its max value OR meets/exceeds defense
    if die == size_max or die >= defense:
        if crushing and die >= defense:
            # Crushing bonus only applies if it meets/exceeds defense
            return die // defense
        else:
            # Normal hit or auto-hit from max value
            return 1
    return 0

def simulate_attacks(quantity, size_max, defense, crushing, iterations=10000):
    """
    Simulates a number of attacks and returns the average damage.
    """
    total_damage = 0
    for _ in range(iterations):
        for _ in range(quantity):
            die = random.randint(1, size_max)
            total_damage += calculate_damage(die, size_max, defense, crushing)
    return total_damage / iterations

def main():
    sizes = [4, 6, 8, 10, 12]
    quantities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    defenses = [3, 4, 5, 6, 7, 8, 9, 10]
    
    for crushing in [False, True]:
        print(f"\n{'='*60}")
        print(f"DI DAMAGE MATRIX (Crushing: {crushing})")
        print(f"{'='*60}")
        
        for defense in defenses:
            print(f"\nTarget Defense: {defense}")
            header = "Qty | " + " | ".join([f"d{s:<2}" for s in sizes])
            print("-" * len(header))
            print(header)
            print("-" * len(header))
            
            for qty in quantities:
                results = []
                for size in sizes:
                    avg_dmg = simulate_attacks(qty, size, defense, crushing)
                    results.append(f"{avg_dmg:.2f}")
                print(f"{qty:<3} | " + " | ".join([f"{r:<3}" for r in results]))

if __name__ == "__main__":
    main()
