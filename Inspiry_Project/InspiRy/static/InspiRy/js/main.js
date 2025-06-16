document.getElementById('postModal').querySelector('form').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('', {
        method: 'POST',
        body: formData,
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    });
    if (response.ok) {
        document.getElementById('postModal').classList.add('hidden');
        location.reload(); // Refresh to show new post (or update DOM dynamically)
    } else {
        const errors = await response.text();
        document.querySelector('#postModal .bg-white').insertAdjacentHTML('beforeend', '<p class="text-red-500">' + errors + '</p>');
    }
});


document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const response = await fetch('', {
            method: 'POST',
            body: formData,
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        });
        if (response.ok) {
            location.reload();
        }
    });
});

