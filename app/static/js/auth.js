document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const registerForm = document.getElementById('registerForm');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const form = new FormData(loginForm);
      const payload = Object.fromEntries(form.entries());

      try {
        const result = await apiFetch('/api/auth/login', {
          method: 'POST',
          body: JSON.stringify(payload)
        });
        saveSession(result);
        showToast(result.message, 'success');
        window.location.href = '/dashboard';
      } catch (error) {
        showToast(error.message, 'error');
      }
    });
  }

  if (registerForm) {
    registerForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const form = new FormData(registerForm);
      const payload = Object.fromEntries(form.entries());

      try {
        const result = await apiFetch('/api/auth/register', {
          method: 'POST',
          body: JSON.stringify(payload)
        });
        saveSession(result);
        showToast(result.message, 'success');
        window.location.href = '/dashboard';
      } catch (error) {
        showToast(error.message, 'error');
      }
    });
  }
});
