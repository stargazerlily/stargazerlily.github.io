const button = document.getElementById("theme-toggle")
button.addEventListener('click', themeToggle);

localStorage.setItem("theme", "light");

var theme = localStorage.getItem("theme");

function darkTheme() {
  document.documentElement.style.setProperty('--lpadgreen', '#2f452f');
  document.documentElement.style.setProperty('--hoverTColor', '#e9381b');
  document.documentElement.style.setProperty('--froggygreen', '#00cd6f');
  document.body.style.backgroundImage = "url('img/WaterTileOcean.gif')";
  localStorage.setItem("theme", "dark");
  button.style.backgroundImage = 'url(img/daymode.png)';
}

function lightTheme() {
  document.documentElement.style.setProperty('--lpadgreen', '#00cd6f');
  document.documentElement.style.setProperty('--hoverTColor', '#ff9c8c');
  document.documentElement.style.setProperty('--froggygreen', '#006400');
  document.body.style.backgroundImage = "url('img/Ocean_edit.gif')";
  localStorage.setItem("theme", "light");
  button.style.backgroundImage = 'url(img/nightmode.png)';
}

function themeToggle() {
  var theme = localStorage.getItem("theme");
  if (theme == 'light') {
    darkTheme()
  }
  else if (theme == 'dark') {
    lightTheme()
  }
  else {
    lightTheme()
  }
}
