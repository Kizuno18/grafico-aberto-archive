import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A ENERGIA QUE VEM DA CANA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Capacidade Instalada de Biomassa de Cana (GW)", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Aneel / Unica (Potência outorgada de biomassa sucroenergética por estado)
estados = ['São Paulo', 'Minas Gerais', 'Goiás', 'Mato Grosso do Sul', 'Paraná', 'Outros']
potencia = [6.85, 1.85, 1.55, 1.25, 0.55, 0.60] # GW
colors = ['#10b981', '#059669', '#38bdf8', '#0284c7', '#f59e0b', '#64748b']

y_pos = np.arange(len(estados))
y_pos = y_pos[::-1]

bars = ax.barh(y_pos, potencia, color=colors, height=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_xlim(0, 8.8)
ax.set_ylim(-0.8, len(estados) - 0.2)
ax.axis('off')

for bar, est, val in zip(bars, estados, potencia):
    y = bar.get_y() + bar.get_height() / 2
    is_sp = est == 'São Paulo'
    textColor = '#ffffff' if is_sp else '#cbd5e1'
    fontSize = 28 if is_sp else 24
    weight = 'bold' if is_sp else 'normal'
    
    ax.text(0.2, y + 0.38, est.upper(), color=textColor, fontsize=fontSize, fontweight=weight, va='center')
    ax.text(val + 0.25, y, f"{val:.2f} GW".replace('.', ','), color='#fbbf24' if is_sp else '#94a3b8', fontsize=fontSize, fontweight='bold', va='center')

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.24, 
        "+12,6 GIGAWATTS DE POTÊNCIA NO BRASIL\n\n"
        "• SP concentra mais de 54% de toda a geração do setor\n"
        "• Autossuficiência das usinas de açúcar e etanol\n"
        "• Exportação de excedente elétrico para o Sistema Interligado\n"
        "• Equivale a quase uma usina de Itaipu operando no campo", 
        color='#f8fafc', fontsize=24, ha='center', va='center', transform=ax.transAxes, bbox=highlight_box, linespacing=1.6)

# Fonte
ax.text(0.5, 0.07, "Fontes: Aneel (SIGEL) / Unica / EPE / Cogen", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-217/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
