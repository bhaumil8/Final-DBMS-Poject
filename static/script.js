let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

menu.onclick = () => {
	menu.classList.toggle('fa-times');
	navbar.classList.toggle('active');
}

window.onscroll = () => {
	menu.classList.remove('fa-times');
	navbar.classList.remove('active');
}

// Toggle navbar starts 

document.querySelector('#dish1').classList.remove('active2');
document.querySelector('#menu1').classList.remove('active4');
document.querySelector('#log1').classList.remove('active7');


document.querySelector('#dish1').onclick = () => {
	document.querySelector('#dish1').classList.toggle('active2');
	document.querySelector('#home1').classList.remove('active1');
	document.querySelector('#menu1').classList.remove('active4');
	document.querySelector('#log1').classList.remove('active7');
}
document.querySelector('#home1').onclick = () => {
	document.querySelector('#dish1').classList.remove('active2');
	document.querySelector('#home1').classList.toggle('active1');
	document.querySelector('#menu1').classList.remove('active4');
	document.querySelector('#log1').classList.remove('active7');
}

// toggle navbar ends

document.querySelector('#search-icon').onclick = () => {
	document.querySelector('#search-form').classList.toggle('active');
}

document.querySelector('#close').onclick = () => {
	document.querySelector('#search-form').classList.remove('active');
}

var swiper = new Swiper(".home-slider", {
	spaceBetween: 30,
	centeredSlides: true,
	autoplay:
	{
		delay: 4000,
		displayOnInteraction: false,
	},
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
	},
	loop: true,
});

function butn() {

	document.getElementById('activebtn').innerHTML = "- 1 +";
	document.getElementById('activebtn').style.background = "#27ae60";
	document.getElementById('activebtn').style.letterSpacing = "1rem";
	document.getElementById('activebtn').style.fontSize = "1.8rem";
}

function addToCart() {
	document.getElementById('btn').innerHTML = "- 1 +";
	document.getElementById('btn').style.background = "#192a56";
}