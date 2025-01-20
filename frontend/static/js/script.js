function showResultFrame() {
    const iframe = document.getElementById('resultFrame');
    iframe.style.display = 'block';
    document.getElementById('resetButton').style.display = 'block';
}

// function toggleTheme() {
//     const body = document.body;
//     body.classList.toggle('dark-mode');
//     const theme = body.classList.contains('dark-mode') ? 'dark' : 'light';
//     localStorage.setItem('theme', theme);

//     // Apply the theme to the iframe content
//     const iframe = document.getElementById('resultFrame');
//     if (iframe) {
//         const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
//         if (iframeDocument) {
//             iframeDocument.body.classList.toggle('dark-mode', theme === 'dark');
//         }
//     }

//     // Update the slider position based on the theme
//     const themeToggle = document.getElementById('themeToggle');
//     themeToggle.checked = theme === 'dark';
// }

function updateThemeIcon() {
    const themeIcon = document.getElementById('theme-icon');
    const isDarkMode = document.body.classList.contains('dark-mode');
    themeIcon.className = isDarkMode ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
}

function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    const theme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', theme);

    // Apply the theme to the iframe content
    const iframe = document.getElementById('resultFrame');
    if (iframe) {
        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        if (iframeDocument) {
            iframeDocument.body.classList.toggle('dark-mode', theme === 'dark');
        }
    }

    // Update the slider position based on the theme
    const themeToggle = document.getElementById('themeToggle');
    // Add any additional logic for themeToggle if needed

    // Update the theme icon
    updateThemeIcon();
}

// Ensure the function is accessible globally
window.toggleTheme = toggleTheme;

// Update the theme icon on page load
document.addEventListener('DOMContentLoaded', updateThemeIcon);

document.addEventListener('DOMContentLoaded', function() {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    }

    // Apply the theme to the iframe content on page load
    const iframe = document.getElementById('resultFrame');
    if (iframe) {
        const iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
        if (iframeDocument) {
            iframeDocument.body.classList.toggle('dark-mode', theme === 'dark');
        }
    }
});

function resetPage() {
    document.getElementById('resultFrame').style.display = 'none';
    document.getElementById('resetButton').style.display = 'none';
    document.getElementById('algorithmForm').reset();
}

function adjustIframeHeight() {
    const iframe = document.getElementById('resultFrame');
    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
}