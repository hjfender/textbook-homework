package chapter2.balloon;

import chapter2.Mover;
import processing.core.PApplet;
import processing.core.PVector;

public class Balloon extends Mover {

	public Balloon(PApplet p) {
		super(p);
	}
	
	public void applyForce(PVector force) {
		this.acceleration.add(force);
	}

	@Override
	public void checkEdges() {
		if (location.x > parent.width) {
			this.location.x = 0;
		} else if (location.x < 0) {
			this.location.x = parent.width;
		}
		
		if (location.y > parent.height) {
			this.location.y = 0;
		} else if (location.y < 0) {
			this.applyForce(new PVector(0, 2));
		}
	}
}
