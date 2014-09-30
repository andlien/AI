package levels;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class ReadBoardTXT {

	//This class 
	
	public static ArrayList<String> readBoard(String adresse) throws FileNotFoundException, IOException{
		ArrayList<String> lines = new ArrayList<String>();

		BufferedReader br = new BufferedReader(new InputStreamReader(InputStream.class.getResourceAsStream(adresse)));
		String line; 

		while ((line = br.readLine()) != null) {
			if(line != null) lines.add(line);
		}

		return lines;

	}
}
