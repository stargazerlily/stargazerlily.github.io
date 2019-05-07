var descriptor = [
  "forest friend",
  "yasai",
  "social-media rejectionist",
  "herbivore",
  "little brown mushroom",
  "damned yellow composite"
]
function describeMe() {
  var randomNumber = Math.floor(Math.random() * (descriptor.length));
  document.getElementById("tDescriptor").innerHTML = descriptor[randomNumber];
}
