import random

# Character class with attributes
class Character:
    def __init__(self, name, tier, fighting, speed, endurance, ki):
        self.name = name
        self.tier = tier
        self.fighting = fighting
        self.ki = ki
        self.speed = speed
        self.endurance = endurance
        self.hp = tier * 20  # HP based on tier
    

# Technique class with customizable attributes
class Technique:
    def __init__(self, name, energy_type, attack_form, speed, damage, area_of_effect, duration, energy_cost, charge_time, special_effects):
        self.name = name
        self.energy_type = energy_type
        self.attack_form = attack_form
        self.speed = speed
        self.damage = damage
        self.area_of_effect = area_of_effect
        self.duration = duration
        self.energy_cost = energy_cost
        self.charge_time = charge_time
        self.special_effects = special_effects

# Function to simulate a battle between two characters
def simulate_battle(character1, character2):
    rounds = 0
    while character1.hp > 0 and character2.hp > 0:
        # Simulate characters taking turns to attack
        attack1 = random.randint(1, character1.fighting)
        attack2 = random.randint(1, character2.fighting)
        print(f"Character 1: {attack1}")
        print(f"Character 2: {attack2}")

        # Calculate damage and update HP
        damage1 = (attack1 - character2.endurance)
        damage2 = (attack2 - character1.endurance)

        print(f"Character 1: {damage1}")
        print(f"Character 2: {damage2}")

        character2.hp -= damage1
        character1.hp -= damage2

        rounds += 1
        print(f"Round {rounds} complete!")
        print(f"{character1.name} is at {character1.hp} HP")
        print(f"{character2.name} is at {character2.hp} HP")

    return rounds

# Create two sample characters
character_a = Character("Character A", tier=1, fighting=10, speed=5, endurance=10, ki=5)
character_b = Character("Character B", tier=1, fighting=10, speed=5, endurance=10, ki=5)

# Create sample techniques for each character (customize as needed)
technique1_a = Technique("Technique 1 (Character A)", energy_type="Ki", attack_form="Projectile", speed=3, damage=2, area_of_effect="Single Target", duration="Instant", energy_cost="Low", charge_time="Instant", special_effects=["Stunning"])
technique2_a = Technique("Technique 2 (Character A)", energy_type="Ki", attack_form="Beam", speed=2, damage=3, area_of_effect="Splash Damage", duration="Instant", energy_cost="Moderate", charge_time="Quick Charge", special_effects=["Blinding"])
technique3_a = Technique("Technique 3 (Character A)", energy_type="Elemental Energy", attack_form="Sphere", speed=1, damage=4, area_of_effect="Area Burst", duration="Continuous", energy_cost="High", charge_time="Extended Charge", special_effects=["Status Effects"])

technique1_b = Technique("Technique 1 (Character B)", energy_type="Ki", attack_form="Projectile", speed=3, damage=2, area_of_effect="Single Target", duration="Instant", energy_cost="Low", charge_time="Instant", special_effects=["Stunning"])
technique2_b = Technique("Technique 2 (Character B)", energy_type="Ki", attack_form="Beam", speed=2, damage=3, area_of_effect="Splash Damage", duration="Instant", energy_cost="Moderate", charge_time="Quick Charge", special_effects=["Blinding"])
technique3_b = Technique("Technique 3 (Character B)", energy_type="Elemental Energy", attack_form="Sphere", speed=1, damage=4, area_of_effect="Area Burst", duration="Continuous", energy_cost="High", charge_time="Extended Charge", special_effects=["Status Effects"])

# Simulate a battle between the characters
rounds = simulate_battle(character_a, character_b)

# Print the battle outcome
if character_a.hp > 0:
    print(f"{character_a.name} wins in {rounds} rounds!")
else:
    print(f"{character_b.name} wins in {rounds} rounds!")
