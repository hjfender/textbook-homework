package introduction.walk.mouse.tending;

import introduction.Walker;
import processing.core.PApplet;
import processing.core.PVector;

public class MouseTendingWalker extends Walker {

	public MouseTendingWalker(PApplet p) {
		super(p);
	}

	@Override
	public void step() {
		float r = parent.random(1);
		
		PVector mouse = new PVector(parent.mouseX, parent.mouseY);
		
		if(r < 0.5) {
			PVector diff = PVector.sub(mouse, pos);
			pos.add(diff.normalize());
		} else {
			int stepx = ((int) parent.random(3)) - 1;
			int stepy = ((int) parent.random(3)) - 1;
			pos.x += stepx;
			pos.y += stepy;
		}
	}

}
