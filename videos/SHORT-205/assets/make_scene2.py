import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

# Cabeçalho
ax.text(0.5, 0.93, "GRÁFICO ABERTO", color='#f59e0b', fontsize=32, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.88, "A EXPLOSÃO DE VAGAS DE MEDICINA", color='#ffffff', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.85, "Evolução das Vagas Anuais de Graduação no Brasil", color='#94a3b8', fontsize=24, ha='center', transform=ax.transAxes)

# Dados Inep / Censo da Educação Superior / CFM
anos = [2010, 2014, 2018, 2021, 2024]
vagas = [15.2, 21.6, 31.4, 37.8, 42.5] # mil vagas

# Plot em barras verticais estilizadas
x_pos = np.arange(len(anos))
bars = ax.bar(x_pos, vagas, color=['#0284c7', '#0ea5e9', '#38bdf8', '#06b6d4', '#14b8a6'], width=0.55, edgecolor='#1e293b', linewidth=2)

ax.set_ylim(0, 52)
ax.set_xticks(x_pos)
ax.set_xticklabels([str(a) for a in anos], color='#cbd5e1', fontsize=24, fontweight='bold')
ax.tick_params(axis='y', colors='#94a3b8', labelsize=20)
ax.grid(True, axis='y', linestyle=':', alpha=0.25, color='#475569')

# Rótulos nas barras
for bar, val in zip(bars, vagas):
    y = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, y + 1.2, f"{val:.1f} mil".replace('.', ','), color='#fbbf24', fontsize=24, fontweight='bold', ha='center')

# Posição dos eixos no layout vertical
ax.set_position([0.12, 0.46, 0.80, 0.35])

# Bloco de destaque analítico
highlight_box = dict(boxstyle='round,pad=1.2', facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
fig.text(0.5, 0.26, 
        "+380 FACULDADES DE MEDICINA NO PAÍS\n\n"
        "• Brasil é o 2º país com mais faculdades no mundo (atrás da Índia)\n"
        "• Mais de 70% das novas vagas criadas no interior do país\n"
        "• Setor privado responde por mais de 75% da oferta de vagas", 
        color='#f8fafc', fontsize=26, ha='center', va='center', bbox=highlight_box, linespacing=1.6)

# Fonte
fig.text(0.5, 0.08, "Fontes: Inep (Censo da Educação Superior) / CFM / Demografia Médica", color='#64748b', fontsize=20, ha='center')

plt.savefig('videos/SHORT-205/assets/scene2.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene2.png gerada com sucesso!")
