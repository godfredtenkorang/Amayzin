document.addEventListener("DOMContentLoaded", function() {
    const submissionAlert = document.querySelector(".submission-alert");
    const formSubmitted = localStorage.getItem("formSubmitted");

    if (formSubmitted) {
      submissionAlert.style.display = "block";
      setTimeout(() => {
        submissionAlert.style.display = "none";
        localStorage.removeItem("formSubmitted");
      }, 5000);
    }
  });

  const formPayment = document.getElementById("form-payment");

  formPayment.addEventListener("submit", (event) => {
    localStorage.setItem("formSubmitted", true);
  });