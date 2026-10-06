// Portfolio JavaScript will be added as sections are built.
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-links a");

function updateActiveNav() {
    let currentSection = "home";

    sections.forEach((section) => {
        const sectionTop = section.offsetTop - 180;
        const sectionHeight = section.offsetHeight;

        if (
            window.scrollY >= sectionTop &&
            window.scrollY < sectionTop + sectionHeight
        ) {
            currentSection = section.getAttribute("id");
        }
    });

    navLinks.forEach((link) => {
        link.classList.remove("active");

        if (link.getAttribute("href") === `#${currentSection}`) {
            link.classList.add("active");
        }
    });
}

window.addEventListener("scroll", updateActiveNav);
window.addEventListener("load", updateActiveNav);

document.addEventListener("DOMContentLoaded", function () {

    const menuBtn = document.querySelector(".menu-btn");
    const navLinks = document.querySelector(".nav-links");

    if (!menuBtn || !navLinks) {
        console.log("Menu elements not found");
        return;
    }

    menuBtn.addEventListener("click", function () {

        navLinks.classList.toggle("active");

        if (navLinks.classList.contains("active")) {
            menuBtn.innerHTML = "✕";
            menuBtn.setAttribute("aria-expanded", "true");
        } else {
            menuBtn.innerHTML = "☰";
            menuBtn.setAttribute("aria-expanded", "false");
        }

    });

    navLinks.querySelectorAll("a").forEach(function (link) {

        link.addEventListener("click", function () {

            navLinks.classList.remove("active");

            menuBtn.innerHTML = "☰";
            menuBtn.setAttribute("aria-expanded", "false");

        });

    });

});