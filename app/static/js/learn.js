document.addEventListener('DOMContentLoaded', async () => {
  requireAuth();
  await loadContent();
});

async function loadContent() {
  try {
    const data = await apiFetch('/api/education');
    const items = data.items || [];
    const container = document.getElementById('contentList');
    if (container) {
      container.innerHTML = items.length ? items.map(renderContent).join('') : '<p class="empty-state">Nenhum conteúdo disponível.</p>';
    }
  } catch (error) {
    showToast(error.message, 'error');
  }
}

function renderContent(item) {
  return `
    <article class="learning-card">
      <span class="badge-soft">${item.categoria}</span>
      <h4>${item.titulo}</h4>
      <p>${item.resumo}</p>
      <div class="learning-meta">
        <span>Nível: ${item.nivel}</span>
        <span>${item.duracao_minutos} min</span>
      </div>
    </article>
  `;
}
