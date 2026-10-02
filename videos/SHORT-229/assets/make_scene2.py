import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O BOOM DOS BIOINSUMOS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Evolução do Mercado no Brasil (R$ Bilhões)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados CropLife Brasil / Kynetec / Embrapa / MAPA
anos = ['2018', '2020', '2022', '2024', '2026 (Proj.)']
faturamento = [1.0, 2.1, 3.9, 5.2, 7.0] # bilhões de reais
colors = ['#166534', '#15803d', '#16a34a', '#22c55e', '#4ade80']

y_pos = np.arange(len(anos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, faturamento, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 9.0)
ax.set_ylim(-0.8, len(anos) - 0.2)
ax.axis('off')

for bar, ano, val in zip(bars, anos, faturamento):
    y = bar.get_y() + bar.get_height() / 2
    is_top = '2024' in ano or 'Proj' in ano
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(0.2, y + 0.38, ano.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"R$ {val:.1f} bi".replace('.', ',')
    ax.text(val + 0.25, y, val_str, color='#86efac' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#22c55e', linewidth=2)
ax.text(0.5, 0.20, 
        "O BRASIL LIDERA O AGRO REGENERATIVO\n\n"
        "• Crescimento explosivo de mais de 30% ao ano no campo\n"
        "• Mais de 70 milhões de hectares tratados com biológicos\n"
        "• Inoculantes bacterianos poupam bilhões em adubos químicos\n"
        "• Controle biológico substitui inseticidas fósseis tradicionais\n"
        "• Soja, milho e cana puxam a revolução sustentável nacional", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: CropLife Brasil / Kynetec / Embrapa Meio Ambiente / MAPA", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-229/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
