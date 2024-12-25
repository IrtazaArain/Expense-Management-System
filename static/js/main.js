// Check the stored theme preference or default to light theme
const currentTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', currentTheme);

// Function to toggle between light and dark themes
function toggleTheme() {
    const newTheme = document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme); 
    console.log("Hi")// Save the user's theme preference
}

// Attach the toggle function to a button
document.getElementById("theme-toggle-button").addEventListener("click", toggleTheme);
