const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

window.addEventListener('load', function(){
  if(sign_up_btn){
    container.classList.add("sign-up-mode");
  }
  else if(sign_up_btn){
    container.classList.remove("sign-up-mode");
  }
})

// sign_up_btn.addEventListener("click", () => {
//   container.classList.add("sign-up-mode");
// });

// sign_in_btn.addEventListener("click", () => {
//   container.classList.remove("sign-up-mode");
// });
