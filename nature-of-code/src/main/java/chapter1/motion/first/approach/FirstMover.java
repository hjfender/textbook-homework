package chapter1.motion.first.approach;

import chapter1.Mover;
import processing.core.PApplet;
import processing.core.PVector;

public class FirstMover extends Mover {

	public FirstMover(PApplet p) {
		super(p);
		this.velocity = new PVector(parent.random(-2,2),parent.random(-2,2));
	}

	@Override
	public void update() {
		this.location.add(velocity);
	}

}
