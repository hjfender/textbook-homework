package introduction.walk.mouse.tending;

import introduction.Walker;
import processing.core.PApplet;

public class MouseTendingWalk extends PApplet {

	Walker walker;
	
	public static void main(String[] args) {
		PApplet.main("introduction.walk.mouse.tending.MouseTendingWalk");
	}
	
	public void settings() {
		size(640, 360);
	}
	
	public void setup() {
		background(255);
		walker = new MouseTendingWalker(this);
	}
	
	public void draw() {
		walker.step();
		walker.display();
	}
}
