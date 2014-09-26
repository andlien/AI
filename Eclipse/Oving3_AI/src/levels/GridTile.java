package levels;

public class GridTile {
	private int xCord;
	private int ycord;
	private char symbol;
	
	public GridTile(int xCord, int ycord, char symbol) {
		super();
		this.xCord = xCord;
		this.ycord = ycord;
		this.symbol = symbol;
	}
	
	public int getxCord() {
		return xCord;
	}
	public void setxCord(int xCord) {
		this.xCord = xCord;
	}
	public int getYcord() {
		return ycord;
	}
	public void setYcord(int ycord) {
		this.ycord = ycord;
	}
	public char getSymbol() {
		return symbol;
	}
	public void setSymbol(char symbol) {
		this.symbol = symbol;
	}
}
