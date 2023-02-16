const buttons = document.getElementsByName('keySig');

buttons.forEach(button => {
  button.addEventListener('click', handleClick, false);
});

function handleClick() {
  alert(this.textContent);
}