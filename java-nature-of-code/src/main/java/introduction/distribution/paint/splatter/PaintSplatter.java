package introduction.distribution.paint.splatter;

import java.util.Random;

import processing.core.PApplet;
import processing.core.PVector;

public class PaintSplatter extends PApplet {

	private Random generator;
	private final PVector sd = new PVector(90,90);
	private final PVector mean = new PVector(395, 450);
	private float size_sd = 3;
	private float size_mean = 20;
	
	public static void main(String[] args) {
		PApplet.main("introduction.distribution.paint.splatter.PaintSplatter");
	}
	
	public void settings() {
		size(640,640);
	}
	
	public void setup() {
		generator = new Random();
		background(255);
	}
	
	public void draw() {
		float x = (float) generator.nextGaussian();
		x = sd.x * x + mean.x;
		float y = (float) generator.nextGaussian();
		y = sd.y * y + mean.y;
		float w = (float) generator.nextGaussian();
		w = size_sd * w + size_mean;
		float h = (float) generator.nextGaussian();
		h = size_sd * h + size_mean;
		
		float clr = (float) generator.nextGaussian();
		clr = 32 * clr + 32;
		
		float opac = (float) generator.nextGaussian();
		opac = 10 * opac + 80;
		
		noStroke();
		fill(clr, opac);
		ellipse(x,y,w,h);
	}
}
