document.addEventListener('DOMContentLoaded', function() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    item.querySelector('.faq-question').addEventListener('click', function() {
      const wasActive = item.classList.contains('active');
      
      // Close all items
      faqItems.forEach(i => i.classList.remove('active'));
      
      // If the clicked item was not active, open it
      if (!wasActive) {
        item.classList.add('active');
      }
    });
  });
});

document.querySelectorAll('#callback').forEach(
  item => item.addEventListener('click', function() {
    var modal = document.querySelector(".popup1");
    var overlay = document.querySelector(".overlay");
    modal.style = "display: flex; visibility:visible;";
    overlay.style = "display: flex; opacity: 1; visibility: visible;";
  })
);


var button_open = document.querySelector("#callback");
button_open.addEventListener("click", function() {
  var modal = document.querySelector(".popup1");
  var overlay = document.querySelector(".overlay");
  modal.style = "display: flex; visibility:visible;";
  overlay.style = "display: flex; opacity: 1; visibility: visible;";
  
});


var button_close = document.querySelector(".close1");
button_close.addEventListener("click", function() {
  var modal = document.querySelector(".popup1");
  var overlay1 = document.querySelector(".overlay");
  modal.style = "";
  overlay1.style = "";
  console.log("Кнопка нажата.");
});

var button = document.querySelector(".overlay");
button.addEventListener("click", function() {
  var modal = document.querySelector(".popup1");
  var overlay1 = document.querySelector(".overlay");
  modal.style = "";
  overlay1.style = "";
  console.log("Кнопка нажата.");
});




  var splide = new Splide( '.splide', {
    type   : 'loop',
    padding: '5rem',
    label  : 'My Gallery',
  } );
  
  splide.mount();


  /* Установите ширину боковой панели на 250 пикселей (показать его) */
function openNav() {
  console.log(1)
  document.getElementById("mySidepanel").style.width = "250px";
}

/* Установите ширину боковой панели в 0 (скройте ее) */
function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
}




