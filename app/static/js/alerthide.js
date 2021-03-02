const alert = document.querySelector('.alert');

if (alert != null) {
    setTimeout(function () {
        alert.parentNode.removeChild(alert)
    }, 4000);
}
