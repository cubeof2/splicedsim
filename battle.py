import random

def _select_target(*, potential_targets, strategy):
    """
    Selects a target from living opponents based on the team strategy.
    
    Args:
        potential_targets (list): List of living opponent objects.
        strategy (str): The strategy to use ('random_attack', 'attack_weak', 'attack_strong').
        
    Returns:
        object: The selected target.
    """
    if not potential_targets:
        return None
        
    if strategy == "attack_weak":
        min_hp = min(t.hp for t in potential_targets)
        candidates = [t for t in potential_targets if t.hp == min_hp]
        return random.choice(candidates)
        
    if strategy == "attack_strong":
        max_hp = max(t.hp for t in potential_targets)
        candidates = [t for t in potential_targets if t.hp == max_hp]
        return random.choice(candidates)
        
    # Default to random_attack
    return random.choice(potential_targets)

def simulate_battle(*, pcs, npcs, pc_strategy="random_attack", npc_strategy="random_attack", verbose=False):
    """
    Simulates a single battle until one side is defeated.
    
    Each round, all living participants get one turn in a randomized order.
    
    Args:
        pcs (list): List of PC objects.
        npcs (list): List of NPC objects.
        pc_strategy (str): Strategy for the PC team.
        npc_strategy (str): Strategy for the NPC team.
        verbose (bool): If True, output detailed round-by-round logs.
        
    Returns:
        dict: A dictionary containing the winner, number of rounds, and damage statistics.
    """
    # Reset participants
    for p in pcs + npcs:
        p.reset()

    round_count = 0
    while any(p.is_alive() for p in pcs) and any(p.is_alive() for p in npcs):
        round_count += 1
        if verbose:
            print(f"\n--- Round {round_count} ---")
        
        # Determine initiative for this round
        participants = [p for p in pcs + npcs if p.is_alive()]
        random.shuffle(participants)
        
        # Track who has gone in the round already
        for attacker in participants:
            if not attacker.is_alive():
                continue
                
            # If the battle ended mid-round, stop
            if not (any(p.is_alive() for p in pcs) and any(p.is_alive() for p in npcs)):
                break

            # Define opponents and strategy
            if attacker in pcs:
                opponents = [n for n in npcs if n.is_alive()]
                strategy = pc_strategy
            else:
                opponents = [p for p in pcs if p.is_alive()]
                strategy = npc_strategy
            
            target = _select_target(potential_targets=opponents, strategy=strategy)
            
            if target:
                rolls = attacker.roll_dice()
                total_damage = 0
                
                for die in rolls:
                    if die >= target.defense:
                        if attacker.weapon.has_tag("crushing"):
                            total_damage += die // target.defense
                        else:
                            total_damage += 1
                
                actual_damage = target.take_damage(amount=total_damage)
                
                attacker.total_damage_dealt += actual_damage
                attacker.current_battle_damage += actual_damage
                
                if verbose:
                    crushing_str = " (Crushing)" if attacker.weapon.has_tag("crushing") else ""
                    rolls_str = ", ".join(map(str, rolls))
                    print(f"  {attacker.name} attacks {target.name}{crushing_str}: Rolls [{rolls_str}] vs Def {target.defense} -> {actual_damage} dmg (HP: {target.hp})")

    winner = "PCs" if any(p.is_alive() for p in pcs) else "NPCs"
    if verbose:
        print(f"\nBattle Over! Winner: {winner}")
    
    return {
        "winner": winner,
        "rounds": round_count,
        "damage_stats": {p.name: p.current_battle_damage for p in pcs + npcs}
    }
