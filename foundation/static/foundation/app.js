// Prevent default action for toggle links
const preventLi = document.querySelectorAll(".toggle");
preventLi.forEach((link) => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
    });
});
// Toggle sub-links visibility
const toggleLinks = document.querySelectorAll(".fa-plus");
toggleLinks.forEach((toggleLink) => {
    toggleLink.addEventListener("click", (e) => {
        // Get the parent <li> element of the clicked toggle link
        const parentListItem = toggleLink.closest("li");

        // Find the sub-links within the parent <li> element
        const subLinks = parentListItem.querySelector(".sub-links");

        // Toggle the visibility of the sub-links
        if (subLinks) {
            subLinks.classList.toggle("showSubLinks");

            // Rotate the toggle button
            toggleLink.classList.toggle("rotate");
        }
    });
});


document.addEventListener("DOMContentLoaded", function () {
    const photos = document.querySelectorAll('.photo img');
    const popUpImage = document.getElementById('popUpImage');
    const popUpContainer = document.querySelector('.gallery-pop-up-container');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');
    const removepopUpImage = document.getElementById("remove-popUp")
    const zoomButton = document.getElementById("zoomButton")
    let currentIndex = 0;

    // Function to display image in the pop-up container
    function displayImage(index) {
        popUpImage.src = photos[index].src;
        currentIndex = index;
    }

    // Event listener for clicking on a photo to show it in the pop-up container
    photos.forEach(function (photo, index) {
        photo.addEventListener('click', function () {
            displayImage(index);
            popUpContainer.style.display = 'block';
        });
    });

    // Event listeners for previous and next buttons
    prevButton.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + photos.length) % photos.length;
        displayImage(currentIndex);
    });

    nextButton.addEventListener('click', function () {
        currentIndex = (currentIndex + 1) % photos.length;
        displayImage(currentIndex);
    });
    
    zoomButton.addEventListener("click", () => {
        popUpImage.classList.toggle("zooms");
    });

    // Close pop-up container 
    removepopUpImage.addEventListener("click", () => {
        popUpContainer.style.display = "none";
        popUpImage.classList.remove("zooms"); // Remove zoom class when closing
    });

    
});




// This event listener manages the fixed navigation bar on scroll
window.addEventListener('scroll', function() {
    // Select the .second-navigation element
    const secondnavigation  = document.querySelectorAll(".second-navigation")

    // Loop through each .second-navigation element
    secondnavigation.forEach(function(secondnavigation){
        // Get the offset of the .second-navigation element
        const stickyNavBar = secondnavigation.offsetTop

        // Get the current scroll position
        const scrollTop = window.scrollY || document.documentElement.scrollTop
    
        // Add/remove 'fixed' class based on scroll position
        if(scrollTop > stickyNavBar){
            secondnavigation.classList.add("fixed")
        } else {
            secondnavigation.classList.remove("fixed")
        }
    })
});

// This block of code handles the navigation functionality
const navigationlinks = document.querySelector(".nav")
const removeNav = document.querySelector(".remove-nav")
const menuIcon = document.querySelector(".fa-bars")

// Event listener for the menu icon to toggle navigation links visibility
menuIcon.addEventListener("click",()=>{
    navigationlinks.classList.toggle("show")
})

// Event listener for the remove navigation button to toggle navigation links visibility
removeNav.addEventListener("click",()=>{
    navigationlinks.classList.toggle("show")
})

// This block of code manages the slide show functionality
const slides = document.querySelectorAll('.slide-show .slide');
let currentSlide = 0;

// Function to show a specific slide
function showSlide(index) {
    slides.forEach((slide, i) => {
        if (i === index) {
            slide.style.display = "block";
        } else {
            slide.style.display = "none";
        }
    });
}

// Function to show the next slide
function nextSlide() {
    currentSlide++;
    if (currentSlide >= slides.length) {
        currentSlide = 0;
    }
    showSlide(currentSlide);
}

// Function to show the previous slide
function prevSlide() {
    currentSlide--;
    if (currentSlide < 0) {
        currentSlide = slides.length - 1;
    }
    showSlide(currentSlide);
}

// Show the first slide initially
showSlide(currentSlide);

// Event listeners for the navigation buttons
document.querySelector(".prev").addEventListener("click", prevSlide);
document.querySelector(".next").addEventListener("click", nextSlide);
setInterval(nextSlide, 7000);

// This block of code handles the reveal animation for elements on scroll
window.addEventListener("scroll", () => {
    const targetElements = document.querySelectorAll(".element");

    targetElements.forEach(element => {
        const position = element.getBoundingClientRect();
        const threshold = window.innerHeight * 0.65;

        // If the element's position is within the threshold, reveal it and trigger animation
        if (position.top <= threshold) {
            element.classList.add("slides");
        }
    });
});







