class Attack:
    def __init__(self, mana_cost: int, quantity_of_attacks: int, attack_name: str, attack_dice: int, is_magic: bool = False, long_range: bool = False):
        self.attack_name = attack_name
        self.attack_dice = attack_dice
        self.mana_cost = mana_cost
        self.quantity_of_attacks = quantity_of_attacks
        self.is_magic = is_magic
        self.long_range = long_range

    def __str__(self):
        return f"{self.attack_name} (D{self.attack_dice})"