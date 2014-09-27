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
	
	    GridTile currentTile;
	    PriorityQueue<GridTile> open = board.getOpen();
	    ArrayList<GridTile> closed = board.getClosed();
	    open.add(board.getStartTile());
	    
	    board.getStartTile().setCurrentG(0);
	    
	    boolean done = false;
	    
	    while (!done) {
	    	
	    	tick(100, bg);
	    	
	    	if (open.isEmpty()) {
	    		throw new RuntimeException("No solution found!");
	    	}
	    	
	    	currentTile = open.poll();
	    	closed.add(currentTile);

	    	if (board.isSolution(currentTile))
	    		break;
	    	if (!currentTile.getSymbol().equals(Symbol.START))
	    		currentTile.setSymbol(Symbol.CLOSED);
	    	
	    	ArrayList<GridTile> succ = board.getSurroundingTiles(currentTile);
	    	succ.remove(currentTile);
	    	
	    	for (GridTile tile : succ) {
	    		if (board.isSolution(tile)) {
	    			tile.setParent(currentTile);
	    			done = true;
	    			break;
	    		}
		    	if (!tile.getSymbol().equals(Symbol.END) && !closed.contains(tile))
		    		tile.setSymbol(Symbol.CHCEKED);
	    		// First time tile is visited
				if (!open.contains(tile) && !closed.contains(tile)) {
					tile.setParent(currentTile);
					tile.setCurrentG(currentTile.getCurrentG() + tile.getSymbol().getCost());
					open.add(tile);
				}
				
				// Already visited, but found cheaper path
				else if (currentTile.getCurrentG() + tile.getSymbol().getCost() < tile.getCurrentG()) {
					tile.setParent(currentTile);
					tile.setCurrentG(currentTile.getCurrentG() + tile.getSymbol().getCost());
					//Has children that must be updated
					if (closed.contains(tile)) {
						board.propagateBetterPath(tile);
					}
				}
				
			}
	    }
	    GridTile t = board.getEndTile().getParent();
	    while (t.getParent() != null) {
	    	t.setSymbol(Symbol.SHORTEST);
	    	t = t.getParent();
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
		window.setBounds(30, 30, 1300, 900);
		window.getContentPane().add(c);
		window.setVisible(true);
		
		return c;
	}
}
