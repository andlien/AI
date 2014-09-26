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
		        StringBuilder sb = new StringBuilder();
		        String line = br.readLine();
		        
		        int index = 0;
		        while (line != null) {
		            sb.append(line);
		            sb.append(System.lineSeparator());
		            line = br.readLine();
		            if(line != null) lines.add(line);
		        }
		       // System.out.println(lines);
		       // String everything = sb.toString();
		        
		        return lines;
		    }
	}
}
