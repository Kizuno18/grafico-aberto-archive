import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "OS MAIORES AEROPORTOS", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Passageiros Anuais no Brasil (Milhões)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Anac / Infraero / Aena / GRU Airport
aeroportos = [
    'Guarulhos (SP - GRU)',
    'Congonhas (SP - CGH)',
    'Brasília (DF - BSB)',
    'Viracopos (Campinas - VCP)',
    'Confins (Belo Horizonte - CNF)',
    'Santos Dumont (RJ - SDU)',
    'Recife (PE - REC)'
]
passageiros = [41.3, 22.1, 14.8, 12.5, 10.7, 9.8, 9.0]
colors = ['#0284c7', '#38bdf8', '#f59e0b', '#10b981', '#6366f1', '#ec4899', '#64748b']

y_pos = np.arange(len(aeroportos))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, passageiros, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 52)
ax.set_ylim(-0.8, len(aeroportos) - 0.2)
ax.axis('off')

for bar, aero, val in zip(bars, aeroportos, passageiros):
    y = bar.get_y() + bar.get_height() / 2
    is_top = val >= 30.0
    textColor = '#ffffff' if is_top else '#cbd5e1'
    fontSize = 27 if is_top else 22
    weight = 'bold' if is_top else 'normal'
    
    ax.text(1.0, y + 0.38, aero.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    val_str = f"{val:.1f} mi".replace('.', ',')
    ax.text(val + 1.2, y, val_str, color='#38bdf8' if is_top else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#0284c7', linewidth=2)
ax.text(0.5, 0.20, 
        "A MALHA AÉREA MAIS DINÂMICA DO CONTINENTE\n\n"
        "• Mais de 112 milhões de passageiros transportados por ano\n"
        "• Guarulhos lidera conexões internacionais de longo curso\n"
        "• Congonhas concentra a ponte aérea corporativa mais densa\n"
        "• Viracopos e Brasília: os grandes hubs de distribuição regional\n"
        "• 2ª maior malha e frota comercial de todas as Américas", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.04, "Fontes: Anac (Dados Estatísticos) / Infraero / Aena Brasil", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-240/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
