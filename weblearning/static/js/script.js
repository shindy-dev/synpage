const checkbox = document.getElementById('nav-menu-toggle')
const dummy = document.getElementById('dummy')

checkbox.addEventListener('change', function () {
    dummy.style.display = checkbox.checked ? 'block' : 'none';
});
dummy.addEventListener('click', function () {
    if (checkbox.checked) {
        checkbox.checked = false;
        checkbox.dispatchEvent(new Event('change'));
    }
});
