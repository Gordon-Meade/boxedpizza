document.addEventListener("DOMContentLoaded", function() {
    // Select the element to fade in
    var element = document.querySelector('.fade-in-text p');

    // Set initial opacity
    element.style.opacity = 0;

    // Define the duration of the fade-in animation (in milliseconds)
    var duration = 5000; // 5 seconds

    // Calculate the interval for changing opacity gradually
    var interval = 1000 / 60; // 60 frames per second

    // Calculate the increment in opacity for each frame
    var increment = interval / duration;

    // Variable to store current opacity
    var opacity = 0;

    // Function to gradually increase opacity until 1 (fully visible)
    var fadeInInterval = setInterval(function() {
        opacity += increment;
        element.style.opacity = opacity;

        // Check if element is fully visible
        if (opacity >= 1) {
            clearInterval(fadeInInterval); // Stop the interval
        }
    }, interval);
});
