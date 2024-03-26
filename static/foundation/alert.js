
function handleSweetAlert(){
    
    const contactForm = document.getElementById("contact-form");
    const sweetalertcontainer = document.querySelector(".sweet-alert");
    const sweetalert = document.querySelector(".alert");
    
    // Function to display the alert message
    function displayAlert(usersName) {
        const alertMessage = document.createElement("p");
        alertMessage.textContent = "Hello " + usersName + ". Thank you for contacting us.";
        sweetalert.appendChild(alertMessage);
        sweetalertcontainer.style.display = "block";
    
        // Set a timeout to hide the alert after 3 seconds (3000 milliseconds)
        setTimeout(() => {
            sweetalertcontainer.style.display = "none";
            localStorage.removeItem("usersName"); // Remove stored user's name from localStorage
        }, 5000);
    }
    
    // Event listener for form submission
    contactForm.addEventListener("submit", (event) => {
        const usersName = document.getElementById("userName").value;
        localStorage.setItem("usersName", usersName); // Store user's name in localStorage
    });
    
    // Event listener for window load
    window.addEventListener("load", () => {
        const usersName = localStorage.getItem("usersName");
        if (usersName) {
            displayAlert(usersName); // Call the displayAlert function with the stored user's name
        }
    });
    }




function handleScrollToTop(){
    window.addEventListener("scroll", () => {
        const windowHeight = window.innerHeight;
        const newHeight = windowHeight - 1;
    
        if (newHeight < windowHeight) {
            scrollToTopBtn.style.display = "block";
        } else {
            scrollToTopBtn.style.display = "none";
        }
        // Check if the scroll position is at the top of the page
        if (window.scrollY === 0) {
            scrollToTopBtn.style.display = "none"; // Set display to "none" when at the top
        }
    });
    // Function to scroll to the top of the page
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
        scrollToTopBtn.style.display = "none"; // Hide the button after initiating smooth scroll
    }
    const scrollToTopBtn = document.getElementById("scrollToTopBtn");
    
    // Event listener for button click
    scrollToTopBtn.addEventListener("click", scrollToTop);
    
}




handleScrollToTop()
handleSweetAlert()