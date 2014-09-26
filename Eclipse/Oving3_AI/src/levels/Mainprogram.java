package levels;



import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

import levels.ReadBoardTXT;
import levels.GridTile;

public class Mainprogram {

	public static void main(String[] args) throws FileNotFoundException, IOException {

		ArrayList<String> lines = ReadBoardTXT.readBoard("src/levels/board-1-1.txt");
		
		GridTile[][] grid = new GridTile[lines.get(0).length()][lines.size()];
		GridTile startTile;
		GridTile endTile;
		
	    for (int i = 0; i < lines.size(); i++) {
	    	String line = lines.get(i);
			for (int j = 0; j < line.length(); j++) {
				grid[i][j] = new GridTile( line.charAt(j));
				if(line.charAt(j) == 'A') startTile = grid[i][j];
				else if(line.charAt(j) == 'B') endTile = grid[i][j];
			}
	    }
	    
	    ArrayList<GridTile> open = new ArrayList<GridTile>();
	    ArrayList<GridTile> closed = new ArrayList<GridTile>();
	    
	    
	    
	}
}
