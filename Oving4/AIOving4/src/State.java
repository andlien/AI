import java.util.ArrayList;


public class State {
	private int[][] eggCarton;
	private ArrayList<State> neighbours;
	private int conflictRatio;
	
	public State(int[][] carton, int max) {
		this.eggCarton = carton;
		calculateObjectiveFunction(max);
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
		return conflictRatio;

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
	
	private void calculateObjectiveFunction(int k) {
		int y = eggCarton.length;
		int x = eggCarton[0].length;
		int[] horSum = new int[y];
		int[] vertSum = new int[x];
		int[] downDiagSum = new int[x+y-1];
		int[] upDiagSum = new int[x+y-1];
		
		// Want to only execute moves that reduce the number of "conflicts"
		// Iterates over each number once
		for (int i = 0; i < y; i++) {
			for (int j = 0; j < x; j++) {
				if (eggCarton[y][x] == 1) {
					horSum[i] ++;
					vertSum[j] ++;
					downDiagSum[7-j+i] ++;
					upDiagSum[i+j] ++;
				}
			}
		}
		
		conflictRatio = 0;
		for (int i = 0; i < horSum.length; i++) {
			if (horSum[i] > k) conflictRatio ++;
		}
		for (int i = 0; i < vertSum.length; i++) {
			if (vertSum[i] > k) conflictRatio ++;
		}
		for (int i = 0; i < downDiagSum.length; i++) {
			if (downDiagSum[i] > k) conflictRatio ++;
			if (upDiagSum[i] > k) conflictRatio ++;
		}
		
		conflictRatio /= (y*k);
	}
}
