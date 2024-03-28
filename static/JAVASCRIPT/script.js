const dropdown = document.querySelector(".dropdown");
const dropdownContent = document.querySelector(".dropdown-content");

// Toggle active class to show/hide dropdown content
dropdown.addEventListener("mouseover", () => {
  dropdownContent.classList.add("active");
});

dropdown.addEventListener("mouseleave", () => {
  dropdownContent.classList.remove("active");
});

// slide show
let slideIndex = 0;

function showSlides() {
  let slides = document.getElementsByClassName("mySlides");
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 5000);
}

showSlides();
