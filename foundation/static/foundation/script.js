




const slider = document.querySelector('.sliders');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

let counter = 0;
const cardWidth = document.querySelector('.card').offsetWidth;

prevBtn.addEventListener('click', () => {
  counter = Math.max(counter - 2, 0);
  slide();
});

nextBtn.addEventListener('click', () => {
  counter = (counter + 2) % (slider.children.length - 3); // Displaying 5 items
  slide();
});

function slide() {
  if (counter < 0) {
    counter = slider.children.length - 3; // Displaying 3 items
  } else if (counter > slider.children.length - 3) { // Displaying 5 items
    counter = 0;
  }
  slider.style.transform = `translateX(${-counter * cardWidth}px)`;
}


//  pop up
function showImage(img){
    const popupImg = document.getElementById("pop-up-img")
    popupImg.src = img.src

    const popupImage = document.getElementById("popupImage")
    popupImage.style.display="flex"
}

// hidePopup()
function hidePopup(){
    const popupImage = document.getElementById("popupImage")
    popupImage.style.display="none" 
}
