import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O ENCOLHIMENTO DA JUVENTUDE", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Proporção de Jovens (15 a 29 Anos) no Brasil (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Históricos do IBGE (Censos Demográficos)
anos = [1980, 1991, 2000, 2010, 2022]
proporcao = [29.1, 28.5, 27.8, 25.6, 21.9] # % da população total

x_pos = np.arange(len(anos))

# Gráfico de barras com linha de tendência
bars = ax.bar(x_pos, proporcao, color=['#3b82f6', '#0284c7', '#0ea5e9', '#f59e0b', '#ef4444'], width=0.55, edgecolor='#1e293b', linewidth=2, zorder=3)
ax.plot(x_pos, proporcao, color='#fca5a5', linestyle='--', linewidth=3, marker='o', markersize=10, zorder=4)

ax.set_ylim(0, 36)
ax.set_xticks(x_pos)
ax.set_xticklabels([str(a) for a in anos], color='#cbd5e1', fontsize=24, fontweight='bold')
ax.tick_params(axis='y', colors='#94a3b8', labelsize=20)
ax.grid(True, axis='y', linestyle=':', alpha=0.25, color='#475569')

# Rótulos nas barras
for bar, val in zip(bars, proporcao):
    y = bar.get_height()
    color = '#fbbf24' if val == 21.9 else '#ffffff'
    weight = 'bold' if val == 21.9 else 'normal'
    ax.text(bar.get_x() + bar.get_width()/2, y + 1.0, f"{val:.1f}%".replace('.', ','), color=color, fontsize=24, fontweight=weight, ha='center')

# Posição dos eixos no layout vertical
ax.set_position([0.12, 0.45, 0.80, 0.35])

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#ef4444', linewidth=2)
fig.text(0.5, 0.24, 
        "FIM DO BÔNUS DEMOGRÁFICO BRASILEIRO\n\n"
        "• Contingente jovem encolheu de 50 para 45 milhões em 10 anos\n"
        "• Menos jovens ingressando na População Economicamente Ativa\n"
        "• Envelhecimento 3x mais veloz que nos países europeus\n"
        "• Urgência de produtividade por trabalhador", 
        color='#f8fafc', fontsize=24, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.07, "Fontes: IBGE (Censos Demográficos 1980 a 2022) / Ipea", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-212/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
