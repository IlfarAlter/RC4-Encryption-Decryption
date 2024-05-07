// Animasi ketika halaman dimuat
window.onload = function() {
    document.querySelector('.form-container').style.opacity = '1';
}

// Animasi ketika tombol submit ditekan
document.querySelector('.submit-btn').addEventListener('click', function() {
    this.style.transform = 'scale(0.95)';
});

// Animasi kembali ke ukuran normal saat tombol submit dilepaskan
document.querySelector('.submit-btn').addEventListener('mouseup', function() {
    this.style.transform = 'scale(1)';
});

// Animasi untuk input fields saat fokus dan blur
const inputFields = document.querySelectorAll('input[type="text"], textarea');
inputFields.forEach(input => {
    input.addEventListener('focus', function() {
        this.style.border = '2px solid #007bff';
    });
    input.addEventListener('blur', function() {
        this.style.border = '1px solid #ccc';
    });
});
