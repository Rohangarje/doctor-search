function searchDoctors() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let cards = document.getElementsByClassName("card");

    for (let i = 0; i < cards.length; i++) {
        let text = cards[i].innerText.toLowerCase();
        cards[i].style.display = text.includes(input) ? "" : "none";
    }
}

/* Page load animation */
window.onload = () => {
    document.body.style.opacity = 0;
    setTimeout(() => {
        document.body.style.transition = "1s";
        document.body.style.opacity = 1;
    }, 100);
};

// Show doctor details in a modal or alert (implement modal as needed)
function showDoctor(name, specialization, services, location, about, rating) {
    // Example: show details in an alert (replace with modal logic as needed)
    alert(
        `Doctor: ${name}\nSpecialization: ${specialization}\nServices: ${services}\nLocation: ${location}\nAbout: ${about}\nRating: ${rating}`
    );
}