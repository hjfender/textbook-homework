package introduction.walk.perlin.noise;

import introduction.Walker;
import processing.core.PApplet;

public class PerlinNoiseRandomWalk extends PApplet {

	Walker walker;
	
	public static void main(String[] args) {
		PApplet.main("introduction.walk.perlin.noise.PerlinNoiseRandomWalk");
	}
	
	public void settings() {
		size(640,360);
	}
	
	public void setup() {
		background(255);
		walker = new PerlinNoiseRandomWalker(this);
	}
	
	public void draw() {
		walker.step();
		walker.display();
	}
}
