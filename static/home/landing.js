window.addEventListener('scroll', function () {
  const navbar = document.querySelector('nav');
  const logo = document.querySelector('#logo-main');
  
  if (window.scrollY > 40) {
    navbar.classList.add('nav-applied-40');
    logo.classList.add('add-class-logo-40');
  } else {
    navbar.classList.remove('nav-applied-40');
    logo.classList.remove('add-class-logo-40');
  }
});

/* Button Hover Animation */
const buttons = document.querySelectorAll('button');
buttons.forEach(button => {
  button.addEventListener('mouseenter', () => {
    button.style.transform = 'scale(1.05)'; /* Zoom effect */
  });
  
  button.addEventListener('mouseleave', () => {
    button.style.transform = 'scale(1)'; /* Reset zoom */
  });
});

/* Interactive Image Animation */
const images = document.querySelectorAll('.product_image_1');
images.forEach(image => {
  image.addEventListener('mouseenter', () => {
    image.style.transform = 'scale(1.05)'; /* Image zoom on hover */
    image.style.boxShadow = '0 12px 24px rgba(0, 0, 0, 0.5)'; /* Shadow depth */
  });
  
  image.addEventListener('mouseleave', () => {
    image.style.transform = 'scale(1)';
    image.style.boxShadow = 'none'; /* Reset shadow */
  });
});
const links = document.querySelectorAll('nav a[href^="#"]');

        links.forEach(link => {
            link.addEventListener('click', function(event) {
                event.preventDefault(); // Prevent default anchor click behavior
                const targetId = this.getAttribute('href'); // Get the target section ID
                const targetSection = document.querySelector(targetId); // Find the section

                // Smooth scroll to the section
                targetSection.scrollIntoView({
                    behavior: 'smooth', // Smooth scrolling
                    block: 'start', // Align to the start of the section
                });
            });
        });
