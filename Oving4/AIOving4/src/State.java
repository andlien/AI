import java.util.ArrayList;


public class State {
	private int[][] eggCarton;
	private ArrayList<State> neighbours;
	private float conflictRatio;
	
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
		System.out.println(conflictRatio);
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
				if (eggCarton[i][j] == 1) {
					horSum[i] ++;
					vertSum[j] ++;
					downDiagSum[(int) (Math.ceil((y+x)/2)-j+i-1)] ++;
					upDiagSum[i+j] ++;
				}
			}
		}
		
		conflictRatio = 0;
		int pos = 0;
		for (int i = 0; i < horSum.length; i++) {
			pos++;
			if (horSum[i] > k) conflictRatio += 1;
		}
		for (int i = 0; i < vertSum.length; i++) {
			pos++;
			if (vertSum[i] > k) conflictRatio += 1;
		}
		for (int i = 0; i < downDiagSum.length; i++) {
			pos+=2;
			if (downDiagSum[i] > k) conflictRatio += 1;
			if (upDiagSum[i] > k) conflictRatio += 1;
		}
		
		conflictRatio /= pos;
	}
}
