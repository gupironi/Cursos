let xBolinha = 300
let yBolinha = 200
let diametro = 20

let velocXBolinha = 3.5
let velocYBolinha = 3.5

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(0);
  circle(xBolinha, yBolinha, diametro);
  xBolinha += velocXBolinha
  yBolinha += velocYBolinha
  
  if (xBolinha > width || xBolinha < 0){
    velocXBolinha *= -1;
  }
  
  if (yBolinha > height || yBolinha < 0)
    velocYBolinha *= -1
}