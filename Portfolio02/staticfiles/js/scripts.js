// Function to add or remove the 'active-button' class
document.addEventListener("DOMContentLoaded", function() {
    toggleButtonColors();

    function toggleButtonColors() {
        const sections = document.querySelectorAll("section");
        const links = document.querySelectorAll("nav a");

        sections.forEach((section, index) => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= 50 && rect.bottom >= 50) {
                links[index].classList.add("active");
            } else {
                links[index].classList.remove("active");
            }
        });
    }
    // Listen for scroll events
    window.addEventListener("scroll", toggleButtonColors);
});
