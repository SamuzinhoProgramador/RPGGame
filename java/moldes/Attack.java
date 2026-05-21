

package moldes;
public class Attack {
    String attackName;
    int attackDice;
    boolean isMagic = false;
    boolean longRange = false;

    public Attack(String nomeDoAtaque, int danoDoAtaque, boolean magia, boolean longoAlcance){
        this.attackName = nomeDoAtaque;
        this.isMagic = magia;
        this.longRange = longoAlcance;
        this.attackDice = danoDoAtaque;
    }

    @Override
    public String toString() {
        return attackName + " (D" + attackDice + ")";
    }
}