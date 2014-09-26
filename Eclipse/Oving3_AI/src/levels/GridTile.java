package levels;

public class GridTile {

	private char symbol;
	private float h;
	
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
}
