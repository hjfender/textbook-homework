package introduction.walk.gaussian;

import java.util.Random;

import introduction.Walker;
import processing.core.PApplet;

public class GaussianRandomWalker extends Walker {
	
	Random generator;
	
	GaussianRandomWalker(PApplet p) {
		super(p);
		generator = new Random();
	}
	
	public void step() {
		double stepx = generator.nextGaussian();
		double stepy = generator.nextGaussian();
		
		pos.x += stepx;
		pos.y += stepy;
	}
}
