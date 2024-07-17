document.addEventListener('DOMContentLoaded', () => {
    // Fade-in animation for elements with class .fade-in
    gsap.from(".fade-in", { opacity: 0, duration: 2, stagger: 1.5 });

    // Example animation for a specific element (adjust as needed)
    gsap.from(".fade-girl", { opacity: 0, x: 500, scale: 0.5, duration: 1.8 });


});
