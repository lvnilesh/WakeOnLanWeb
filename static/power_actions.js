function turnon() {
  fetch('/turnon')
      .then(response => response.text())
      // .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}


function fw() {
  fetch('/fw')
      .then(response => response.text())
      .catch(error => console.error('Error:', error));
}

function restart() {
  fetch('/restart')
      .then(response => response.text())
      // .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}

function shutdown() {
  fetch('/shutdown')
      .then(response => response.text())
      // .then(data => alert(data))
      .catch(error => console.error('Error:', error));
}