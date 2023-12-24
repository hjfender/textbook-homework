package introduction.walk.right.tending;

import introduction.Walker;
import processing.core.PApplet;
import processing.core.PVector;

public class RightTendingWalker extends Walker {
	
	public RightTendingWalker(PApplet p) {
		super(p);
	}

	@Override
	public void step() {
		float r = parent.random(1);
		
		if (r < 0.4) {
			pos.x++;
		} else if (r < 0.6) {
			pos.x--;
		} else if (r < 0.8) {
			pos.y++;
		} else {
			pos.y--;
		}
		
		PVector step = new PVector((int) parent.random(3) - 1, (int) parent.random(3) - 1);
		
		pos.x += step.x;
		pos.y += step.y;
	}

}
