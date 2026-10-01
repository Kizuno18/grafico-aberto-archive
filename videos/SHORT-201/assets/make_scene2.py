import matplotlib.pyplot as plt
import numpy as np

# Configurar estilo visual padrão Gráfico Aberto
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Título do Short e Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "O IMPÉRIO DO SUCO DE LARANJA", color='#ffffff', fontsize=38, fontweight='heavy', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Participação no Comércio Global de Suco (FCOJ/NFC)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados do Gráfico
paises = ['Brasil', 'México', 'União Europeia', 'EUA', 'Outros']
shares = [75.0, 11.0, 6.0, 4.0, 4.0]
colors = ['#f97316', '#3b82f6', '#10b981', '#64748b', '#475569']

y_pos = np.arange(len(paises))
y_pos = y_pos[::-1] # Brasil no topo

bars = ax.barh(y_pos, shares, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

# Configurar eixos
ax.set_xlim(0, 95)
ax.set_ylim(-0.8, len(paises) - 0.2)
ax.axis('off')

# Rótulos nas barras
for idx, (bar, pais, val) in enumerate(zip(bars, paises, shares)):
    y = bar.get_y() + bar.get_height() / 2
    weight = 'bold' if pais == 'Brasil' else 'normal'
    textColor = '#ffffff' if pais == 'Brasil' else '#cbd5e1'
    fontSize = 32 if pais == 'Brasil' else 26
    
    ax.text(2, y + 0.38, pais.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    
    valColor = '#fbbf24' if pais == 'Brasil' else '#94a3b8'
    ax.text(val + 2.5, y, f"{val:.0f}%", color=valColor, fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#f97316', linewidth=2)
ax.text(0.5, 0.28, 
        "3 EM CADA 4 COPOS NO MUNDO\n\n"
        "Cinturão Citrícola SP & MG:\n"
        "• +1 Milhão de toneladas exportadas/ano\n"
        "• Faturamento cambial > US$ 2,5 Bilhões\n"
        "• Logística refrigerada via Porto de Santos", 
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.08, "Fontes: CitrusBR / Fundecitrus / Comex Stat (MDIC)", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-201/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
