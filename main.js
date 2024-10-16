let menu = document.querySelectorAll('#menu-icon');
let navbar = document.querySelectorAll('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active')
}

window.onscroll  = () =>{
    menu.classList.remove('bx-x');
    navbar.classList.remove('active')
}
