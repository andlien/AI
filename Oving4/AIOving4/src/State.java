import java.util.ArrayList;


public class State {
	private int[][] eggCarton;
	private ArrayList<State> neighbours;
	
	public State(int[][] carton) {
		this.eggCarton = carton;
	}
	
	public ArrayList<State> getNeighbours() {
		return neighbours;
	}
	
	public int[][] getEggCarton() {
		return eggCarton;
	}
	
	public boolean equals(State i) {
		return eggCarton == i.getEggCarton();
	}
	
}
