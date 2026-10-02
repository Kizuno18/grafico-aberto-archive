import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A REVOLUÇÃO DO TRIGO NO BRASIL", color='#ffffff', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produção Nacional vs Importações (Milhões de Toneladas)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Conab / Embrapa Trigo (Evolução das safras recentes)
anos = ['2018', '2020', '2022', '2024 (Est.)']
producao = [5.4, 6.2, 9.6, 9.8]
importacao = [6.8, 6.4, 5.8, 4.9]

x_pos = np.arange(len(anos))
bar_width = 0.35

bars1 = ax.bar(x_pos - bar_width/2, producao, bar_width, label='Produção Nacional', color='#f59e0b', edgecolor='#1e293b', linewidth=2)
bars2 = ax.bar(x_pos + bar_width/2, importacao, bar_width, label='Importações (Arg/EUA)', color='#38bdf8', edgecolor='#1e293b', linewidth=2)

ax.set_ylim(0, 12.5)
ax.set_xticks(x_pos)
ax.set_xticklabels(anos, color='#cbd5e1', fontsize=24, fontweight='bold')
ax.tick_params(axis='y', colors='#94a3b8', labelsize=20)
ax.grid(True, axis='y', linestyle=':', alpha=0.25, color='#475569')

# Rótulos nas barras
for bar in bars1:
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, y + 0.3, f"{y:.1f}".replace('.', ','), color='#fbbf24', fontsize=22, fontweight='bold', ha='center')

for bar in bars2:
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, y + 0.3, f"{y:.1f}".replace('.', ','), color='#38bdf8', fontsize=22, fontweight='bold', ha='center')

ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.14), ncol=2, frameon=False, fontsize=22, labelcolor='#ffffff')

# Posição dos eixos no layout vertical
ax.set_position([0.12, 0.44, 0.80, 0.35])

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
fig.text(0.5, 0.23, 
        "O AVANÇO HISTÓRICO DO TRIGO TROPICAL\n\n"
        "• Embrapa adaptou variedades de trigo ao calor do Cerrado\n"
        "• Produtividade irrigada no Cerrado supera 6.000 kg/ha\n"
        "• Redução drástica da dependência de trigo argentino\n"
        "• Meta de autossuficiência nacional até o fim da década", 
        color='#f8fafc', fontsize=24, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.07, "Fontes: Conab (Série Histórica das Safras) / Embrapa Trigo / MDIC", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-214/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
