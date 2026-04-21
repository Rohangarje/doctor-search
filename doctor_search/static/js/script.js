// User menu toggle
window.toggleUserMenu = function() {
    document.getElementById('userMenu').classList.toggle('show');
}

// Book modal logic
window.showBookModal = function(doctorId) {
    document.getElementById('bookModal').style.display = 'flex';
    // Optionally, load doctor info by ID
}
window.closeBookModal = function() {
    document.getElementById('bookModal').style.display = 'none';
}

// Hide user menu on click outside
document.addEventListener('click', function(e) {
    const menu = document.getElementById('userMenu');
    const avatar = document.querySelector('.user-avatar');
    if (menu && !menu.contains(e.target) && avatar !== e.target) {
        menu.classList.remove('show');
    }
});

// Smooth card animation on scroll (intersection observer)
if ('IntersectionObserver' in window) {
    const cards = document.querySelectorAll('.doctor-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });
    cards.forEach(card => observer.observe(card));
}

// Map integration (Leaflet.js demo, replace with your API key and logic)
window.initDoctorMap = function() {
    if (window.L && document.getElementById('doctorMap')) {
        var map = L.map('doctorMap').setView([20.5937, 78.9629], 4); // Center on India
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        // Optionally, add doctor markers here
    }
}
if (document.getElementById('doctorMap')) {
    // Load Leaflet CSS/JS dynamically if not present
    if (!window.L) {
        var leafletCSS = document.createElement('link');
        leafletCSS.rel = 'stylesheet';
        leafletCSS.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
        document.head.appendChild(leafletCSS);
        var leafletJS = document.createElement('script');
        leafletJS.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
        leafletJS.onload = window.initDoctorMap;
        document.body.appendChild(leafletJS);
    } else {
        window.initDoctorMap();
    }
}

// Location auto-detect for search bar
document.querySelectorAll('.detect-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        e.preventDefault();
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(pos) {
                // Use a geocoding API to get city/location from lat/lng
                const lat = pos.coords.latitude;
                const lng = pos.coords.longitude;
                fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`)
                  .then(res => res.json())
                  .then(data => {
                    const locInput = btn.parentElement.querySelector('input[name="location"]');
                    if (locInput && data.address) {
                        locInput.value = data.address.city || data.address.town || data.address.village || data.display_name;
                    }
                  });
            });
        }
    });
});