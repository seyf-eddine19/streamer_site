// Swiper: Clients (Marquee)
const clientSwiper = new Swiper(".client-swiper", {
    loop: true,
    speed: 2500,
    autoplay: {
      delay: 0,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    spaceBetween: 40,
    freeMode: true,
    grabCursor: true,
    breakpoints: {
      320: { slidesPerView: 2 },
      640: { slidesPerView: 3 },
      768: { slidesPerView: 4 },
      1024: { slidesPerView: 5 },
    }
  });
  