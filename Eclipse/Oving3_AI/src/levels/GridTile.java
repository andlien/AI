package levels;

public class GridTile implements Comparable<GridTile> {

	private char symbol;
	private int h;
	private GridTile parent = null;
	private int currentG = 100;
	
	public int getH() {
		return h;
	}

	public void setH(int h) {
		this.h = h;
	}

	public GridTile( char symbol) {
		this.symbol = symbol;
	}
	
	public char getSymbol() {
		return symbol;
	}
	public void setSymbol(char symbol) {
		this.symbol = symbol;
	}

	@Override
	public int compareTo(GridTile o) {
		// TODO: Sjekk at denne blir rett mtp -1 
		return (h + currentG) - (o.getH() + o.getCurrentG());
	}

	public GridTile getParent() {
		return parent;
	}
	
	public void setParent(GridTile parent) {
		this.parent = parent;
	}
	
	public void setCurrentG(int g) {
		this.currentG = g;
	}
	
	public int getCurrentG() {
		return currentG;
	}
}
