import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "OS GIGANTES DO PRÉ-SAL", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produção Diária por Campo Offshore (Mil Barris/Dia)", color='#94a3b8', fontsize=23, ha='center', transform=ax.transAxes)

# Dados ANP (Boletim Mensal da Produção) / Petrobras
campos = [
    'Búzios (Maior Campo Offshore)',
    'Tupi (Pioneiro do Pré-Sal)',
    'Mero (Bacia de Santos)',
    'Sapinhoá (Bacia de Santos)',
    'Peregrino (Bacia de Campos)',
    'Jubarte (Parque das Baleias)'
]
producao = [625.0, 575.0, 245.0, 185.0, 110.0, 95.0]
colors = ['#f59e0b', '#d97706', '#0284c7', '#38bdf8', '#64748b', '#475569']

y_pos = np.arange(len(campos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, producao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 780)
ax.set_ylim(-0.8, len(campos) - 0.2)
ax.axis('off')

for bar, camp, val in zip(bars, campos, producao):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 500.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 27 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(12, y + 0.38, camp.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:,.0f} mil bpd".replace(',', '.')
    ax.text(val + 15, y, val_str, color='#fbbf24' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.20, 
        "O PETRÓLEO EM ÁGUAS ULTRAPROFUNDAS\n\n"
        "• O pré-sal responde por quase 80% do petróleo extraído no país\n"
        "• Búzios e Tupi sozinhos produzem 1,2 milhão de barris diários\n"
        "• Reservatórios a mais de 200 km da costa e 7.000m de profundidade\n"
        "• Camada de sal espessa de até 2.000 metros sob o fundo do mar\n"
        "• Plataformas FPSO de ponta gerando bilhões em royalties e divisas", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: ANP (Boletim da Produção de Petróleo) / Petrobras / IBP", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-241/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
