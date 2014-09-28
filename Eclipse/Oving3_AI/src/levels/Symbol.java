package levels;

import java.awt.Color;

public enum Symbol {
	NONE (Color.WHITE, 1,false),
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
	
	private final Color color;
	private final int cost;
	private final boolean small;
	
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
			throw new RuntimeException("WOOT");
		}
	}
}
