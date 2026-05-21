import random
from moldes.character import Character
from moldes.attack import Attack

class Main:
    def __init__(self):
        self.player = None
        self.valid_answer = False

    def start_game(self):
        print("Welcome to the game! Let's create your character.")
        self.create_character()

    def roll_dice(self, dice_sides: int) -> int:
        # Substitui o ThreadLocalRandom do Java
        return random.randint(1, dice_sides)

    def create_character(self):
        inserted_name = input("Enter the name of your character:\n")

        self.valid_answer = False 
        while not self.valid_answer:
            print("Choose your class: 1 - Warrior, 2 - Wizard, 3 - Ranger, 4 - Rogue")
            class_type_input = input()
            
            # Validação para garantir que o usuário digitou um número
            if not class_type_input.isdigit():
                print("Please enter a valid number.")
                continue
            
            class_type = int(class_type_input)

            # Substituindo o switch/case por if/elif/else (padrão do Python)
            if class_type == 1:
                self.player = Character(inserted_name, "Warrior", 150, 0, 0)
                self.player.inventory.extend(["sword", "health potion"])
                self.player.attacks.append(Attack("sword", 8, False, False))
                self.player.attacks.append(Attack("punch", 4, False, False))
                self.valid_answer = True
            elif class_type == 2:
                self.player = Character(inserted_name, "Wizard", 100, 0, 100)
                self.player.inventory.append("staff")
                self.player.attacks.append(Attack("fire ball", 12, True, False))
                self.valid_answer = True
            elif class_type == 3:
                self.player = Character(inserted_name, "Ranger", 130, 8, 0)
                self.player.inventory.append("bow")
                self.player.attacks.append(Attack("arrow", 6, False, True))
                self.valid_answer = True
            elif class_type == 4:
                self.player = Character(inserted_name, "Rogue", 110, 12, 0)
                self.player.inventory.append("dagger")
                self.player.attacks.append(Attack("dagger", 4, False, False))
                self.valid_answer = True
            else:
                print("Invalid class type. Please type 1, 2, 3, or 4.")

        print("\nCharacter created successfully!")
        print(self.player) 
        print(f"Inventory: {self.player.inventory}")
        
        # Formatando a lista de ataques para usar o __str__ de cada ataque
        attacks_str = ", ".join([str(attack) for attack in self.player.attacks])
        print(f"Character attacks: [{attacks_str}]")

        self.start_adventure() 

    def start_adventure(self):
        friendship = 7
        print("\nYou are in a tavern, in a vast world called Manta.")
        print("The bartender approaches you and says:") 
        
        self.valid_answer = False 
        while not self.valid_answer:         
            print("\n'I've never seen you around here in Stix, welcome. Would you like something?'")
            print("1 - Thanks! I'll have a vodka!")
            print("2 - Ignore")
            print("3 - Go f*** yourself!")
            
            response = input()

            if response == "1":
                friendship += 1
                print("He brings you a vodka.")
                self.valid_answer = True
            elif response == "2":
                friendship -= 1
                print("You ignore him. He shrugs and goes to serve another table.")
                self.valid_answer = True
            elif response == "3":
                friendship -= 3
                print("The bartender frowns and mutters something.")
                self.valid_answer = True
            else:
                print("Invalid option. Choose 1, 2, or 3.")

# Ponto de entrada clássico do Python para rodar o sistema
if __name__ == "__main__":
    game = Main()
    game.start_game()