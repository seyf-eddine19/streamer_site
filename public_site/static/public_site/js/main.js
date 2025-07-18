
function toggleMenu() {
  const menu = document.getElementById('nav-menu');
  menu.classList.toggle('show');
}

function toggleLangMenu() {
  const langMenu = document.getElementById('lang-menu');
  langMenu.classList.toggle('show');
  langMenu.classList.toggle('hide');
}

document.addEventListener('click', function (e) {
  const menu = document.getElementById('nav-menu');
  const langMenu = document.getElementById('lang-menu');
  const toggle = document.getElementById('nav-toggle');
  const langBtn = document.querySelector('.lang-btn');

  if (!menu.contains(e.target) && !toggle.contains(e.target)) {
    menu.classList.remove('show');
  }

  if (!langBtn.contains(e.target)) {
    langMenu.classList.add('hide');
    langMenu.classList.remove('show');
  }
});

function submitLangForm(lang) {
  document.getElementById('language-input').value = lang;
  document.getElementById('lang-form').submit();
}

// Swiper: Footer Photography Types
const footerSwiper = new Swiper(".footer-swiper", {
  loop: true,
  speed: 2000,
  autoplay: {
    delay: 0,
    disableOnInteraction: false,
  },
  slidesPerView: "auto",
  spaceBetween: 20,
  freeMode: true,
  grabCursor: true,
});
