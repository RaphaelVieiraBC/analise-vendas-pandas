import pandas as pd

df = pd.read_excel(r'C:\AnaliseDados\projetos_dados\dataset_vendas_pandas.xlsx')

# ── Informações gerais ─────────────────────────────────────────────────────────
percentualNulos = df.isnull().sum() / len(df) * 100
print(percentualNulos)

# ── Tratar valores nulos ───────────────────────────────────────────────────────

# Avaliação_Cliente → mediana
avaliacao_cliente = df['Avaliação_Cliente'].describe()
print('Coluna Avaliação_cliente:\n', avaliacao_cliente)

medianaAvaCliente = df['Avaliação_Cliente'].median()
df['Avaliação_Cliente'] = df['Avaliação_Cliente'].fillna(medianaAvaCliente)

# Status → 'Desconhecido'
df['Status'] = df['Status'].fillna('Desconhecido')  
print(df.info())

# ── Converter coluna Data ──────────────────────────────────────────────────────
df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d')  

# ── Receita por mês ────────────────────────────────────────────────────────────
df['Mês'] = df['Data'].dt.month
receita_por_mes = df.groupby('Mês')['Total_Venda'].sum().reset_index()
receita_por_mes.columns = ['Mês', 'Receita_Total']
print(f'\nReceita mensal:\n{receita_por_mes}')

# ── Produto mais vendido ───────────────────────────────────────────────────────

# Por quantidade de unidades
mais_vendido_qtd = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
print('\nProduto mais vendido por quantidade:\n', mais_vendido_qtd)

# Por receita gerada 
mais_vendido_receita = df.groupby('Produto')['Total_Venda'].sum().sort_values(ascending=False)
print('\nProduto mais vendido por receita:\n', mais_vendido_receita)

# ── Ticket medio ───────────────────────────────────────────────────────
ticket_medio = df['Total_Venda'].mean()
print(f'\nTicket Médio Geral: R$ {ticket_medio:,.2f}')

# Ticket médio por produto 
ticket_por_produto = df.groupby('Produto')['Total_Venda'].mean().sort_values(ascending=False)
print(f'\nTicket Médio por Produto:\n{ticket_por_produto}')

# ── Região com Maior Faturamento ───────────────────────────────────────────────
faturamento_por_regiao = df.groupby('Região')['Total_Venda'].sum().sort_values(ascending=False)
print(f'\nFaturamento por Região:\n{faturamento_por_regiao}')

# Descobrir qual é a número 1
regiao_top = faturamento_por_regiao.idxmax()
valor_top  = faturamento_por_regiao.max()
print(f'\nRegião com maior faturamento: {regiao_top} — R$ {valor_top:,.2f}')


#falta gerar a vizualização dos dados 