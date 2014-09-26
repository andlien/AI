package levels;



import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

import levels.CreateLevels;
import levels.GridTile;

public class Mainprogram {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		// TODO Auto-generated method stub
		System.out.println("Hei");
		
		ArrayList<String> lines = CreateLevels.readLevel();
		
		GridTile[][] grid = new GridTile[lines.get(0).length()][lines.size()];
		
	    for (int i = 0; i < lines.size(); i++) {
	    	String line = lines.get(i);
			for (int j = 0; j < line.length(); j++) {
				grid[i][j] = new GridTile( line.charAt(j));
			}
	    }

	}

}
