package moldes;
import java.util.ArrayList;

public class Character {
    // Atributos específicos do personagem
    String name;
    String characterClass;
    int healthPoints;
    int level;
    int stealth;
    int mana;
    public ArrayList<Attack> attacks;
    public ArrayList<String> inventory;

    public Character(String name, String characterClass, int healthPoints, int stealth, int mana) {
        this.name = name;
        this.characterClass = characterClass;
        this.healthPoints = healthPoints;
        this.level = 1; 
        this.stealth = stealth;
        this.mana = mana;
        this.attacks = new ArrayList<>();
        this.inventory = new ArrayList<>();
    }

    // Método para facilitar a impressão dos dados do personagem na tela
    @Override
    public String toString() {
        return "Nome: " + name + " | Classe: " + characterClass + " | HP: " + healthPoints + " | Mana: " + mana + " | Stealth: " + stealth;
    }
}