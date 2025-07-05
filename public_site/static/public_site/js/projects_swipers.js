
// Swipers: Projects
document.querySelectorAll('.projectSwiper').forEach((el, index) => {
    new Swiper(el, {
      slidesPerView: 3,
      slidesPerGroup: 3,
      loop: true,
      grabCursor: true,
      spaceBetween: 30,
      centeredSlides: false,
      navigation: {
        nextEl: document.querySelectorAll(".project-button-next")[index],
        prevEl: document.querySelectorAll(".project-button-prev")[index],
      },
      breakpoints: {
        0: { slidesPerView: 1, slidesPerGroup: 1 },
        768: { slidesPerView: 2, slidesPerGroup: 2 },
        1024: { slidesPerView: 3, slidesPerGroup: 3 },
      }
    });
});