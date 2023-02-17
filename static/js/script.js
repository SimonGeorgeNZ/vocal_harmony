const buttons = document.getElementsByName('keySig');

buttons.forEach(button => {
  button.addEventListener('click', handleClick, false);
});


function handleClick() {
  const key_Disp = document.createElement("p");
  key_Disp.id = this.getAttribute('value');
  key_Disp.setAttribute('name', 'keyDisp');
  document.getElementById('keyIs').appendChild(key_Disp);
  key_Disp.textContent = "Something"
  console.log(key_Disp.id)
}
