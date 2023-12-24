package introduction.distribution.gaussian;

import java.util.Random;

import processing.core.PApplet;

public class GaussianDistribution extends PApplet {

	Random generator;
	
	public static void main(String[] args) {
		PApplet.main("introduction.distribution.gaussian.GaussianDistribution");
	}
	
	public void settings() {
		size(640, 360);
	}
	
	public void setup() {
		generator = new Random();
		background(255);
	}
	
	public void draw() {
		float num = (float) generator.nextGaussian();
		float sd = 60;
		float mean = 320;
		
		float x = sd * num + mean;
		
		noStroke();
		fill(0,10);
		ellipse(x,100,16,16);
	}
}
