package chapter1.vector.magnitude;

import processing.core.PApplet;
import processing.core.PVector;

public class VectorMagnitude extends PApplet {

	public static void main(String[] args) {
		PApplet.main("chapter1.vector.magnitude.VectorMagnitude");
	}
	
	public void settings() {
		size(640, 640);
	}
	
	public void setup() {
		
	}
	
	public void draw() {
		background(255);
		stroke(255);
		fill(200);
		ellipse(width/2, height/2, 640, 640);
		stroke(0);
		
		PVector mouse = new PVector(mouseX, mouseY);
		PVector center = new PVector(width/2, height/2);
		mouse.sub(center);
		
		float m = 2 * mouse.mag();
		fill(0);
		rect(0, 0, m, 10);
		
		translate(width/2, height/2);
		line(0,0,mouse.x, mouse.y);
	}
}
