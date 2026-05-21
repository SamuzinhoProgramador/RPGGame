class Attack:
    def __init__(self, attack_name: str, attack_dice: int, is_magic: bool = False, long_range: bool = False):
        self.attack_name = attack_name
        self.attack_dice = attack_dice
        self.is_magic = is_magic
        self.long_range = long_range

    # O método __str__ substitui o toString() do Java
    def __str__(self):
        return f"{self.attack_name} (D{self.attack_dice})"