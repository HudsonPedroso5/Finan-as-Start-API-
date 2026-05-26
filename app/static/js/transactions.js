document.addEventListener('DOMContentLoaded', async () => {
  requireAuth();
  await loadTransactions();

  const form = document.getElementById('transactionForm');
  if (!form) return;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(form).entries());

    try {
      const result = await apiFetch('/api/transactions', {
        method: 'POST',
        body: JSON.stringify(payload)
      });
      showToast(result.message, 'success');
      form.reset();
      await loadTransactions();
    } catch (error) {
      showToast(error.message, 'error');
    }
  });
});

async function loadTransactions() {
  try {
    const data = await apiFetch('/api/transactions');
    const items = data.items || [];
    const container = document.getElementById('transactionList');
    const receitaEl = document.getElementById('txReceitas');
    const despesaEl = document.getElementById('txDespesas');

    const receitas = items.filter(item => item.tipo === 'receita').reduce((sum, item) => sum + Number(item.valor), 0);
    const despesas = items.filter(item => item.tipo === 'despesa').reduce((sum, item) => sum + Number(item.valor), 0);

    if (receitaEl) receitaEl.textContent = formatMoney(receitas);
    if (despesaEl) despesaEl.textContent = formatMoney(despesas);

    if (container) {
      container.innerHTML = items.length ? items.map(renderTransaction).join('') : '<p class="empty-state">Nenhuma transação cadastrada.</p>';
    }
  } catch (error) {
    showToast(error.message, 'error');
  }
}

function renderTransaction(item) {
  return `
    <div class="item-row">
      <div>
        <strong>${item.categoria}</strong>
        <p>${item.descricao || 'Sem descrição'} · ${formatDate(item.data)}</p>
      </div>
      <div class="tx-actions">
        <span class="${item.tipo === 'receita' ? 'positive' : 'negative'}">
          ${item.tipo === 'receita' ? '+' : '-'}${formatMoney(item.valor)}
        </span>
        <button class="text-btn" onclick="deleteTransaction(${item.id})">Excluir</button>
      </div>
    </div>
  `;
}

async function deleteTransaction(id) {
  if (!confirm('Deseja excluir esta transação?')) return;
  try {
    const result = await apiFetch(`/api/transactions/${id}`, { method: 'DELETE' });
    showToast(result.message, 'success');
    await loadTransactions();
  } catch (error) {
    showToast(error.message, 'error');
  }
}
