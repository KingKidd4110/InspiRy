
    // Get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

    // Post creation form (modal)
const postForm = document.querySelector('#postModal form');
if (postForm) {
    postForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const errorContainer = this.querySelector('.error-container') || document.createElement('div');
        errorContainer.className = 'error-container text-red-500 mb-2';
        this.prepend(errorContainer);
        errorContainer.innerHTML = '';

        try {
            const response = await fetch('{% url "homepage" %}', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            if (response.ok) {
                document.getElementById('postModal').classList.add('hidden');
                location.reload();
            } else {
                const errorData = await response.json();
                errorContainer.innerHTML = errorData.errors || 'Failed to save post. Please check your input.';
            }
        } catch (error) {
            errorContainer.innerHTML = 'Network error: ' + error.message;
        }
    });
}

    // Comment and like forms
document.querySelectorAll('form.comment-form, form.like-form').forEach(form => {
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        const errorContainer = this.querySelector('.error-container') || document.createElement('div');
        errorContainer.className = 'error-container text-red-500 mb-2';
        this.prepend(errorContainer);
        errorContainer.innerHTML = '';

        try {
            const response = await fetch('{% url "homepage" %}', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            if (response.ok) {
                location.reload();
            } else {
                const errorData = await response.json();
                errorContainer.innerHTML = errorData.errors || 'Action failed. Please try again.';
            }
        } catch (error) {
            errorContainer.innerHTML = 'Network error: ' + error.message;
        }
    });
});
