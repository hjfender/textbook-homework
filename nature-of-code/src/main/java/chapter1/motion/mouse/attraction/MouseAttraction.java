package chapter1.motion.mouse.attraction;

import chapter1.Mover;
import processing.core.PApplet;

public class MouseAttraction extends PApplet {

	Mover mover;
	
	public static void main(String[] args) {
		PApplet.main("chapter1.motion.mouse.attraction.MouseAttraction");
	}
	
	public void settings() {
		size(640,360);
	}
	
	public void setup() {
		mover = new MouseAttractedMover(this);
	}
	
	public void draw() {
		background(255);
		
		mover.update();
		mover.display();
	}
}
