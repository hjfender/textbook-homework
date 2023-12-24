package chapter1.vector.bouncing.ball;

import processing.core.PApplet;
import processing.core.PVector;

public class BouncingBall extends PApplet {

	PVector location;
	PVector velocity;
	
	public static void main(String[] args) {
		PApplet.main("chapter1.vector.bouncing.ball.BouncingBall");
	}
	
	public void settings() {
		size(640, 360, P3D);
	}
	
	public void setup() {
		location = new PVector(100,100,100);
		velocity = new PVector(2.5f, 5, 0);
	}
	
	public void draw() {
		background(0);
		
		location.add(velocity);
		  if((location.x > width) || (location.x < 0)){
		    velocity.x = velocity.x * -1;
		  }
		  if((location.y > height) || location.y < 0){
		    velocity.y = velocity.y * -1;
		  }
		  
		  pushMatrix();
		  translate(location.x,location.y,location.y);
		  stroke(255);
		  fill(175);
		  sphere(16);
		  popMatrix();
	}
}
