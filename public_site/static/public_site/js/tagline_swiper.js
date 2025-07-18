// Swiper: tagline
const taglineSwiper = new Swiper(".tagline-swiper", {
  loop: true,
  speed: 3000,
  autoplay: {
    delay: 0,
    disableOnInteraction: false,
  },
  slidesPerView: "auto",
  freeMode: true,
  grabCursor: true,
  freeModeMomentum: false,
  allowTouchMove: false, 
  spaceBetween: 50,
});
