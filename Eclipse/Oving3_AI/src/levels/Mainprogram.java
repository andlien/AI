package levels;



import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;

import javax.swing.JFrame;

public class Mainprogram {

	public static void main(String[] args) throws FileNotFoundException, IOException {

		ArrayList<String> lines = ReadBoardTXT.readBoard("src/levels/board-1-1.txt");
		Board board = new Board(lines);
		
		BoardGraphics bg = createBoardGraphics(board.getGridTiles());
		

		//Kjør bg.repaint() for å tegne brettet på nytt
		
		
	    GridTile currentTile;
	    PriorityQueue<GridTile> open = board.getOpen();
	    ArrayList<GridTile> closed = board.getClosed();
	    open.add(board.getStartTile());
	    
	    while (board.endTile.getParent() != null) {
	    	if (open.isEmpty()) {
	    		throw new RuntimeException("No solution found!");
	    	}
	    	
	    	currentTile = open.poll();
	    	closed.add(currentTile);
	    	
	    	
	    }
	    
	    
	}
	
	
	private static BoardGraphics createBoardGraphics(GridTile[][] gridTiles){
		
		JFrame window = new JFrame();
		BoardGraphics c = new BoardGraphics(gridTiles);
		//c.setLines(lines);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setBounds(30, 30, 900, 900);
		window.getContentPane().add(c);
		window.setVisible(true);
		
		return c;
	}
}
