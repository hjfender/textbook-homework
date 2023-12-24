package chapter2.balloon;

import processing.core.PApplet;
import processing.core.PVector;

public class HotAirBalloon extends PApplet {

	Balloon balloon;
	PVector risingHeat = new PVector(0,-0.1f);
	PVector rightWind = new PVector(-0.1f,0);
	PVector leftWind = new PVector(0.1f,0);
	PVector perlinWind = new PVector(0,0);
	PVector perlinDifferential = new PVector(0,10000);;
	
	public static void main(String[] args) {
		PApplet.main("chapter2.balloon.HotAirBalloon");
	}
	
	public void settings() {
		size(640,360);
	}
	
	public void setup() {
		balloon = new Balloon(this);
	}
	
	public void draw() {
		background(255);
		
		balloon.applyForce(risingHeat);
		
		// Mouse Press controlled wind
//		if(mousePressed && mouseX <= 320) {
//			balloon.applyForce(leftWind);
//		} else if (mousePressed) {
//			balloon.applyForce(rightWind);
//		}
		
		//Perlin noise varying wind
		perlinWind.x = PApplet.map(noise(perlinDifferential.x), 0, 1, -0.1f, 0.1f);
		perlinWind.y = PApplet.map(noise(perlinDifferential.x), 0, 1, -0.1f, 0.1f);
		perlinDifferential.x += 0.01;
		perlinDifferential.y += 0.01;
		balloon.applyForce(perlinWind);
		
		balloon.checkEdges();
		balloon.update();
		balloon.display();
	}
}
