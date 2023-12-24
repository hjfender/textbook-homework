package chapter1.motion.first.approach;

import chapter1.Mover;
import processing.core.PApplet;

public class Motion101 extends PApplet {

	Mover mover;
	
	public static void main(String[] args) {
		PApplet.main("chapter1.motion.first.approach.Motion101");
	}
	
	public void settings() {
		size(640, 360);
	}
	
	public void setup() {
		mover = new FirstMover(this);
	}
	
	public void draw() {
		background(255);
		
		mover.update();
		mover.checkEdges();
		mover.display();
	}
}
