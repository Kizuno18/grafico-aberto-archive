import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "CELULOSE SOLÚVEL & TECIDOS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Aplicações da Fibra de Eucalipto no Mundo (%)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Ibá / Abrafita / MDIC
aplicacoes = [
    'Tecidos (Viscose / Lyocell)',
    'Cápsulas & Farmacêutica',
    'Acetato (Filtros e Armações)',
    'Especialidades Químicas'
]
shares = [68.0, 14.0, 11.0, 7.0]
colors = ['#10b981', '#3b82f6', '#f59e0b', '#64748b']

y_pos = np.arange(len(aplicacoes))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, shares, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 85)
ax.set_ylim(-0.8, len(aplicacoes) - 0.2)
ax.axis('off')

for bar, app, val in zip(bars, aplicacoes, shares):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 50
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(2, y + 0.38, app.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 2, y, f"{val:.0f}%", color='#34d399' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.22, 
        "A REVOLUÇÃO DA MADEIRA SUSTENTÁVEL\n\n"
        "• O Brasil produz mais de 2,1 milhões de toneladas/ano\n"
        "• 100% proveniente de florestas plantadas de eucalipto\n"
        "• Fibras botânicas que substituem o poliéster fóssil\n"
        "• Viscose e Lyocell: toque de seda, conforto e biodegradabilidade\n"
        "• Mais de US$ 1,5 bilhão em exportações de alto valor agregado", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.05, "Fontes: Ibá (Indústria Brasileira de Árvores) / Abrafita / MDIC", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-224/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
