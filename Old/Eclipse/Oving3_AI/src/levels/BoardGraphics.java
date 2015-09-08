package levels;

import java.awt.Font;
import java.awt.Graphics;
import java.awt.RenderingHints;

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
	private String adresse;
	private String algorithm;
	private String iteration;
	
	
	 public BoardGraphics(GridTile[][] gridTiles,String adresse, String algorithm) {
		this.gridTiles = gridTiles;
		this.adresse = adresse;
		this.algorithm = algorithm;
	}
	 
	public void setIterations(int iter){
		iteration = "" + iter;
	}

	 //The board is repainted from the mainprogram class at a given intervall
	public void paint(Graphics g) {

		
		g.setFont(new Font("TimesRoman", Font.PLAIN, 20)); 
		g.drawString("Type of search: " + algorithm, 30, (gridTiles.length +1)* re);
		g.drawString("Board: " + adresse, 30, (gridTiles.length +2)* re);
		g.drawString("Iterations: " + iteration, 30, (gridTiles.length +3)* re);
		
		
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
