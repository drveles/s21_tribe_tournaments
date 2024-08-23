function toggleBlock(event) {
    var clickedElement = event.currentTarget;
    var nextElement = clickedElement.nextElementSibling;

    if (nextElement) {
        nextElement.classList.toggle("__hidden");
    }

    // var tribes = document.getElementsByClassName("tribe-info");

    // for (var i = 0; i < tribes.length; i++) {
    //     console.log(tribes[i])
    //     tribes[i].nextElementSibling.classList.add("__hidden");
    // }
}