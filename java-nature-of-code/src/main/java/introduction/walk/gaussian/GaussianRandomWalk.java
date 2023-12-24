package introduction.walk.gaussian;

import introduction.Walker;
import processing.core.PApplet;

public class GaussianRandomWalk extends PApplet {

	Walker walker;
	
	public static void main(String[] args) {
		PApplet.main("introduction.walk.gaussian.GaussianRandomWalk");
	}
	
	public void settings() {
		size(640,360);
	}
		
	public void setup() {
		background(255);
		walker = new GaussianRandomWalker(this);
	}
	
	public void draw() {
		walker.step();
		walker.display();
	}
}
