package chapter2;

import processing.core.PApplet;
import processing.core.PVector;

public class Mover extends chapter1.Mover {

	protected float mass;
	
	public Mover(PApplet p) {
		super(p);
		mass = 1f;
	}

	public void update() {
	    velocity.add(acceleration);
	    location.add(velocity);
	    acceleration.mult(0);
	 }
	
	public void applyForce(PVector force) {
		PVector f = force.div(mass);
		this.acceleration.add(f);
	}
}
