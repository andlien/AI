package levels;



import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;

import levels.ReadBoardTXT;
import levels.GridTile;

public class Mainprogram {

	public static void main(String[] args) throws FileNotFoundException, IOException {

		ArrayList<String> lines = ReadBoardTXT.readBoard("src/levels/board-1-1.txt");
		Board board = new Board(lines);
		
	    GridTile currentTile;
	    PriorityQueue<GridTile> open = board.getOpen();
	    ArrayList<GridTile> closed = board.getClosed();
	    open.add(board.startTile);
	    
	    while (board.endTile.getParent() != null) {
	    	if (open.isEmpty()) {
	    		throw new RuntimeException("No solution found!");
	    	}
	    	
	    	currentTile = open.poll();
	    	closed.add(currentTile);
	    	
	    	
	    }
	    
	}
}
