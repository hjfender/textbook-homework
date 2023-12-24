package chapter1;

import processing.core.PApplet;
import processing.core.PVector;

public abstract class Mover {

	protected PApplet parent;
	protected PVector location;
	protected PVector velocity;
	protected PVector acceleration;
	protected float topspeed;
	
	public Mover(PApplet p) {
		this.parent = p;
		this.location = new PVector(parent.random(parent.width), parent.random(parent.height));
		this.velocity = new PVector(0,0);
		this.acceleration = new PVector(-0.001f, 0.01f);
		this.topspeed = 10;
	}
	
	public abstract void update();
	
	public void display() {
		parent.stroke(0);
		parent.fill(175);
		parent.ellipse(location.x, location.y, 16, 16);
	}
	
	public void checkEdges() {
		if (location.x > parent.width) {
			this.location.x = 0;
		} else if (location.x < 0) {
			this.location.x = parent.width;
		}
		
		if (location.y > parent.height) {
			this.location.y = 0;
		} else if (location.y < 0) {
			this.location.y = parent.height;
		}
	}
}
