import terrapin.*;

Terrapin t;

void setup() {
  // create a blank window to draw on
  size(400,400);
  background(0);

  // create Terrapin
  t = new Terrapin(this);

  // set the Terrapin's pen color to an r,g,b value
  t.setPenColor(0, 0, 255);
}

// move the Terrapin forward and turn
// the movements in the draw method will be repeated
void draw() {
  t.forward(100);
  t.right(85);
}


