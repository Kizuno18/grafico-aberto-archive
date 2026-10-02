import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O BRASIL NO TOP 10 DO PETRÓLEO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Produção Diária de Óleo Cru por País (Milhões de Barris/dia)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados IEA / EIA / ANP (Top Produtores de Petróleo do Mundo)
paises = ['EUA', 'Arábia Saudita', 'Rússia', 'Canadá', 'Iraque', 'China', 'Irã', 'Brasil', 'EAU', 'Kuwait']
producao = [13.2, 9.1, 9.0, 4.8, 4.3, 4.2, 3.8, 3.5, 3.2, 2.7]
colors = ['#64748b', '#64748b', '#64748b', '#64748b', '#64748b', '#64748b', '#64748b', '#38bdf8', '#64748b', '#64748b']

y_pos = np.arange(len(paises))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, producao, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 16.5)
ax.set_ylim(-0.8, len(paises) - 0.2)
ax.axis('off')

for bar, pais, val in zip(bars, paises, producao):
    y = bar.get_y() + bar.get_height() / 2
    is_br = pais == 'Brasil'
    textColor = '#ffffff' if is_br else '#cbd5e1'
    fontSize = 28 if is_br else 22
    weight = 'bold' if is_br else 'normal'
    
    ax.text(0.2, y + 0.38, pais.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 0.35, y, f"{val:.1f} M".replace('.', ','), color='#fbbf24' if is_br else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.17, 
        "+3,5 MILHÕES DE BARRIS POR DIA\n\n"
        "• O pré-sal responde por quase 80% da extração brasileira\n"
        "• Bacia de Santos é a maior produtora offshore de águas profundas\n"
        "• Exportações de petróleo bruto superam US$ 42 Bilhões/ano\n"
        "• China é o destino de mais de 45% do petróleo embarcado", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: ANP (Boletim da Produção) / IEA / MDIC / IBP", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-221/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
