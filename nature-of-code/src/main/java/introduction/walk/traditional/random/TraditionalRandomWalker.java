package introduction.walk.traditional.random;

import introduction.Walker;
import processing.core.PApplet;

public class TraditionalRandomWalker extends Walker {

	public TraditionalRandomWalker(PApplet p) {
		super(p);
	}

	@Override
	public void step() {
		pos.x += (int) parent.random(3) - 1;
		pos.y += (int) parent.random(3) - 1;
	}

}
