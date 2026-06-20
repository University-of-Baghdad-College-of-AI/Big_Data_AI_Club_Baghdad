/* nav-toggle.js — add <script src="nav-toggle.js"></script> before </body> */
document.addEventListener('DOMContentLoaded', function () {

  // Hamburger toggle
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });
  }

  // Mobile: tap on Activities to expand dropdown inline
  const dropdowns = document.querySelectorAll('.dropdown');
  dropdowns.forEach(function (dd) {
    const btn = dd.querySelector('.dropbtn');
    if (btn) {
      btn.addEventListener('click', function (e) {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          dd.classList.toggle('open');
        }
      });
    }
  });

  // Close nav when a link is clicked (mobile)
  const navAnchors = document.querySelectorAll('.nav-links a');
  navAnchors.forEach(function (a) {
    a.addEventListener('click', function () {
      if (navLinks) navLinks.classList.remove('open');
    });
  });
});
