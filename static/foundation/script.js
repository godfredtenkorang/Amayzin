


function handleCardSlider(){
  const sliders = document.querySelectorAll('.sliders');
const prevBtns = document.querySelectorAll('.prev-btn');
const nextBtns = document.querySelectorAll('.next-btn');

prevBtns.forEach(prevBtn => {
  prevBtn.addEventListener('click', () => {
    const slider = prevBtn.parentElement.querySelector('.sliders');
    const cardWidth = slider.querySelector('.card').offsetWidth;
    let counter = parseInt(slider.dataset.counter) || 0;
    counter = Math.max(counter - 2, 0);
    slider.style.transform = `translateX(${-counter * cardWidth}px)`;
    slider.dataset.counter = counter;
  });
});

nextBtns.forEach(nextBtn => {
  nextBtn.addEventListener('click', () => {
    const slider = nextBtn.parentElement.querySelector('.sliders');
    const cardWidth = slider.querySelector('.card').offsetWidth;
    let counter = parseInt(slider.dataset.counter) || 0;
    counter = (counter + 2) % (slider.children.length - 5); // Displaying 5 items
    slider.style.transform = `translateX(${-counter * cardWidth}px)`;
    slider.dataset.counter = counter;
  });
});
}

handleCardSlider()


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
