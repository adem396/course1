function menu(menu) {
  menu.preventDefault();
  a = document.getElementById("menu");
  if (a.style.display == "none" || a.style.display == "") {
    a.style.display == "block";
  } else {
    a.style.display == "";
  }
}
