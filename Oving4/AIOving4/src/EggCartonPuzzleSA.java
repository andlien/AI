import java.util.ArrayList;
import java.util.Random;


public class EggCartonPuzzleSA {

	public static void main(String[] args) {
		
		int[][] eggCarton = new int[5][5];
		int numberOfEggsInEachRow = 2;
		
		
		getArrayTo(5);
		
		for (int i = 0; i < eggCarton.length; i++) {
			for (int j = 0; j < eggCarton[0].length; j++) {
				
			}
		}

	}
	
	private static ArrayList<Integer> getArrayTo(int to){
		ArrayList<Integer> array = new ArrayList<Integer>();
		for (int i = 0; i < to; i++) {
			array.add(i);
			System.out.println(i);
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
	
	
	public static void generateNaboer(){
		
	}

}
