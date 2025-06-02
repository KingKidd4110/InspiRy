window.addEventListener('load', function() {
    const loadingScreen = document.getElementById('loading-screen');
    const mainContent = document.getElementById('main-content');

    loadingScreen.classList.add('hidden');
    mainContent.classList.remove('hidden');
});
