import terrapin.*;

// create a blank window to draw on
size(400,400);
background(0);

// create Terrapin
Terrapin t = new Terrapin(this);

// set the Terrapin's pen color to an r,g,b value
t.setPenColor(255, 0, 0);

// move the Terrapin to draw a square
t.forward(100);
t.right(90);
t.forward(100);
t.right(90);
t.forward(100);
t.right(90);
t.forward(100);

