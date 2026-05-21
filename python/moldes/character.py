from typing import List
from moldes.attack import Attack

class Character:
    def __init__(self, name: str, character_class: str, health_points: int, stealth: int, mana: int):
        self.name = name
        self.character_class = character_class
        self.health_points = health_points
        self.level = 1 
        self.stealth = stealth
        self.mana = mana
        self.attacks: List[Attack] = []
        self.inventory: List[str] = []

    # O método __str__ substitui o toString() do Java
    def __str__(self):
        return f"Nome: {self.name} | Classe: {self.character_class} | HP: {self.health_points} | Mana: {self.mana} | Stealth: {self.stealth}"