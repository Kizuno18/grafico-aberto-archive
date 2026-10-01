import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "LOGÍSTICA REVERSA & RENDA", color='#ffffff', fontsize=40, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "O Valor Esquecido no Nosso Lixo", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: A Força dos Catadores
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.64,
        "[ COOPERATIVAS DE TRIAGEM ]\n\n"
        "Os catadores de materiais recicláveis são responsáveis\n"
        "por recolher mais de 90% de tudo o que é reciclado\n"
        "nas cidades brasileiras, gerando sustento digno.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Logística Reversa
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.44,
        "[ ECONOMIA CIRCULAR ]\n\n"
        "• Metas de logística reversa para embalagens plásticas\n"
        "• Créditos de reciclagem e incentivos fiscais verdes\n"
        "• Triagem mecânica e usinas de valorização energética",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#10b981', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#064e3b', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Abrema / SNIS / Cempre / Ministério do Meio Ambiente", color='#64748b', fontsize=20, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-210/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
