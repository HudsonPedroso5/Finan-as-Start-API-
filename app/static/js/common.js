function getToken() {
  return localStorage.getItem('fs_token');
}

function getUser() {
  try {
    return JSON.parse(localStorage.getItem('fs_user') || 'null');
  } catch {
    return null;
  }
}

function saveSession(data) {
  if (data?.token) localStorage.setItem('fs_token', data.token);
  if (data?.user) localStorage.setItem('fs_user', JSON.stringify(data.user));
  updateUserPill();
}

function logout() {
  localStorage.removeItem('fs_token');
  localStorage.removeItem('fs_user');
  window.location.href = '/login';
}

function updateUserPill() {
  const user = getUser();
  const el = document.getElementById('topUser');
  if (el) el.textContent = user?.nome || 'Usuário';
  const navAvatar = document.getElementById('profileAvatar');
  if (navAvatar && user?.avatar) navAvatar.textContent = user.avatar;
  const profileName = document.getElementById('profileName');
  if (profileName && user?.nome) profileName.textContent = user.nome;
}

function toggleSidebar() {
  document.body.classList.toggle('sidebar-open');
}

async function apiFetch(url, options = {}) {
  const headers = options.headers || {};
  headers['Content-Type'] = 'application/json';
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;
  const response = await fetch(url, { ...options, headers });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.message || 'Falha na requisição.');
  }
  return data;
}

function formatMoney(value) {
  const number = Number(value || 0);
  return number.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
}

function formatDate(dateStr) {
  if (!dateStr) return '-';
  return new Date(dateStr).toLocaleDateString('pt-BR');
}

function showToast(message, type = 'success') {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.className = `toast-box show ${type}`;
  setTimeout(() => {
    toast.className = 'toast-box';
  }, 2800);
}

function requireAuth() {
  if (!getToken()) {
    window.location.href = '/login';
  }
}

document.addEventListener('DOMContentLoaded', () => {
  updateUserPill();
});
