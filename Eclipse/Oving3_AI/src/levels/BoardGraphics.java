package levels;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Arrays;

import javax.swing.JComponent;

@SuppressWarnings("serial")
class BoardGraphics extends JComponent {
	
	private GridTile[][] gridTiles;
	
	private final int re = 30; //Rectangel edges
	private final int sre = 10; //Small Rectangel edges
	private final int pixelBetweenTiles = 0;
	private final boolean allowSmallerBoxes = true;
	
	
	 public BoardGraphics(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;
	}


	public void paint(Graphics g) {
		
	
		    for (int y = 0; y < gridTiles.length; y++) {
				for (int x = 0; x < gridTiles[0].length; x++) {
					GridTile tile = gridTiles[y][x]; 
					Symbol sym = tile.getSymbol();
					Symbol oldSym = tile.getOldSymbol();
					
					
					if(oldSym != null) g.setColor(oldSym.getColor());
					g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					
					g.setColor(sym.getColor());
					
					if(sym.isSmall() && allowSmallerBoxes){
						g.fillRect((re+pixelBetweenTiles)*x+ re/2 - sre/2,(re+pixelBetweenTiles)*y+ re/2 -sre/2,sre,sre);

					}
					else {
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
				}
		    }
	    

		

	  }

	public void setGridTiles(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;

	}

	  
	  
	  
	}
