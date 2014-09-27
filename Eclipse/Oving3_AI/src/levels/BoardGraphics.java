package levels;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Arrays;

import javax.swing.JComponent;

class BoardGraphics extends JComponent {
	
	private GridTile[][] gridTiles;
	private GridTile[][] orignalGridTiles;
	
	private final int re = 30; //Rectangel edges
	private final int sre = 10; //Small Rectangel edges
	private final int pixelBetweenTiles = 1;
	private final boolean allowSmallerBoxes = true;
	
	
	 public BoardGraphics(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;
		orignalGridTiles = copyOf(gridTiles);
	}
	 
	 public GridTile[][] copyOf(GridTile[][] originalArray)  
	    {  
		 GridTile[][] newArray = new GridTile[originalArray.length][originalArray[0].length];  
	        for (int x = 0; x < originalArray.length; x++)  
	        {  
	            for (int y = 0; y < originalArray[0].length; y++)  
	            {  
	                newArray[x][y]= new GridTile(originalArray[x][y].getSymbol());  
	            }  
	        }  
	        return newArray;  
	    }

	public void paint(Graphics g) {
		
		for (int tall = 1; tall <= 2; tall++) {
			
		
		    for (int y = 0; y < gridTiles.length; y++) {
				for (int x = 0; x < gridTiles[0].length; x++) {
					GridTile tile = gridTiles[y][x]; 
					if(tall == 1) tile = orignalGridTiles[y][x];
						
					//TILE NOT VISITED
					if(tile.getSymbol() == '.'){
						g.setColor(Color.WHITE);
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					//WALL
					else if(tile.getSymbol() == '#'){
						g.setColor(Color.DARK_GRAY);
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					//TILE, IN CLOSED
					else if(tile.getSymbol() == '-'){
						g.setColor(Color.BLACK);
						if(allowSmallerBoxes) g.fillRect((re+pixelBetweenTiles)*x+ re/2 - sre/2,(re+pixelBetweenTiles)*y+ re/2 -sre/2,sre,sre);
						else g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					//TILE, CHECKED
					else if(tile.getSymbol() == ',' || tile.getSymbol() == 'm'){
						g.setColor(Color.GRAY);
						if(allowSmallerBoxes) g.fillRect((re+pixelBetweenTiles)*x+ re/2 - sre/2,(re+pixelBetweenTiles)*y+ re/2 -sre/2,sre,sre);
						else g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					else if(tile.getSymbol() == 'r'){
						g.setColor(new Color(110,95,80,255));
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					//START
					else if(tile.getSymbol() == 'A'){
						g.setColor(Color.GREEN);
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					//GOAL
					else if(tile.getSymbol() == 'B'){
						g.setColor(Color.RED);
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					// Path to goal
					else if(tile.getSymbol() == 'G'){
						g.setColor(Color.YELLOW);
						if(allowSmallerBoxes) g.fillRect((re+pixelBetweenTiles)*x+ re/2 - sre/2,(re+pixelBetweenTiles)*y+ re/2 -sre/2,sre,sre);
						else g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
					else if(tile.getSymbol() == 'f'){
						g.setColor(new Color(68,94,26,250));
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
					else if(tile.getSymbol() == 'g'){
						g.setColor(new Color(190,235,178,250));
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
					else if(tile.getSymbol() == 'w'){
						g.setColor(Color.BLUE);
						g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
					}
					
				}
		    }
	    
		}
		

	  }

	public void setGridTiles(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;
		orignalGridTiles = gridTiles.clone();
//		repaint();

	}

	  
	  
	  
	}
	
/*
	public class  {
		  public static void main(String[] a) throws FileNotFoundException, IOException {
			  
			ArrayList<String> lines = ReadBoardTXT.readBoard("src/levels/board-1-1.txt");
	
			JFrame window = new JFrame();
			MyCanvas c = new MyCanvas();
			c.setLines(lines);
			window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			window.setBounds(30, 30, 900, 900);
			window.getContentPane().add(c);
			window.setVisible(true);
		  }
	}
*/