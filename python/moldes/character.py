from typing import List
from moldes.attack import Attack

class Character:
    def __init__(self, name: str, character_class: str, hp: int, stealth: int, mana: int):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.max_hp = hp
        self.xp_to_level_up = 100
        self.level = 1 
        self.xp = 0
        self.stealth = stealth
        self.mana = mana
        self.attacks: List[Attack] = []
        self.inventory: List[str] = []

    # O método __str__ substitui o toString() do Java
    def __str__(self):
        return f"Nome: {self.name} | Classe: {self.character_class} | HP: {self.max_hp} | Mana: {self.mana} | Stealth: {self.stealth}"
    
    def gain_xp(self, xp_gain: int):
        self.xp += xp_gain

        if(self.xp >= self.xp_to_level_up):
            levelUp()
        
    

def levelUp(self):
    self.level +=1
    self.xp_to_next_level += (self.xp_to_next_level / 2)
    self.xp = 0
    increaseHealth = self.max_hp / 2
    self.max_hp += increaseHealth
    self.hp += increaseHealth
    if self.character_class == "Warrior":
        if self.level == 2:
            
            for attack in self.player.attacks:
                attack.quantity_of_attacks +=1
            print("Congratulations! You leveled up and gain extra attack!")

        elif self.level == 3:
            print("Tomorow I'll continue")