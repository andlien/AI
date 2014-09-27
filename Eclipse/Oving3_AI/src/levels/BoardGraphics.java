package levels;

import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JComponent;

class BoardGraphics extends JComponent {
	
	private GridTile[][] gridTiles;
	private final int re = 30; //Rectangel edges
	private final int pixelBetweenTiles = 1;
	
	
	 public BoardGraphics(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;
	}

	public void paint(Graphics g) {
		
		
	    for (int y = 0; y < gridTiles.length; y++) {
			for (int x = 0; x < gridTiles[0].length; x++) {
				GridTile tile = gridTiles[y][x];
				
				//TILE NOT VISITED
				if(tile.getSymbol() == '.'){
					g.setColor(Color.WHITE);
					g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
				}
				//WALL
				else if(tile.getSymbol() == '#'){
					g.setColor(Color.BLUE);
					g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
				}
				//TILE, IN CLOSED
				else if(tile.getSymbol() == '-'){
					g.setColor(Color.BLACK);
					g.fillRect((re+pixelBetweenTiles)*x,(re+pixelBetweenTiles)*y,re,re);
				}
				//TILE, CHECKED
				else if(tile.getSymbol() == ','){
					g.setColor(Color.GRAY);
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
			}
	    }
		

	  }

	public void setGridTiles(GridTile[][] gridTiles) {
		this.gridTiles = gridTiles;
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