document.addEventListener('DOMContentLoaded', async () => {
  requireAuth();
  await loadGoals();

  const form = document.getElementById('goalForm');
  if (!form) return;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(form).entries());

    try {
      const result = await apiFetch('/api/goals', {
        method: 'POST',
        body: JSON.stringify(payload)
      });
      showToast(result.message, 'success');
      form.reset();
      await loadGoals();
    } catch (error) {
      showToast(error.message, 'error');
    }
  });
});

async function loadGoals() {
  try {
    const data = await apiFetch('/api/goals');
    const items = data.items || [];
    const container = document.getElementById('goalList');

    if (container) {
      container.innerHTML = items.length ? items.map(renderGoal).join('') : '<p class="empty-state">Nenhuma meta criada ainda.</p>';
    }
  } catch (error) {
    showToast(error.message, 'error');
  }
}

function renderGoal(item) {
  return `
    <div class="goal-card">
      <div class="goal-line">
        <strong>${item.titulo}</strong>
        <span>${item.progresso}%</span>
      </div>
      <p>${item.descricao || 'Sem descrição'}</p>
      <div class="progress-bar"><div style="width:${item.progresso}%"></div></div>
      <div class="goal-foot">
        <span>${formatMoney(item.valor_atual)} / ${formatMoney(item.valor_meta)}</span>
        <span>${formatDate(item.prazo)}</span>
      </div>
      <button class="text-btn" onclick="deleteGoal(${item.id})">Excluir</button>
    </div>
  `;
}

async function deleteGoal(id) {
  if (!confirm('Deseja excluir esta meta?')) return;
  try {
    const result = await apiFetch(`/api/goals/${id}`, { method: 'DELETE' });
    showToast(result.message, 'success');
    await loadGoals();
  } catch (error) {
    showToast(error.message, 'error');
  }
}
