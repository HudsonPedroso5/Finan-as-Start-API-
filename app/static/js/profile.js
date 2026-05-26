document.addEventListener('DOMContentLoaded', async () => {
  requireAuth();
  await loadProfile();

  const form = document.getElementById('profileForm');
  if (!form) return;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(form).entries());

    try {
      const result = await apiFetch('/api/auth/me', {
        method: 'PUT',
        body: JSON.stringify(payload)
      });
      saveSession({ user: result.user, token: getToken() });
      showToast(result.message, 'success');
      await loadProfile();
    } catch (error) {
      showToast(error.message, 'error');
    }
  });
});

async function loadProfile() {
  try {
    const data = await apiFetch('/api/auth/me');
    const user = data.user;
    localStorage.setItem('fs_user', JSON.stringify(user));

    const nameEl = document.getElementById('profileName');
    const emailEl = document.getElementById('profileEmail');
    const avatarEl = document.getElementById('profileAvatar');
    const createdEl = document.getElementById('profileCreated');

    if (nameEl) nameEl.textContent = user.nome;
    if (emailEl) emailEl.textContent = user.email;
    if (avatarEl) avatarEl.textContent = user.avatar || 'FS';
    if (createdEl) createdEl.textContent = formatDate(user.created_at);

    const form = document.getElementById('profileForm');
    if (form) {
      form.nome.value = user.nome || '';
      form.avatar.value = user.avatar || '';
    }
  } catch (error) {
    showToast(error.message, 'error');
  }
}
