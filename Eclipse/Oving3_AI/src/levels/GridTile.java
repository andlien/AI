package levels;

public class GridTile implements Comparable<GridTile>{

	private char symbol;
	private float h;
	private GridTile parent = null;
	
	public float getH() {
		return h;
	}

	public void setH(float h) {
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
		int g1, g2 = 0;
		GridTile t = this;
		while ((t = t.parent) != null) {
			g1++;
		}
		while ((o = o.parent) != null) {
			g2++;
		}
		return g1 - g2;
	}
}
