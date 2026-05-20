import java.util.List;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;
import moldes.Attack;
import moldes.Character;

public class Main {
    
    // Now main only holds the reference to the character object
    Character player; 
    boolean validAnswer = false;
    Scanner scanner = new Scanner(System.in); 

    public static void main(String[] args) {
        Main game = new Main();
        game.startGame();
    }

    public void startGame(){
        System.out.println("Welcome to the game! Let's create your character.");
        createCharacter();
    }

    public int rollDice(int diceSides){
        return ThreadLocalRandom.current().nextInt(1, diceSides + 1);
    }

    public void createCharacter(){
        int classType;

        System.out.println("Enter the name of your character:");
        String insertedName = scanner.nextLine();

        validAnswer = false; 
        while (!validAnswer) {
            System.out.println("Choose your class: 1 - Warrior, 2 - Wizard, 3 - Ranger, 4 - Rogue");
            
            if (scanner.hasNextInt()) {
                classType = scanner.nextInt();
                scanner.nextLine(); 
            } else {
                System.out.println("Please enter a valid number.");
                scanner.nextLine(); 
                continue;
            }

            switch (classType){
                case 1:
                    player = new Character(insertedName, "Warrior", 150, 0, 0);
                    player.inventory.addAll(List.of("sword", "health potion"));
                    player.attacks.add(new Attack("sword", 8, false, false));
                    player.attacks.add(new Attack("punch", 4, false, false));
                    validAnswer = true;
                    break;
                case 2:
                    player = new Character(insertedName, "Wizard", 100, 0, 100);
                    player.inventory.add("staff");
                    player.attacks.add(new Attack("fire ball", 12, true, false));
                    validAnswer = true;
                    break;
                case 3:
                    player = new Character(insertedName, "Ranger", 130, 8, 0);
                    player.inventory.add("bow");
                    player.attacks.add(new Attack("arrow", 6, false, true));
                    validAnswer = true;
                    break;
                case 4:
                    player = new Character(insertedName, "Rogue", 110, 12, 0);
                    player.inventory.add("dagger");
                    player.attacks.add(new Attack("dagger", 4, false, false));
                    validAnswer = true;
                    break;
                default:
                    System.out.println("Invalid class type. Please type 1, 2, 3, or 4.");
                    break;
            }
        }

        // To access the character's information, we use the dot: player.attribute
        System.out.println("\nCharacter created successfully!");
        System.out.println(player); // Runs the toString() we created in the Character class
        System.out.println("Inventory: " + player.inventory);
        System.out.println("Character attacks: " + player.attacks);

        startAdventure(); 
    }

    public void startAdventure(){
        int friendship = 7;
        System.out.println("\nYou are in a tavern, in a vast world called Manta.");
        System.out.println("The bartender approaches you and says:"); 
        
        validAnswer = false; 
        while (!validAnswer) {         
            System.out.println("\n'I've never seen you around here in Stix, welcome. Would you like something?'");
            System.out.println("1 - Thanks! I'll have a vodka!");
            System.out.println("2 - Ignore");
            System.out.println("3 - Go f*** yourself!");
            
            String response = scanner.nextLine();

            switch (response) {
                case "1":
                    friendship++;
                    System.out.println("He brings you a vodka.");
                    validAnswer = true;
                    break;
                case "2":
                    friendship -= 1;
                    System.out.println("You ignore him. He shrugs and goes to serve another table.");
                    validAnswer = true;
                    break;
                case "3":
                    friendship -= 3;
                    System.out.println("The bartender frowns and mutters something.");
                    validAnswer = true;
                    break;
                default:
                    System.out.println("Invalid option. Choose 1, 2, or 3.");
                    break;
            }
        }
    }
}