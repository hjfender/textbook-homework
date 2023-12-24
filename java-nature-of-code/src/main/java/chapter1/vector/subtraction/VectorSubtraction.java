package chapter1.vector.subtraction;

import processing.core.PApplet;
import processing.core.PVector;

public class VectorSubtraction extends PApplet {

	public static void main(String[] args) {
		PApplet.main("chapter1.vector.subtraction.VectorSubtraction");
	}
	
	public void settings() {
		size(640, 360);
	}
	
	public void setup() {
		
	}
	
	public void draw() {
		background(255);
		PVector mouse = new PVector(mouseX, mouseY);
		PVector center = new PVector(width/2, height/2);
		mouse.sub(center);
		translate(width/2, height/2);
		line(0, 0, mouse.x, mouse.y);
	}
}
