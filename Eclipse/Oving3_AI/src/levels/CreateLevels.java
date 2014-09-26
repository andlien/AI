package levels;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class CreateLevels {

	
	
	public static ArrayList<String> readLevel() throws FileNotFoundException, IOException{
		ArrayList<String> lines = new ArrayList<String>();
		
		   try(BufferedReader br = new BufferedReader(new FileReader("src/levels/board-1-1.txt"))) {
		       String line; 
			   
		        while ((line = br.readLine()) != null) {
		            if(line != null) lines.add(line);
		        }
		        
		        return lines;
		    }
	}
}
