import java.util.Arrays;
import java.util.Random;

public class Sa {
	
	public static void main(String[] args) {
		int lengde = 20;
		int[] tall = new int[lengde];
		for (int i = 0; i < tall.length; i++) {
			tall[i] = i * 2;
		}
		System.out.println(Arrays.toString(tall));
		Random randomGenerator = new Random();
		int randomIndex = randomGenerator.nextInt(lengde);
		System.out.println(randomIndex);
		
		float t_max = 200;
		float t = t_max;
		float p = randomIndex;
		
		
		while(t > 0){
			float f_of_p = tall[(int) p];
			
			if(f_of_p > (lengde-2)*2){
				System.out.println("Svar: " + p);
				break;
			}
			
			int[] naboer = generateNeighbors();
			float p_max = getBestNabo(naboer, tall);
			float f_of_p_max = tall[(int) p_max];
			
			//System.out.println("f_of_p_max: " + f_of_p_max);
			//System.out.println("f_of_p: " + f_of_p);
			
			float q = (f_of_p_max - f_of_p) / f_of_p;
			float p_temp = (float) Math.exp(-q/t);
			float pp = Math.min(1, p_temp);
			
			float x = randomGenerator.nextFloat();
			//System.out.println("x: " + x);
			//System.out.println("q: " + q);
			System.out.println("p: " + pp);
			
			
			
			if(x > pp){
				if(f_of_p < f_of_p_max) p = p_max;
				//System.out.println("Max selected");
			}
			else{
				int randomP = randomGenerator.nextInt(naboer.length);
				p = naboer[randomP];
				//System.out.println("Random selected");
			}
			
			System.out.println(" ");
			t-=20;
		}
		
		System.out.println("Timout svar: index: " + p + ", value: " + tall[(int)p]);

	}
	static int getBestNabo(int[] naboer, int[] tall){
		int p_max = naboer[0];
		
		for (int i = 0; i < naboer.length; i++) {
			
			if(p_max < tall[i]) p_max = naboer[i];
		}
		
		return p_max;
	}
	
	static int[] generateNeighbors(){
		int[] naboer = new int[4];
		Random randomGenerator = new Random();
		
		
		for (int i = 0; i < naboer.length; i++) {
			int randomInt = randomGenerator.nextInt(20);
			naboer[i] = randomInt;
		}
		
		return naboer;
	}

}
