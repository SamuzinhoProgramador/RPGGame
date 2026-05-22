from random import randint as rd #samuzinho esteve aqui
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
        return rd(1, dice_sides)

    def create_character(self):
        inserted_name = input("Enter the name of your character:\n")

        while True:
            try:
                class_type = int(input("Choose your class: 1 - Warrior, 2 - Wizard, 3 - Ranger, 4 - Rogue"))

            except ValueError:
                print("Please enter a number.\n")
                input()                 

            else:

                if class_type < 1 or class_type > 4:
                    print("The value must be 1, 2, 3 or 4\n")
                    input()
                    continue #se não for válido, reinicia o while

                if class_type == 1:
                    self.player = Character(inserted_name, "Warrior", 150, 0, 0)
                    self.player.inventory.extend(["sword", "health potion"])
                    self.player.attacks.append(Attack(0, 1,"sword", 8, False, False))
                    self.player.attacks.append(Attack(0, 1, "punch", 4, False, False))
                elif class_type == 2:
                    self.player = Character(inserted_name, "Wizard", 100, 0, 100)
                    self.player.inventory.append("staff")
                    self.player.attacks.append(Attack(30, 1, "fire ball", 12, True, False))
                elif class_type == 3:
                    self.player = Character(inserted_name, "Ranger", 130, 8, 0)
                    self.player.inventory.append("bow")
                    self.player.attacks.append(Attack(0, 1, "arrow", 6, False, True))
                elif class_type == 4:
                    self.player = Character(inserted_name, "Rogue", 110, 12, 0)
                    self.player.inventory.append("dagger")
                    self.player.attacks.append(Attack(0, 1, "dagger", 4, False, False))

                print("\nCharacter created successfully!")
                input()
                print(self.player) 
                print(f"Inventory: {self.player.inventory}")
                attacks_str = ", ".join([str(attack) for attack in self.player.attacks])
                print(f"Character attacks: [{attacks_str}]")
                input()
                self.start_adventure()
                break

    def start_adventure(self):
        friendship = 7
        print("\nYou are in a tavern, in a vast world called Manta.")
        input()
        print("The bartender approaches you and says:") 
        correctAnswer = False
        
        while correctAnswer == False:
            try:
                print("\n'I've never seen you around here in Stix, welcome. Would you like something?'")
                input()
                print("1 - Thanks! I'll have a vodka!")
                print("2 - Ignore")
                print("3 - Go f*** yourself!")
                
                response = int(input())
            
            except ValueError:
                print("Please enter a number.\n")
                input()

            else:
                if response < 1 or response > 3:
                    print("Please enter a number that correspondes with one of the options")
                    continue #reinicia o while
                else:
                    correctAnswer = True
                    
                if response == "1":
                    friendship += 1
                    print("He brings you a vodka.")
                elif response == "2":
                    friendship -= 1
                    print("You ignore him. He shrugs and goes to serve another table.")
                elif response == "3":
                    friendship -= 3
                    print("The bartender frowns and mutters something.")
                
if __name__ == "__main__":
    game = Main()
    game.start_game()