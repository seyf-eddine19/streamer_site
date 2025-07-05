// FAQ Toggle
document.addEventListener("DOMContentLoaded", function () {
    const faqItems = document.querySelectorAll(".faq-item");
    faqItems.forEach(item => {
      const header = item.querySelector(".faq-header");
      const body = item.querySelector(".faq-body");
      const icon = item.querySelector(".faq-icon");
  
      header.addEventListener("click", () => {
        body.classList.toggle("faq-active");
  
        if (icon.classList.contains("bx-chevron-down")) {
          icon.classList.remove("bx-chevron-down");
          icon.classList.add("bx-chevron-up");
        } else {
          icon.classList.remove("bx-chevron-up");
          icon.classList.add("bx-chevron-down");
        }
      });
    });
  });
  