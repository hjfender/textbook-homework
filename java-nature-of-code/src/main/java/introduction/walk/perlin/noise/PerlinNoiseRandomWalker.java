package introduction.walk.perlin.noise;

import introduction.Walker;
import processing.core.PApplet;
import processing.core.PVector;

public class PerlinNoiseRandomWalker extends Walker {

	PVector differential;
	
	public PerlinNoiseRandomWalker(PApplet p) {
		super(p);
		differential = new PVector(0,10000);
	}

	@Override
	public void display() {
		parent.background(255);
		parent.fill(0);
		parent.ellipse(pos.x, pos.y, 16, 16);
	}
	
	@Override
	public void step() {
		pos.x = PApplet.map(parent.noise(differential.x), 0, 1, 0, parent.width);
		pos.y = PApplet.map(parent.noise(differential.y), 0, 1, 0, parent.height);
		
		differential.x += 0.01;
		differential.y += 0.01;
	}

}
