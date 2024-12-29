function showResultFrame() {
    const iframe = document.getElementById('resultFrame');
    iframe.style.display = 'block';
    document.getElementById('resetButton').style.display = 'block';
}

function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    const theme = body.classList.contains('dark-mode') ? 'dark' : 'light';
    localStorage.setItem('theme', theme);
}

window.onload = function() {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
    }
}

function resetPage() {
    document.getElementById('resultFrame').style.display = 'none';
    document.getElementById('resetButton').style.display = 'none';
    document.getElementById('algorithmForm').reset();
}

function adjustIframeHeight() {
    const iframe = document.getElementById('resultFrame');
    iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
}