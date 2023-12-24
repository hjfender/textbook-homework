package chapter1.motion.mouse.attraction;

import chapter1.Mover;
import processing.core.PApplet;
import processing.core.PVector;

public class MouseAttractedMover extends Mover {
	
	public MouseAttractedMover(PApplet p) {
		super(p);
	}

	@Override
	public void update() {
		PVector mouse = new PVector(parent.mouseX, parent.mouseY);
		PVector dir = PVector.sub(mouse, location);
		
		//dir.normalize();
	    //dir.mult(0.5f);
		
		dir.mult(0.001f);
		
		acceleration = dir;
	    
	    velocity.add(acceleration);
	    velocity.limit(topspeed);
	    location.add(velocity);
	    
	    checkEdges();
	}

}
