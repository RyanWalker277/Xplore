$(".option").click(function(){
    $(".option").removeClass("active");
    $(this).addClass("active");
    
 });

 // Function to toggle header menu in mobile view.
function toggleMenu(flag) {
    let value = document.getElementById("menu");
    if (flag) {
        value.classList.remove("hidden");
    } else {
        value.classList.add("hidden");
    }
}


//Scroll Js