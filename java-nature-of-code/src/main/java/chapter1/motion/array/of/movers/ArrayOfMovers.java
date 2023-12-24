package chapter1.motion.array.of.movers;

import chapter1.Mover;
import chapter1.motion.mouse.attraction.MouseAttractedMover;
import chapter1.motion.third.approach.ThirdMover;
import processing.core.PApplet;

public class ArrayOfMovers extends PApplet {
	
	Mover[] movers = new Mover[20];
	
	public static void main(String[] args) {
		PApplet.main("chapter1.motion.array.of.movers.ArrayOfMovers");
	}
	
	public void settings() {
		size(640, 360);
	}
	
	public void setup() {
		background(255);
		
		for (int i = 0; i < movers.length; i++) {
			float r = random(1);
			if(r > 0.5) {
				movers[i] = new ThirdMover(this);
			} else {
				movers[i] = new MouseAttractedMover(this);
			}
		}
	}
	
	public void draw() {
		background(255);
		
		for(int i = 0; i < movers.length; i++){
		    movers[i].update();
		    movers[i].checkEdges();
		    movers[i].display();
		  }
	}
}
