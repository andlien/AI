package levels;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.concurrent.TimeUnit;

import javax.swing.JFrame;

public class Mainprogram {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		
		//String typeOfSearch = "A*";
		//String typeOfSearch = "Dijkstra";
		String typeOfSearch = "BFS";

		
		String adresse = "/levels/board-2-3.txt";

		// Read and create board from textfile
		ArrayList<String> lines = ReadBoardTXT.readBoard(adresse);
		Board board = new Board(lines, typeOfSearch);
		
		// Create graphics
		BoardGraphics bg = createBoardGraphics(board.getGridTiles(),typeOfSearch,adresse);
	
		// Initialize the lists
	    GridTile currentTile;
	    Queue<GridTile> open = board.getOpen();
	    ArrayList<GridTile> closed = board.getClosed();

	    // Algorithm start
	    int it = 0;
	    open.add(board.getStartTile());
	    
	    board.getStartTile().setCurrentG(0);
	    
	    // Possible?
	    boolean done = board.isSolution(board.getStartTile());
	    
	    while (!done) {
	    	
	    	//Repaint board
	    	tick(100, bg);
	    	
	    	// All tiles explored, but no solution found
	    	if (open.isEmpty()) {
	    		throw new RuntimeException("No solution found!");
	    	}
	    	
	    	// Explore currentTile
	    	currentTile = open.poll();

	    	// Mark/paint current tile as closed
	    	closed.add(currentTile);
	    	if (!currentTile.getSymbol().equals(Symbol.START))
	    		currentTile.setSymbol(Symbol.CLOSED);
	    	
	    	ArrayList<GridTile> succ = board.getSurroundingTiles(currentTile);
	    	succ.remove(currentTile.getParent());
	    	
	    	// Process neighbouring nodes except parent of the current tile
	    	for (GridTile tile : succ) {
	    		it++;
	    		bg.setIterations(it);
	    		// If tile is the end, we're done
	    		if (board.isSolution(tile)) {
	    			tile.setParent(currentTile);
	    			done = true;
	    			break;
	    		}
	    		
	    		// First time tile is visited
				if (!open.contains(tile) && !closed.contains(tile)) {
					// Paint it as checked
					if (!tile.getSymbol().equals(Symbol.END))
						tile.setSymbol(Symbol.CHCEKED);
					tile.setParent(currentTile);
					
					// set g of neighbouring node to cost of parent + cost from parent to this 
					tile.setCurrentG(currentTile.getCurrentG() + tile.getSymbolCost());
					open.add(tile);
				}
				
				// Already visited, but found cheaper path
				else if (currentTile.getCurrentG() + tile.getSymbolCost() < tile.getCurrentG()) {
					//Update parent and g
					tile.setParent(currentTile);
					tile.setCurrentG(currentTile.getCurrentG() + tile.getSymbolCost());
					//Has children that must be updated
					if (closed.contains(tile)) {
						// Updates cost recursively
						board.propagateBetterPath(tile);
					}
				}
				
			}
	    }
	    
	    // Paints shortest path
	    GridTile t = board.getEndTile().getParent();
	    while (t.getParent() != null) {
	    	t.setSymbol(Symbol.SHORTEST);
	    	t = t.getParent();
	    	bg.repaint();
	    }
	    System.out.println(it);
	    
	}
	
	private static void tick(int msec, BoardGraphics bg) {
		try {
    		TimeUnit.MILLISECONDS.sleep(msec);
    	} catch (InterruptedException e) {
    		System.err.println(e);
    	}
		bg.repaint();
	}
	
	
	private static BoardGraphics createBoardGraphics(GridTile[][] gridTiles, String adresse, String algorithm){
		
		JFrame window = new JFrame();
		BoardGraphics c = new BoardGraphics(gridTiles, algorithm, adresse);
		//c.setLines(lines);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setBounds(30, 30, 1300, 900);
		window.getContentPane().add(c);
		window.setVisible(true);
		
		return c;
	}
}
