document.addEventListener("DOMContentLoaded", function() {
    const dropdownButton = document.getElementById("dropdownButton");
    const dropdownMenu = document.getElementById("dropdownMenu");

    dropdownButton.addEventListener("click", function() {
        dropdownMenu.classList.toggle("hidden");
    });

    document.addEventListener("DOMContentLoaded", function(e) {
        if (!dropdownButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
            dropdownMenu.classList.add("hidden");
        }
    });

});


document.addEventListener("DOMContentLoaded", function() {
    const dropdownButton1 = document.getElementById("dropdownButton1");
    const dropdownMenu1 = document.getElementById("dropdownMenu1");

    dropdownButton1.addEventListener("click", function() {
        dropdownMenu1.classList.toggle("hidden");
    });

    document.addEventListener("DOMContentLoaded", function(e) {
        if (!dropdownButton1.contains(e.target) && !dropdownMenu1.contains(e.target)) {
            dropdownMenu1.classList.add("hidden");
        }
    });

});
