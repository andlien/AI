package levels;

import java.awt.Color;
import java.awt.Graphics;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

import javax.swing.JComponent;
import javax.swing.JFrame;

class MyCanvas extends JComponent {
	
	private ArrayList<String> lines;
	
	  public void paint(Graphics g) {
	    //g.drawRect (10, 10, 200, 200); 
	    
	    int height = 30;
	    int width = 30;
	   // g.setColor(Color.red);
	    System.out.println("heia");	    
	    
	    for (int i = 0; i < lines.size(); i++) {
	    	String line = lines.get(i);
			for (int j = 0; j < line.length(); j++) {
				char word = line.charAt(j);
				//System.out.println();
				if(word == '.'){
					g.setColor(Color.GRAY);
					g.fillRect(31 *j,31*i,height,width);
				}
				else if(word == '#'){
					g.setColor(Color.BLUE);
					g.fillRect(31 *j,31*i,height,width);
				}
				else if(word == 'A'){
					g.setColor(Color.GREEN);
					g.fillRect(31 *j,31*i,height,width);
				}
				else if(word == 'B'){
					g.setColor(Color.RED);
					g.fillRect(31 *j,31*i,height,width);
				}
			}
		}
	  }
	  
	  public void setLines(ArrayList<String> lines){
		  this.lines = lines;
	  }
	  
	  
	  
	}

	public class DrawRect {
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