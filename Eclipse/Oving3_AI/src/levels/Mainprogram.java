package levels;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.concurrent.TimeUnit;

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
	    
	    while (true) {
	    	
	    	tick(1, bg);
	    	
	    	if (open.isEmpty()) {
	    		throw new RuntimeException("No solution found!");
	    	}
	    	
	    	currentTile = open.poll();
	    	closed.add(currentTile);
	    	currentTile.setSymbol('-');
	    	
	    	if (board.isSolution(currentTile))
	    		break;
	    	
	    	ArrayList<GridTile> succ = board.getSurroundingTiles(currentTile);
	    	succ.remove(currentTile.getParent());
	    	
	    	for (GridTile tile : succ) {
	    		tile.setSymbol(',');
	    		tick(500, bg);
	    		// First time tile is visited
				if (!open.contains(tile) && !closed.contains(tile)) {
					tile.setParent(currentTile);
					tile.setCurrentG(currentTile.getCurrentG() + 1);
					open.add(tile);
				}
				
				// Already visited, but found cheaper path
				else if (currentTile.getCurrentG() + 1 < tile.getCurrentG()) {
					tile.setParent(currentTile);
					tile.setCurrentG(currentTile.getCurrentG() + 1);
					//Has children that must be updated
					if (closed.contains(tile)) {
						board.propagateBetterPath(tile);
					}
				}
				
			}
	    }
	    
	}
	
	private static void tick(int msec, BoardGraphics bg) {
		try {
    		TimeUnit.MILLISECONDS.sleep(msec);
    	} catch (InterruptedException e) {
    		System.err.println(e);
    	}
		bg.repaint();
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
