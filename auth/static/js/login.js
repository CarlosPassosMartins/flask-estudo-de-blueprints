const loginForm = document.getElementById('loginForm');
const cadastroForm = document.getElementById('cadastroForm');
const toggleBtn = document.getElementById('toggleBtn');

toggleBtn.addEventListener('click', () => {
    loginForm.classList.toggle('hidden');
    cadastroForm.classList.toggle('hidden');
});