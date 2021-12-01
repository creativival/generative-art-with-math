import terrapin.*;

Terrapin t;
int x = 1;

void setup() {
  // create a blank window to draw on
  size(400,400);
  background(0);

  // create Terrapin
  t = new Terrapin(this);

  // set the Terrapin's pen color to an r,g,b value
  t.setPenColor(0, 0, 255);
}

// move the Terrapin forward - use the x value for the distance
// the movements in the draw method will be repeated
void draw() {
  t.forward(x);
  t.right(50);
  
  // increase x by two
  x = x + 2;
}


