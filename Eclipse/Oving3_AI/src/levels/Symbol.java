package levels;

import java.awt.Color;

public enum Symbol {
	NONE (Color.WHITE, 1),
	WALL (Color.GRAY, -1),
	CHCEKED (Color.GRAY.darker(), -1),
	CLOSED (Color.BLACK, -1),
	START (Color.GREEN, 1),
	END (Color.RED, 1),
	WATER (Color.BLUE, 100),
	MOUNTAINS (Color.GRAY, 50),
	FORESTS (Color.GREEN, 10),
	GRASSLANDS (Color.GREEN.brighter(), 5),
	ROADS (Color.ORANGE.darker(), 1),
	SHORTEST (Color.YELLOW, -1);
	
	private final Color color;
	private final int cost;
	
	private Symbol(Color color, int cost) {
		this.color = color;
		this.cost = cost;
	}
	
	public Color getColor() {
		return this.color;
	}
	
	public int getCost() {
		if (this.cost != -1)
			return this.cost;
		else
			throw new RuntimeException("WOOOOOOT!");
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
