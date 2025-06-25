function openModal(modalId) {
    document.getElementById(modalId).classList.add('active');
        document.body.style.overflow = 'hidden';
}
        
function closeModal(modalId) {
    document.getElementById(modalId).classList.remove('active');
    document.body.style.overflow = 'auto';
}
        
        // Close modal when clicking outside content
document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal(modal.id);
        }
    });
});
