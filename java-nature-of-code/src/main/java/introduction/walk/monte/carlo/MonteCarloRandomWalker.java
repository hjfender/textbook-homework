package introduction.walk.monte.carlo;

import introduction.Walker;
import processing.core.PApplet;

public class MonteCarloRandomWalker extends Walker {
	
	public MonteCarloRandomWalker(PApplet p) {
		super(p);
	}
	
	public void step() {
		float r = generateFloat();
		
		float stepx = parent.random(-r,r);
		float stepy = parent.random(-r,r);
		
		pos.x += stepx;
	    pos.y += stepy;
	}
	
	private float generateFloat() {
		while(true) {
			float r1 = parent.random(1);
			float probability = r1;
			float r2 = parent.random(1);
			if(r2 < probability) {
				return r1;
			}
		}
	}

}
