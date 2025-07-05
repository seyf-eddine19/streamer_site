// Swiper: Games
const swiper = new Swiper(".gameSwiper", {
    slidesPerView: 3,
    centeredSlides: true,
    loop: true,
    grabCursor: true,
    spaceBetween: 30,
    breakpoints: {
      0: { spaceBetween: 10 },
      974: { spaceBetween: 30 }
    },
    on: {
      slideChange: function () {
        const activeSlide = this.slides[this.activeIndex];
        const gameName = activeSlide.getAttribute('data-name') || '';
        document.querySelector('.game-name').textContent = gameName;
      }
    }
  });
  
// Set initial game name
document.addEventListener("DOMContentLoaded", () => {
    const initial = document.querySelector('.swiper-slide-active');
    if (initial) {
      const name = initial.getAttribute('data-name');
      document.querySelector('#game-name').textContent = name;
    }
  });