import java.util.ArrayList;
import java.util.Random;


public class EggCartonPuzzleSA {
	
	private static final int size = 10;
	private static final int numberOfEggsInEachRow = 3;

	public static void main(String[] args) {

		int[][] eggCarton = new int[size][size];
		
		Random randomGenerator = new Random();
		
		//Lager den første staten
		//Den første staten har akuratt antall tilate egg i hver rad, men ikke nødvendigvis i hver kolone
		for (int i = 0; i < eggCarton.length; i++) {
			
			ArrayList<Integer> avaiableIndices = getArrayTo(size);// En liste med tallene 0,...,n
			for (int j = 0; j < numberOfEggsInEachRow; j++) {
				//Plukker ut en tilgjengelig plass i listen og plasserer et egg der
				int randomIndex = randomGenerator.nextInt(avaiableIndices.size());
				int index = avaiableIndices.get(randomIndex);
				avaiableIndices.remove(randomIndex);
				eggCarton[i][index] = 1;
				
			}
		}
		
		State startState = new State(eggCarton, numberOfEggsInEachRow);
		System.out.println("StartState for n=m=" + size + " and k=" + numberOfEggsInEachRow);
		startState.printState();
		System.out.println("");
		State answer = eggCartonSimulatedAnnealing(startState, 10, 0.1f);
		answer.printState();
		System.out.println("Solution for n=m=" + size + " and k=" + numberOfEggsInEachRow);

	}
	
	public static State eggCartonSimulatedAnnealing (State startState, float t_max, float dt){
		float t = t_max;
		State currentState = startState;
		float targetCost = 0; //Høyeste godkjent kost for en optimal løsning
		
		int iterations = 0;
		
		while(t > 0){
			
			// Vi har definert at den optimale løsning som 0.
			// Hvis algoritmen finner en state med cost = targetCost er dette en optimal løsning og den vil bl returnert
			if(currentState.getCost() <= targetCost){
				System.out.println(" ");
				System.out.println("Optimal solution found after " + iterations + " iterations.");
				return currentState;
			}
			float currentStateCost = currentState.getCost();
			
			State neighbor = generateManyNeighborsAndFindLowestCost(currentState);
			float neighborCost = neighbor.getCost();
			
			//Standard q fra beskrivelsen
			float q = (neighborCost - currentStateCost) / currentStateCost;
			
			//p måtte tweakes litt for denne oppgaven
			//Passer på at p er i intervallet [0,1]
			float p =  (float) Math.exp(-q/t) -1;
			p *= 10;
			if(Float.isNaN(p)){ //Hvis q=0 vil p bli NaN. Passer på at det ikke skjer
				p = 1;
			}
			
			Random randomGenerator = new Random();
			float x = randomGenerator.nextFloat();
			
			//Velger den naboen med lavest cost (Teoretisk nærmest en løsning)
			//Exploting
			if(currentStateCost > neighborCost){
				currentState = neighbor;
			}
			
			//Velger en tilfeldig nabo
			//EXPLORING
			else if(x > p){
				currentState = generateNeighbors(currentState);
			}
			
			iterations ++;
			t -= dt;
			
		}
		System.out.println("No optimal solution found. Try again....");
		return currentState;
	}
	
	//Lager en liste med tallene fra 0 til den oppgitte verdien
	// F.eks to = 4 -> [0,1,2,3]
	private static ArrayList<Integer> getArrayTo(int to){
		ArrayList<Integer> array = new ArrayList<Integer>();
		for (int i = 0; i < to; i++) {
			array.add(i);
		}
		
		return array;
	}

	//Generer mange naboer og velger den med lavest cost
	// Bruker generateNeighbors
	public static State generateManyNeighborsAndFindLowestCost(State state){
		int numberOfNeighbors = 40;
		
		State bestNeighbor = generateNeighbors(state);
		
		for (int i = 0; i < numberOfNeighbors; i++) {
			State newNabo = generateNeighbors(state);
			if(newNabo.getCost() < bestNeighbor.getCost()){
				bestNeighbor = newNabo;
			}
		}
		
		return bestNeighbor;
	}
	
	//Generer en nabo
	//Har to metoder å lage nye naboer på
	//Det er 50/50 sjanse hvilken metode som blir valgt
	//Den første velger seg en rad i eggkartongen og stokker om på eggene på en tilfeldig måte
	
	//Den andre metoden lager seg to lister. En med alle koloene med for mange egg og en med alle kolonene med for få egg
	//Så prøver metoden å flytte egg fra koloner med for mange egg til koloner med for få egg
	//På grunn av tilfeldigheten, kan det hende at ingen ruter blir byttet om.
	// Da velger metoden en rad og bytter om alle tallene.
	public static State generateNeighbors(State state){
		int[][] eggCarton = state.getCloneEggCarton();
		Random randomGenerator = new Random();
		

		
		float type = randomGenerator.nextFloat();

		// Flytter rundt på eggene i en rad
		if(type < 0.50){
			int NumberOfSwaps = randomGenerator.nextInt(20);
			boolean targetFound = true;
			boolean targetFound2 = true;
			
			int row = randomGenerator.nextInt(eggCarton.length );
			
			for (int i = 0; i < NumberOfSwaps; i++) {
				
				while(targetFound){
					int rowIndex = randomGenerator.nextInt(eggCarton.length);
					
					if(eggCarton[row][rowIndex] == 1) {
						while(targetFound2){
							int rowIndex2 = randomGenerator.nextInt(eggCarton.length);
							if(eggCarton[row][rowIndex2] == 0) {
								eggCarton[row][rowIndex2] = 1;
								eggCarton[row][rowIndex] = 0;
								targetFound = false;
								targetFound2 = false;
								//return new State(eggCarton,numberOfEggsInEachRow);
							}
						}
					}
				}
			}
		}
		else{
			
			//Koloner med for mange egg
			ArrayList<Integer> troubleColumns = findColumnsWithMoreEggsThenAllowed(eggCarton,numberOfEggsInEachRow);
			//Koloner med "for få" egg. Altså koloner hvor det lovlig plass til flere egg
			ArrayList<Integer> freeColumns = findColumnsWithLessEggsThenAllowed(eggCarton,numberOfEggsInEachRow);
			
			//Legger inn litt tilfeldighet for å få en gjevn fordeling av flyttingene av eggene
			int randomStartPoint = randomGenerator.nextInt(eggCarton.length );
			int randomStartPoint3 = randomGenerator.nextInt(eggCarton.length /2);
			int randomStartPoint2 = randomGenerator.nextInt(Math.max(troubleColumns.size(),1 ) );
			
			int swaps = 0; //Antall egg som bytter plass
			
			for (int i = randomStartPoint2; i < troubleColumns.size(); i++) {
				
				for (int j = randomStartPoint; j < eggCarton.length; j++) {
					if(eggCarton[i][j] == 1){ //Hvis denne plassen har et egg
						
						for (int j2 = randomStartPoint3; j2 < freeColumns.size(); j2++) {
							if(eggCarton[i][j2] == 0){ //Hvis denne plassen er ledig
								
								//Da bytter de plass
								eggCarton[i][j] = 0;
								eggCarton[i][j2] = 1;
								swaps ++;
								break;
							}
						}
						break;
					}
					
				}
			}
			//Hvis det av eller annen grunn ikke ble noen endring av eggene, stokkes en tilfeldig rad om;
			//Dette kan også skje av ren tilfeldighet
			//Denne metoden er lik måten den første staten blir generert
			if(swaps == 0 || randomGenerator.nextFloat() > 0.6){
				
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
			}
		}
		
		return new State(eggCarton,numberOfEggsInEachRow);
	}
	
	//Går gjennom kolonene og returnerer en liste med alle kolonene med for mange egg
	private static ArrayList<Integer> findColumnsWithMoreEggsThenAllowed(int[][] eggCarton, int allowdEggs){
		ArrayList<Integer> columns = new ArrayList<Integer>();
		for (int i = 0; i < eggCarton[0].length; i++) {
			int numberOfEggs = 0;
			for (int j = 0; j < eggCarton.length; j++) {
				numberOfEggs += eggCarton[j][i];
			}
			if(numberOfEggs > allowdEggs){
				columns.add(i);
			}
		}
		
		return columns;
	}
	//Går gjennom kolonene og returnerer en liste med alle kolonene med ferre egg enn allowdEggs
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
