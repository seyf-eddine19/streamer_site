// Swiper: Testimonials
const testimonialSwiper = new Swiper(".testimonial-swiper", {
  slidesPerView: 1,
  slidesPerGroup: 1,
  spaceBetween: 30,
  grabCursor: true,
  centeredSlides: false,
  loop: true,
  navigation: {
    nextEl: ".testimonial-button-next",
    prevEl: ".testimonial-button-prev",
  },
  breakpoints: {
    768: {
      slidesPerView: 2,
      slidesPerGroup: 2,
    },
    1024: {
      slidesPerView: 3,
      slidesPerGroup: 3,
    }
  }
});
