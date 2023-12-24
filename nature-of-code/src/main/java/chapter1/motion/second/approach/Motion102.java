package chapter1.motion.second.approach;

import chapter1.Mover;
import processing.core.PApplet;

public class Motion102 extends PApplet {

	Mover mover;
	
	public static void main(String[] args) {
		PApplet.main("chapter1.motion.second.approach.Motion102");
	}
	
	public void settings() {
		size(640,360);
	}
	
	public void setup() {
		mover = new SecondMover(this);
	}
	
	public void draw() {
		background(255);
		
		mover.checkEdges();
		mover.update();
		mover.display();
	}
}
