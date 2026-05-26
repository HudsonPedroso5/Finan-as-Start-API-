document.addEventListener('DOMContentLoaded', async () => {
  requireAuth();

  try {
    const data = await apiFetch('/api/dashboard/summary');
    const summary = data.summary;

    document.getElementById('receitas').textContent = formatMoney(summary.receitas);
    document.getElementById('despesas').textContent = formatMoney(summary.despesas);
    document.getElementById('saldo').textContent = formatMoney(summary.saldo);
    document.getElementById('metasAtivas').textContent = summary.goals.length;

    renderRecent(summary.recent_transactions || []);
    renderGoals(summary.goals || []);
    renderContents(summary.educational_contents || []);
    renderChart(summary.receitas, summary.despesas);
  } catch (error) {
    showToast(error.message, 'error');
  }
});

function renderRecent(items) {
  const container = document.getElementById('recentTransactions');
  if (!container) return;
  container.innerHTML = items.length
    ? items.map(item => `
      <div class="item-row">
        <div>
          <strong>${item.categoria}</strong>
          <p>${item.descricao || 'Sem descrição'} · ${formatDate(item.data)}</p>
        </div>
        <span class="${item.tipo === 'receita' ? 'positive' : 'negative'}">
          ${item.tipo === 'receita' ? '+' : '-'}${formatMoney(item.valor)}
        </span>
      </div>
    `).join('')
    : '<p class="empty-state">Nenhuma transação registrada.</p>';
}

function renderGoals(items) {
  const container = document.getElementById('goalPreview');
  if (!container) return;
  container.innerHTML = items.length
    ? items.map(item => `
      <div class="goal-item">
        <div class="goal-line">
          <strong>${item.titulo}</strong>
          <span>${item.progresso}%</span>
        </div>
        <div class="progress-bar"><div style="width:${item.progresso}%"></div></div>
        <p>${formatMoney(item.valor_atual)} de ${formatMoney(item.valor_meta)} · prazo ${formatDate(item.prazo)}</p>
      </div>
    `).join('')
    : '<p class="empty-state">Crie sua primeira meta para acompanhar o progresso.</p>';
}

function renderContents(items) {
  const container = document.getElementById('contentPreview');
  if (!container) return;
  container.innerHTML = items.length
    ? items.map(item => `
      <div class="content-item">
        <strong>${item.titulo}</strong>
        <p>${item.resumo}</p>
      </div>
    `).join('')
    : '<p class="empty-state">Sem conteúdos disponíveis.</p>';
}

function renderChart(receitas, despesas) {
  const canvas = document.getElementById('financeChart');
  if (!canvas || typeof Chart === 'undefined') return;
  new Chart(canvas, {
    type: 'doughnut',
    data: {
      labels: ['Receitas', 'Despesas'],
      datasets: [{
        data: [receitas, despesas],
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { position: 'bottom' } }
    }
  });
}
