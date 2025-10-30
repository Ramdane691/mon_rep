document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.toggle').forEach(title => {
        title.addEventListener('click', () => {
            const content = title.nextElementSibling;
            if (content) {
                content.classList.toggle('hidden');
            }
        });
    });
});