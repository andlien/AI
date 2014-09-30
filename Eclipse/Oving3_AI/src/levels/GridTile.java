package levels;

import javax.management.RuntimeErrorException;

public class GridTile implements Comparable<GridTile> {

	private Symbol symbol;
	private Symbol oldSymbol;
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
	
	public Symbol getOldSymbol() {
		return oldSymbol;
	}
	
	public void setSymbol(Symbol symbol) {
		if(oldSymbol == null) oldSymbol = this.symbol;
		this.symbol = symbol;
	}
	
	public int getSymbolCost(){
		int cost = symbol.getCost();
		if(cost != -1) return cost;
		return oldSymbol.getCost();
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
