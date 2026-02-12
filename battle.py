import random

def simulate_battle(pcs, npcs):
    """
    Simulates a single battle until one side is defeated.
    Returns a dictionary with the results.
    """
    # Reset participants
    for p in pcs + npcs:
        p.reset()
        p.current_battle_damage = 0

    battle_log = []
    
    # Simple initiative: random order of all participants
    participants = pcs + npcs
    
    round_count = 0
    while any(p.is_alive() for p in pcs) and any(p.is_alive() for p in npcs):
        round_count += 1
        random.shuffle(participants)
        
        for attacker in participants:
            if not attacker.is_alive():
                continue
                
            # Target selection: PCs attack NPCs, NPCs attack PCs
            if attacker in pcs:
                targets = [n for n in npcs if n.is_alive()]
            else:
                targets = [p for p in pcs if p.is_alive()]
            
            if not targets:
                break
                
            target = random.choice(targets)
            
            raw_damage = attacker.roll_damage()
            actual_damage = target.take_damage(raw_damage)
            
            attacker.total_damage_dealt += actual_damage
            attacker.current_battle_damage += actual_damage
            
            # (Optional) Log the action if needed for debugging
            # battle_log.append(f"{attacker.name} hit {target.name} for {actual_damage} damage ({raw_damage} raw)")

    winner = "PCs" if any(p.is_alive() for p in pcs) else "NPCs"
    
    return {
        "winner": winner,
        "rounds": round_count,
        "damage_stats": {p.name: p.current_battle_damage for p in pcs + npcs}
    }
