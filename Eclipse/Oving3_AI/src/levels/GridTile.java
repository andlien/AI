package levels;

public class GridTile implements Comparable<GridTile>{

	private char symbol;
	private int h;
	private GridTile parent = null;
	private int currentG = -1;
	
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
		int f1 = this.h, f2 = o.getH();
		GridTile t = this;
		while ((t = t.parent) != null) {
			f1++;
		}
		while ((o = o.parent) != null) {
			f2++;
		}
		return f1 - f2;
	}

	public GridTile getParent() {
		return parent;
	}
}
