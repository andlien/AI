package levels;

import java.awt.Graphics;

import javax.swing.JComponent;

@SuppressWarnings("serial")

//the view
//Handles all the graphics
class BoardGraphics extends JComponent {
	
	private GridTile[][] gridTiles;
	
	private final int re = 30; //Rectangel edges
	private final int sre = 10; //Small Rectangel edges
	private final int pixelBetweenTiles = 0;
	private final boolean allowSmallerBoxes = true;
	
	
	 public BoardGraphics(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;
	}

	 //The board is repainted from the mainprogram class at a given intervall
	public void paint(Graphics g) {
		    for (int y = 0; y < gridTiles.length; y++) {
				for (int x = 0; x < gridTiles[0].length; x++) {
					GridTile tile = gridTiles[y][x]; 
					Symbol sym = tile.getSymbol();
					
					//Old symbol is used when a tile is examined and the symbol has changed. 
					//Old symbol saved the previous value and displays it correctly under the new symbol
					Symbol oldSym = tile.getOldSymbol();
					
					if(oldSym != null){
						g.setColor(oldSym.getColor());//The color is saved at the symbol enum class.
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
					g.setColor(sym.getColor());
					
					//When a symbols is examined it is displayed as a small box on top of the orignal tile 
					// The origianl tile is always a big rectangle
					if(sym.isSmall() && allowSmallerBoxes){
						g.fillRect((re+pixelBetweenTiles)*x+ re/2 - sre/2,(re+pixelBetweenTiles)*y+ re/2 -sre/2,sre,sre);

					}
					else {
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
				}
		    }
	    

		

	  }
	  
	  
}
