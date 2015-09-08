package levels;

import java.awt.Color;

//The enum-class used to save the symbol and the weight for each of tiles
//The color of the tile is also saved here
public enum Symbol {
	// Tilecolor, weight, rectangle size
	//
	NONE (new  Color(184,184,184,250), 1,false),
	WALL (Color.GRAY, -1,false),
	CHCEKED (Color.GRAY.darker(), -1,true),
	CLOSED (Color.BLACK, -1,true),
	START (Color.ORANGE, 1,false),
	END (Color.RED, 1,false),
	WATER (Color.BLUE, 100,false),
	MOUNTAINS (Color.GRAY, 50,false),
	FORESTS (new Color(68,94,26,250), 10,false),
	GRASSLANDS (Color.GREEN.brighter(), 5,false),
	ROADS (Color.ORANGE.darker(), 1,false),
	SHORTEST (Color.YELLOW, -1,true);
	
	private final Color color;// Color of the tile
	
	private final int cost; // Weight of the tile. The cost of tiles with cost = -1 are never used as they are either ignored, i.e walls, 
							// or always drawed over other tiles, i.e CHCEKED, CLOSED
	
	private final boolean small; //Size of tile when the board is drawn. 
	//Tiles like CLOSED and SHORTEST are always drawn on top of other tiles and are therefore small
	// 
	
	private Symbol(Color color, int cost, boolean small) {
		this.color = color;
		this.cost = cost;
		this.small = small;
	}
	
	public Color getColor() {
		return this.color;
	}
	
	public boolean isSmall() {
		return small;
	}

	public int getCost() {
		return this.cost;

	}
	
	public static Symbol getSymByChar(char c) {
		switch (c) {
		case '#':
			return WALL;
		case '.':
			return NONE;
		case 'A':
			return START;
		case 'B':
			return END;
 		case 'w':
			return WATER;
 		case 'm':
 			return MOUNTAINS;
 		case 'f':
 			return FORESTS;
 		case 'g':
 			return GRASSLANDS;
 		case 'r':
 			return ROADS;

		default:
			throw new RuntimeException("ERROR: Symbol not found");
		}
	}
}
