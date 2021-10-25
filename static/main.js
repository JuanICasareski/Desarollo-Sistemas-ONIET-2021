const nav_list = document.querySelectorAll('.nav-item');
const active_element = document.querySelector('.active');
const hamburger = document.querySelector('.hamburger');
const navbar = document.querySelector('.nav-list');

nav_list.forEach((item) => {
    item.addEventListener('mouseover', () => {
        active_element.classList.remove('active');
        item.classList.add('active');
    });
    item.addEventListener('mouseout', () => {
        item.classList.remove('active');
        active_element.classList.add('active');
    })
});

hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navbar.classList.toggle('menu-active');
    document.body.classList.toggle('disableScroll');
});