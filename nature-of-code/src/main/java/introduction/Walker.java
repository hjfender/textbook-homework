package introduction;

import processing.core.PApplet;
import processing.core.PVector;

public abstract class Walker {

	protected PVector pos;
	protected PApplet parent;
	
	public Walker(PApplet p) {
		parent = p;
		pos = new PVector(parent.width/2, parent.height/2);
	}
	
	public void display() {
		parent.stroke(0);
		parent.point(pos.x, pos.y);
	}
	
	public abstract void step();
	
}
