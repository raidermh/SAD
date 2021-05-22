function toggleForm(buttonId, formId) {
    document.getElementById(buttonId).addEventListener('click', (event) => {
        event.preventDefault();
        let form = document.getElementById(formId);
        if (form.style.display === 'none') {
            form.style.display = 'block';
            event.target.textContent = `-${event.target.textContent.substring(1)}`;
        } else {
            form.style.display = 'none';
            event.target.textContent = `+${event.target.textContent.substring(1)}`;
        }
    });
}