package chapter1.motion.second.approach;

import chapter1.Mover;
import processing.core.PApplet;

public class SecondMover extends Mover {

	public SecondMover(PApplet p) {
		super(p);
	}

	@Override
	public void update() {
		velocity.add(acceleration);
		velocity.limit(topspeed);
		location.add(velocity);
	}

}
