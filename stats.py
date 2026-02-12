from collections import defaultdict

class StatsTracker:
    def __init__(self):
        self.pc_wins = 0
        self.npc_wins = 0
        self.total_battles = 0
        self.damage_distribution = defaultdict(float)
        self.battle_durations = []

    def track_battle(self, result):
        self.total_battles += 1
        if result["winner"] == "PCs":
            self.pc_wins += 1
        else:
            self.npc_wins += 1
        
        for name, damage in result["damage_stats"].items():
            self.damage_distribution[name] += damage
            
        self.battle_durations.append(result["rounds"])

    def report(self):
        if self.total_battles == 0:
            return "No battles simulated."

        pc_win_rate = (self.pc_wins / self.total_battles) * 100
        npc_win_rate = (self.npc_wins / self.total_battles) * 100
        avg_rounds = sum(self.battle_durations) / self.total_battles

        out = []
        out.append("=== SIMULATION RESULTS ===")
        out.append(f"Total Battles: {self.total_battles}")
        out.append(f"PC Wins: {self.pc_wins} ({pc_win_rate:.1f}%)")
        out.append(f"NPC Wins: {self.npc_wins} ({npc_win_rate:.1f}%)")
        out.append(f"Avg Rounds per Battle: {avg_rounds:.1f}")
        out.append("\nTotal Damage Distribution:")
        
        # Sort by damage descending
        sorted_damage = sorted(self.damage_distribution.items(), key=lambda x: x[1], reverse=True)
        for name, damage in sorted_damage:
            avg_damage = damage / self.total_battles
            out.append(f"  - {name:15}: {damage:8.0f} total (avg {avg_damage:6.1f} per battle)")
        
        return "\n".join(out)
