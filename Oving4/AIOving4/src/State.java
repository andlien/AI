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
	
	public int[][] getCloneEggCarton() {
		int[][] cloneEggCarton = new int[eggCarton.length][eggCarton[0].length];
		for (int i = 0; i < eggCarton.length; i++) {
			for (int j = 0; j < eggCarton[0].length; j++) {
				cloneEggCarton[i][j] = eggCarton[i][j];
			}
		}
		return cloneEggCarton;
	}
	
	public float getCost(){
		//TODO
		return 100;
	}
	
	@Override
	public boolean equals(Object i) {
		return eggCarton == ((State) i).getEggCarton();
	}
	
	public void printState() {
		for (int i = 0; i < eggCarton.length; i++) {
			String line = "";
			for (int j = 0; j < eggCarton[i].length; j++) {
				line += eggCarton[i][j] + " ";
			}
			System.out.println(line);
		}
	}
	
}
