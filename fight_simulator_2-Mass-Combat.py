import random

# Tier Dice list
tier = (0, 4, 6, 8, 10, 12)

# Character class with attributes
class Character:
    def __init__(self, name, tier, fighting, defensive):
        self.name = name
        self.tier = tier
        self.fighting = fighting
        self.defensive = defensive
        self.hp = tier * 20  # HP based on tier
        self.pool = 1
    
    def attack_roll(self, opponent):
        # Creates a roll pool, and checks if skill is higher then opponents
        roll_pool = self.pool
        
        if self.fighting > opponent.fighting:
            pool += 1
        # rolls all dice
        roll_results = 0
        for dice in range(roll_pool):
            roll_results += random.randint(1, tier[self.tier])

        return roll_results
    
    def defense_roll(self, opponent):
        # Creates a roll pool, and checks if skill is higher then opponents
        roll_pool = self.pool
        
        if self.defensive > opponent.defensive:
            pool += 1
        # rolls all dice
        roll_results = 0
        for dice in range(roll_pool):
            roll_results += random.randint(1, tier[self.tier])

        return roll_results

    
# Function to simulate a battle between two characters
def full_combat_log(character1, character2):
    rounds = 1
    while character1.hp > 0 and character2.hp > 0:
        print(f"Start of Round {rounds}!")

        # Characters roll their attack roll against the opponents defense roll
        damage1 = character1.attack_roll(character2) - character2.defense_roll(character1)
        damage2 = character2.attack_roll(character1) - character1.defense_roll(character2)

        # Characters take the damage from the attack, or zero if negative damage was inflicted
        character1.hp -= max(damage2, 0)
        character2.hp -= max(damage1, 0)

        # Increases the round counter and report the results of the round
        rounds += 1
        print(f"Round {rounds} complete!")
        print(f"{character1.name} took {damage2} damage")
        print(f"{character2.name} took {damage1} damage")

    # Reports the results of the fight
    if character1.hp > 0:
        print(f"{character1.name} wins in {rounds} rounds with {character1.hp} HP left!")
    elif character2.hp > 0:
        print(f"{character2.name} wins in {rounds} rounds with {character2.hp} HP left!")
    else:
        print("Neither one the battle, both were knocked out!")


def quick_combat_log(character1, character2):
    rounds = 1
    while character1.hp > 0 and character2.hp > 0:
        # Characters roll their attack roll against the opponents defense roll
        damage1 = character1.attack_roll(character2) - character2.defense_roll(character1)
        damage2 = character2.attack_roll(character1) - character1.defense_roll(character2)

        # Characters take the damage from the attack, or zero if negative damage was inflicted
        character1.hp -= max(damage2, 0)
        character2.hp -= max(damage1, 0)

        # Increases the round counter
        rounds += 1

    # Reports the results of the fight
    if character1.hp > 0:
        print(f"{character1.name} wins in {rounds} rounds with {character1.hp} HP left!")
    elif character2.hp > 0:
        print(f"{character2.name} wins in {rounds} rounds with {character2.hp} HP left!")
    else:
        print("Neither one the battle, both were knocked out!")

character_a = Character("FighterMan", tier=1, fighting=10, defensive=10)
character_b = Character("FighterWoman", tier=1, fighting=10, defensive=10)

quick_combat_log(character_a, character_b,)
