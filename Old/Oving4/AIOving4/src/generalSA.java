import java.util.Random;

public class generalSA {
	
	
	//En generell Simulated annealing algoritme for å finne det høyeste tallet i en gitt liste
	public static float simulatedAnnealing (float[] tall, float t_max, float dt, int numberOfNeighbors ){
		
		Random randomGenerator = new Random();
		int randomIndex = randomGenerator.nextInt(tall.length);
		
		// Set the temperature, T, to it’s starting value: Tmax
		float t = t_max;
		
		float p = randomIndex;
		
		while(t > 0){
			
			//Evaluate P with an objective function, F. This yields the value F(P).
			float f_of_p = tall[(int) p];
			
			// Generate n neighbors of P in the search space: (P1, P2, ..., Pn).
			int[] neighbors = generateNeighbors(numberOfNeighbors, tall.length);
			
			//Evaluate each neighbor, yielding (F(P1), F(P2), ..., F(Pn)).
			float[] f_neighbors = objectFunction(neighbors, tall);
			
			//Let Pmax be the neighbor with the highest evaluation
			int p_max = getPMax(f_neighbors);
			float f_of_p_max = tall[p_max];
			
			
			float q = (f_of_p_max - f_of_p) / f_of_p;
			float p_temp = (float) Math.exp(-q/t);
			float pp = Math.max(1, p_temp);
			
			//Generate x, a random real number in the closed range [0,1].
			float x = randomGenerator.nextFloat();		
			
			//Velger den indeksen med høyest verdi
			//Exploiting
			if(f_of_p_max > f_of_p){
				f_of_p = f_of_p_max;
				p = p_max;
			}
			
			//Velger en tilfeldig nabo
			//Exploring
			if(x > pp){
				int randomP = randomGenerator.nextInt(neighbors.length);
				p = neighbors[randomP];
			}

			t-= dt;
		}
		
		return p;

	}
	//Ønsker å finne det høyeste tallet i listen
	// I dette generelle eksmeplet er det kun verdien i seg selv som avgjør
	//Jo høyere tall, jo bedre
	static float[] objectFunction(int[] neighbors, float[] tall){
		float[] f_neighbors = new float[neighbors.length];
		
		for (int i = 0; i < neighbors.length; i++) {
			f_neighbors[i] = tall[neighbors[i]];
		}
		
		return f_neighbors;
	}
	
	// Finner indeksen til det den høyeste verdien blandt naboene
	static int getPMax(float[] f_neighbors){
		float f_max = f_neighbors[0]; //Høyeste verdi funnet
		int p_max = 0; // Indeksen til naboen med høyest verdi
		
		for (int i = 0; i < f_neighbors.length; i++) {
			
			if(f_max < f_neighbors[i]){
				f_max = f_neighbors[i];
				p_max = i;
			}
		}
		
		return p_max;
	}
	
	//Generer et gitt antall med naboer
	static int[] generateNeighbors(int numberOfNeighbors, int number){
		int[] neighbors = new int[numberOfNeighbors];
		Random randomGenerator = new Random();
		
		
		for (int i = 0; i < neighbors.length; i++) {
			int randomInt = randomGenerator.nextInt(number);
			neighbors[i] = randomInt;
		}
		
		return neighbors;
	}

}
