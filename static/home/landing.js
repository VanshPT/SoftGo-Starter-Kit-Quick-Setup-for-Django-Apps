window.addEventListener('scroll', function () {
    const navbar = document.querySelector('nav');
    const logo = document.querySelector('#logo-main')
  
    if (window.scrollY > 40) {
      navbar.classList.add('nav-applied-40');
      logo.classList.add('add-class-logo-40')  
    } else {
      navbar.classList.remove('nav-applied-40');
      logo.classList.remove('add-class-logo-40')   
    }
  });
  