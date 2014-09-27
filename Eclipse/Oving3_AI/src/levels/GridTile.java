package levels;

import javax.management.RuntimeErrorException;

public class GridTile implements Comparable<GridTile> {

	private Symbol symbol;
	private int h;
	private GridTile parent = null;
	private int currentG = Integer.MAX_VALUE;
	
	public int getH() {
		return h;
	}

	public void setH(int h) {
		this.h = h;
	}
	
	public GridTile(Symbol sym) {
		this.symbol = sym;
	}

	public GridTile( char symbol) {
		this.symbol = Symbol.getSymByChar(symbol);
	}
	
	public Symbol getSymbol() {
		return symbol;
	}
	public void setSymbol(Symbol symbol) {
		this.symbol = symbol;
	}

	@Override
	public int compareTo(GridTile o) {
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
