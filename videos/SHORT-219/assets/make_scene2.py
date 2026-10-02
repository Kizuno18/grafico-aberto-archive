import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O IMPÉRIO DA TILÁPIA NO BRASIL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Evolução da Produção de Tilápia (Mil Toneladas)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Peixe BR / Embrapa Pesca (Evolução da tilapicultura nacional)
anos = ['2014', '2016', '2018', '2020', '2022', '2024 (Est.)']
producao = [285.0, 357.0, 400.0, 486.0, 550.0, 610.0] # mil toneladas

x_pos = np.arange(len(anos))

# Gráfico de barras com linha de crescimento
bars = ax.bar(x_pos, producao, color=['#0284c7', '#0369a1', '#0ea5e9', '#38bdf8', '#06b6d4', '#10b981'], width=0.55, edgecolor='#1e293b', linewidth=2, zorder=3)
ax.plot(x_pos, producao, color='#fbbf24', linestyle='-', linewidth=4, marker='o', markersize=10, zorder=4)

ax.set_ylim(0, 720)
ax.set_xticks(x_pos)
ax.set_xticklabels(anos, color='#cbd5e1', fontsize=22, fontweight='bold')
ax.tick_params(axis='y', colors='#94a3b8', labelsize=20)
ax.grid(True, axis='y', linestyle=':', alpha=0.25, color='#475569')

# Rótulos nas barras
for bar, val in zip(bars, producao):
    y = bar.get_height()
    color = '#10b981' if val > 600 else '#ffffff'
    weight = 'bold' if val > 600 else 'normal'
    ax.text(bar.get_x() + bar.get_width()/2, y + 16, f"{val:.0f} mil", color=color, fontsize=22, fontweight=weight, ha='center')

# Posição dos eixos no layout vertical
ax.set_position([0.12, 0.45, 0.80, 0.35])

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
fig.text(0.5, 0.24, 
        "4º MAIOR PRODUTOR DE TILÁPIA DO MUNDO\n\n"
        "• Tilápia responde por mais de 65% de toda a piscicultura nacional\n"
        "• Paraná lidera isolado com mais de 210 mil toneladas (35% do total)\n"
        "• Seguido por São Paulo, Minas Gerais e Santa Catarina\n"
        "• Exportações de filé fresco crescendo +30% ao ano para os EUA", 
        color='#f8fafc', fontsize=24, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.07, "Fontes: Peixe BR (Anuário Brasileiro da Piscicultura) / Embrapa / MAPA", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-219/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
