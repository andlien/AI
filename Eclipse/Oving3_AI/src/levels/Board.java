package levels;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Board {
	GridTile[][] gridTiles;
	
	int startTileX;
	int startTileY;
	int endTileX;
	int endTileY;
	GridTile startTile, endTile;
	private String searchType;
	
	private Queue<GridTile> open;
	private ArrayList<GridTile> closed;
	
	public Board(ArrayList<String> lines, String typeSearch){
		gridTiles = new GridTile[lines.size()][lines.get(0).length()];
		this.searchType = typeSearch;
		
	    for (int i = 0; i < lines.size() ; i++) {
	    	String line = lines.get(i);
	    	
			for (int j = 0; j < line.length() ; j++) {
				gridTiles[i][j] = new GridTile( line.charAt(j));
				
				if(line.charAt(j) == 'A'){
					startTileX = j;
					startTileY = i;
					startTile = gridTiles[i][j];
				}
				else if(line.charAt(j) == 'B'){
					endTileX = j;
					endTileY = i;
					endTile = gridTiles[i][j];
				}
			}
	    }
	    
	    if (typeSearch.equals("BFS")) {
	    	open = new LinkedList<GridTile>();
	    } else {
	    	open = new PriorityQueue<GridTile>();
	    }
	    closed = new ArrayList<GridTile>();
	    
	    setHInAllTiles();
	    

	    
	    
	}
	
	private void setHInAllTiles(){
	    for (int y = 0; y < gridTiles.length; y++) {
	    	
			for (int x = 0; x < gridTiles[0].length; x++) {
				setHInTile(gridTiles[y][x],x,y);
			}
	    }
	}
	
	private void setHInTile(GridTile tile, int x, int y){
		int h = manhattenDistanceToEndTile(x, y);
		tile.setH(h);
	}
	
	
	private int manhattenDistanceToEndTile(int x, int y){
		if (!this.searchType.equals("A*"))
			return 0;
		int xDist = Math.abs(x - endTileX); 
		int yDist = Math.abs(y - endTileY); 

		return xDist + yDist;
	}
	
	public Queue<GridTile> getOpen() {
		return open;
	}
	
	public ArrayList<GridTile> getClosed() {
		return closed;
	}
	
	public GridTile[][] getGridTiles() {
		return gridTiles;
	}

	public GridTile getStartTile() {
		return startTile;
	}

	public GridTile getEndTile() {
		return endTile;
	}
	
	public boolean isSolution(GridTile tile) {
		return tile.equals(endTile);
	}
	
	public ArrayList<GridTile> getSurroundingTiles(GridTile tile) {
		ArrayList<GridTile> tiles = new ArrayList<GridTile>();
		for (int y = 0; y < gridTiles.length; y++) {
			for (int x = 0; x < gridTiles[0].length; x++) {
				if (gridTiles[y][x].equals(tile)) {
					if (x > 0 && !gridTiles[y][x-1].getSymbol().equals(Symbol.WALL))
						tiles.add(gridTiles[y][x-1]);
					if (x < gridTiles[0].length - 1 && !gridTiles[y][x+1].getSymbol().equals(Symbol.WALL))
						tiles.add(gridTiles[y][x+1]);
					if (y > 0 && !gridTiles[y-1][x].getSymbol().equals(Symbol.WALL))
						tiles.add(gridTiles[y-1][x]);
					if (y < gridTiles.length - 1 && !gridTiles[y+1][x].getSymbol().equals(Symbol.WALL))
						tiles.add(gridTiles[y+1][x]);
					
				}
			}
	    }
		return tiles;
	}
	
	public void propagateBetterPath(GridTile tile) {
		ArrayList<GridTile> possibleKids = getSurroundingTiles(tile);
		for (GridTile kid : possibleKids) {
			if (tile.equals(kid.getParent())) {
				kid.setCurrentG(kid.getParent().getCurrentG() + kid.getSymbolCost());
				propagateBetterPath(kid);
			}
		}
	}
}
