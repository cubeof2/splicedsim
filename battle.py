import random

def simulate_battle(*, pcs, npcs):
    """
    Simulates a single battle until one side is defeated.
    
    Args:
        pcs (list): List of PC objects.
        npcs (list): List of NPC objects.
        
    Returns:
        dict: A dictionary containing the winner, number of rounds, and damage statistics.
    """
    # Reset participants
    for p in pcs + npcs:
        p.reset()

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
            actual_damage = target.take_damage(amount=raw_damage)
            
            attacker.total_damage_dealt += actual_damage
            attacker.current_battle_damage += actual_damage

    winner = "PCs" if any(p.is_alive() for p in pcs) else "NPCs"
    
    return {
        "winner": winner,
        "rounds": round_count,
        "damage_stats": {p.name: p.current_battle_damage for p in pcs + npcs}
    }
