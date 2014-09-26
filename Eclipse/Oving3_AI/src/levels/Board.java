package levels;

import java.util.ArrayList;

public class Board {
	GridTile[][] gridTiles;
	
	int startTileX;
	int startTileY;
	int endTileX;
	int endTileY;
	
	GridTile currentTile;
	
	
	public Board(ArrayList<String> lines){
		gridTiles = new GridTile[lines.get(0).length()][lines.size()];
		
	    for (int i = 0; i < lines.size(); i++) {
	    	String line = lines.get(i);
			for (int j = 0; j < line.length(); j++) {
				gridTiles[i][j] = new GridTile( line.charAt(j));
				
				if(line.charAt(j) == 'A'){
					startTileX = i;
					startTileY = j;
				}
				else if(line.charAt(j) == 'B'){
					endTileX = i;
					endTileY = j;
				}
			}
	    }
	    
	    setHInAllTiles();
	    
	    
	    
	}
	
	private void setHInAllTiles(){
	    for (int y = 0; y < gridTiles.length; y++) {
			for (int x = 0; x < gridTiles[0].length; x++) {
				setHInTile(gridTiles[x][y],x,y);
			}
	    }
	}
	
	private void setHInTile(GridTile tile, int x, int y){
		int h = manhattenDistanceToEndTile(x, y);
		tile.setH(h);
	}
	
	
	private int manhattenDistanceToEndTile(int x, int y){
		int xDist = Math.abs(x - endTileX); 
		int yDist = Math.abs(y - endTileY); 
		
		return xDist + yDist;
	}
	
	
	
}
