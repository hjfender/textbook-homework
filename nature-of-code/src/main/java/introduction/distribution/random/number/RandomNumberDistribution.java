package introduction.distribution.random.number;

import processing.core.PApplet;

public class RandomNumberDistribution extends PApplet {

	int[] randomCounts;
	
	public static void main(String[] args) {
		PApplet.main("introduction.distribution.random.number.RandomNumberDistribution");
	}
	
	public void settings() {
		size(640, 240);
	}
	
	public void setup() {
		randomCounts = new int[20];
	}
	
	public void draw() {
		background(255);
		int index = (int) random(randomCounts.length);
		randomCounts[index]++;
		
		stroke(0);
		fill(175);
		int w = width / randomCounts.length;
		for(int x = 0; x < randomCounts.length; x++) {
			rect(x*w, height-randomCounts[x], w-1, randomCounts[x]);
		}
	}
}
