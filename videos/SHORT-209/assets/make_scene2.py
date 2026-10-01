import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O BRASIL CALÇA O MUNDO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Principais Polos Calçadistas do Brasil (% Produção)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Abicalçados / MDIC (Participação estimada na produção nacional de calçados)
polos = ['Ceará (Sandálias/Injetados)', 'Rio Grande do Sul (Couro/Feminino)', 'São Paulo (Franca/Jaú/Birigui)', 'Minas Gerais (Nova Serrana)', 'Bahia & Outros']
shares = [32.0, 26.0, 18.0, 12.0, 12.0]
colors = ['#f59e0b', '#3b82f6', '#10b981', '#ec4899', '#64748b']

y_pos = np.arange(len(polos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, shares, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 42)
ax.set_ylim(-0.8, len(polos) - 0.2)
ax.axis('off')

for bar, polo, val in zip(bars, polos, shares):
    y = bar.get_y() + bar.get_height() / 2
    textColor = '#ffffff' if val >= 25.0 else '#cbd5e1'
    fontSize = 26 if val >= 25.0 else 22
    weight = 'bold' if val >= 25.0 else 'normal'
    
    ax.text(0.8, y + 0.38, polo.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 1.0, y, f"{val:.0f}%", color='#fbbf24', fontsize=26, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.24, 
        "4º MAIOR PRODUTOR DO PLANETA\n\n"
        "• ~880 Milhões de pares fabricados por ano\n"
        "• +140 Milhões de pares exportados para 150 países\n"
        "• +US$ 1,1 Bilhão em receita de exportação anual\n"
        "• 300 mil empregos diretos gerados pela cadeia", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.07, "Fontes: Abicalçados (Relatório Setorial) / MDIC / Comex Stat", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-209/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
