package chapter1.motion.third.approach;

import chapter1.Mover;
import processing.core.PApplet;
import processing.core.PVector;

public class ThirdMover extends Mover {

	public ThirdMover(PApplet p) {
		super(p);
	}

	@Override
	public void update() {
		this.acceleration = PVector.random2D();
		
		this.velocity.add(acceleration);
		this.velocity.limit(topspeed);
		this.location.add(velocity);
	}

}
