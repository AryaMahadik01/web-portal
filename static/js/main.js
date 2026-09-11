// Function to update HR form position field when "Apply Now" is clicked
function openHrModal(positionTitle) {
    const positionInput = document.getElementById('selected-position');
    if (positionInput) {
        positionInput.value = positionTitle;
    }
    // Smooth scroll down to application form
    document.getElementById('apply-form-container').scrollIntoView({ behavior: 'smooth' });
}

// Mobile Navbar Toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
        if (navLinks.style.display === 'flex') {
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '70px';
            navLinks.style.left = '0';
            navLinks.style.width = '100%';
            navLinks.style.background = '#0b0f19';
            navLinks.style.padding = '2rem';
            navLinks.style.borderBottom = '1px solid #1f2937';
        }
    });
}