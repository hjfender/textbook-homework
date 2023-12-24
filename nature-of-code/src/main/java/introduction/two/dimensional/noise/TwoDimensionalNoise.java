package introduction.two.dimensional.noise;

import processing.core.PApplet;

public class TwoDimensionalNoise extends PApplet {

	float t;
	
	public static void main(String[] args) {
		PApplet.main("introduction.two.dimensional.noise.TwoDimensionalNoise");
	}
	
	public void settings() {
		size(1000,600);
	}
	
	public void setup() {
		t = 0.0f;
		noiseDetail(2);
	}
	
	public void draw() {
		loadPixels();
		float xoff = 0.0f + t;
		for (int x = 0; x < width; x++) {
			float yoff = 0.0f + t;
			for (int y = 0; y < height; y++) {
				//float birght = random(255);
				float bright = map(noise(xoff,yoff),0,1,0,255);
				pixels[x+y*width] = color(1/bright,1/bright,bright);
				yoff += 0.01;
			}
			xoff += 0.01;
		}
		updatePixels();
		t += 0.05;
	}
}
