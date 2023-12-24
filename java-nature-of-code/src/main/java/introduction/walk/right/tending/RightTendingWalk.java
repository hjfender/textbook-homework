package introduction.walk.right.tending;

import introduction.Walker;
import processing.core.PApplet;

public class RightTendingWalk extends PApplet {

	Walker walker;
	
	public static void main(String[] args) {
		PApplet.main("introduction.walk.right.tending.RightTendingWalk");
	}
	
	public void settings() {
		size(640, 360);
	}
	
	public void setup() {
		background(255);
		walker = new RightTendingWalker(this);
	}
	
	public void draw() {
		walker.step();
		walker.display();
	}
}
