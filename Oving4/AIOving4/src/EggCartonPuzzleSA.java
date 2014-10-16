import java.util.ArrayList;
import java.util.Random;


public class EggCartonPuzzleSA {

	public static void main(String[] args) {
		
		
		int size = 8;
		int[][] eggCarton = new int[size][size];
		int numberOfEggsInEachRow = 3;
		
		Random randomGenerator = new Random();
		
		
		for (int i = 0; i < eggCarton.length; i++) {
			
			ArrayList<Integer> avaiableIndices = getArrayTo(size);// En liste med tallene 0,...,n
			for (int j = 0; j < numberOfEggsInEachRow; j++) {

				int randomIndex = randomGenerator.nextInt(avaiableIndices.size());
				int index = avaiableIndices.get(randomIndex);
				avaiableIndices.remove(randomIndex);
				eggCarton[i][index] = 1;
				
			}
		}
		
		State startState = new State(eggCarton);
		startState.printState();
		
		generateNeighbors(startState,numberOfEggsInEachRow);
		
		//findColumnsWithMoreEggsThenAllowed(eggCarton,numberOfEggsInEachRow);
		//findColumnsWithLessEggsThenAllowed(eggCarton,numberOfEggsInEachRow);

	}
	
	private static ArrayList<Integer> getArrayTo(int to){
		ArrayList<Integer> array = new ArrayList<Integer>();
		for (int i = 0; i < to; i++) {
			array.add(i);
			//System.out.println(i);
		}
		
		return array;
	}
	
	
	public static void sa(State firstState, float t_max, float dt, int numberOfNeighbors ){
		
		Random randomGenerator = new Random();

		
		// Set the temperature, T, to it’s starting value: Tmax
		float t = t_max;
		
		while(t > 0){
			
		}
	}
	
	
	public static State generateNeighbors(State state, int numberOfEggsInEachRow){
		int[][] eggCarton = state.getCloneEggCarton();
		
		ArrayList<Integer> troubleColumns = findColumnsWithMoreEggsThenAllowed(eggCarton,numberOfEggsInEachRow);
		ArrayList<Integer> freeColumns = findColumnsWithLessEggsThenAllowed(eggCarton,numberOfEggsInEachRow);
		
		Random randomGenerator = new Random();
		
		int randomStartPoint = randomGenerator.nextInt(eggCarton.length );
		int randomStartPoint3 = randomGenerator.nextInt(eggCarton.length /2);
		
		int randomStartPoint2 = randomGenerator.nextInt(troubleColumns.size()  );
		
		int swaps = 0;
		
		for (int i = randomStartPoint2; i < troubleColumns.size(); i++) {
			
			if(swaps > 0) break;
			
			for (int j = randomStartPoint; j < eggCarton.length; j++) {
				if(eggCarton[i][j] == 1){
					//System.out.println(i + "," + j);
					
					for (int j2 = randomStartPoint3; j2 < freeColumns.size(); j2++) {
						if(eggCarton[i][j2] == 0){
							
							eggCarton[i][j] = 0;
							eggCarton[i][j2] = 1;
							//System.out.println("Swapped (" + j +"," + i + ") with ("  + j2 +"," + i + ")");
							swaps ++;
							break;
						}
					}
					break;
				}
				
			}
		}
		
		if(swaps == 0){
			
			for (int i = 0; i < eggCarton.length; i++) {
				eggCarton[randomStartPoint][i] = 0;
			}
			
			ArrayList<Integer> avaiableIndices = getArrayTo(eggCarton.length);// En liste med tallene 0,...,n
			for (int j = 0; j < numberOfEggsInEachRow; j++) {

				int randomIndex = randomGenerator.nextInt(avaiableIndices.size());
				int index = avaiableIndices.get(randomIndex);
				avaiableIndices.remove(randomIndex);
				eggCarton[randomStartPoint][index] = 1;
				
			}
			System.out.println("Ingen swaps. Linje + " + randomStartPoint + "byttet ut");
		}
		System.out.println("-");
		state.printState();
		
		return new State(eggCarton);
	}
	
	private static ArrayList<Integer> findColumnsWithMoreEggsThenAllowed(int[][] eggCarton, int allowdEggs){
		ArrayList<Integer> columns = new ArrayList<Integer>();
		for (int i = 0; i < eggCarton[0].length; i++) {
			int numberOfEggs = 0;
			for (int j = 0; j < eggCarton.length; j++) {
				numberOfEggs += eggCarton[j][i];
			}
			if(numberOfEggs > allowdEggs){
				columns.add(i);
				//System.out.println("TroubleColumn: " + i);
			}
		}
		
		return columns;
	}
	
	private static ArrayList<Integer> findColumnsWithLessEggsThenAllowed(int[][] eggCarton, int allowdEggs){
		ArrayList<Integer> columns = new ArrayList<Integer>();
		for (int i = 0; i < eggCarton[0].length; i++) {
			int numberOfEggs = 0;
			for (int j = 0; j < eggCarton.length; j++) {
				numberOfEggs += eggCarton[j][i];
			}
			if(numberOfEggs < allowdEggs){
				columns.add(i);
				//System.out.println("Free columns: " + i);
			}
		}
		
		return columns;
	}

}
