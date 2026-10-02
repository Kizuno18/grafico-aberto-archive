import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "ONDE VIVEM OS INDÍGENAS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Censo Demográfico do IBGE (Mil Pessoas)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Censo 2022 (IBGE)
categorias = [
    'Fora de Terras Indígenas',
    'Em Terras Indígenas Demarcadas',
    'Manaus (Capital Líder)',
    'São Paulo & Salvador'
]
populacao = [1071.1, 622.5, 71.7, 29.4] # mil pessoas
colors = ['#dc2626', '#10b981', '#f59e0b', '#3b82f6']

y_pos = np.arange(len(categorias))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, populacao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 1300)
ax.set_ylim(-0.8, len(categorias) - 0.2)
ax.axis('off')

for bar, cat, val in zip(bars, categorias, populacao):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 600
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 28 if is_top else 24
    weight = 'bold' if is_top else 'normal'
    
    ax.text(25, y + 0.38, cat.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:,.1f} mil".replace(',', 'X').replace('.', ',').replace('X', '.')
    ax.text(val + 30, y, val_str, color='#f87171' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#dc2626', linewidth=2)
ax.text(0.5, 0.20, 
        "A GRANDE VIRADA DO CENSO 2022\n\n"
        "• 1.693.535 indígenas mapeados (quase o dobro de 2010)\n"
        "• 63,2% residem FORA de reservas oficialmente demarcadas\n"
        "• Manaus abriga mais de 71 mil indígenas (a maior capital)\n"
        "• Presentes em 86% dos municípios brasileiros (4.832 cidades)\n"
        "• Cidadania e autoidentificação reconhecidas em dados", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fonte: IBGE (Censo Demográfico 2022: Indígenas) / Funai", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-232/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
