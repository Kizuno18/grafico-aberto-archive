import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "INFRAESTRUTURA & CARGA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Os Desafios de Integrar o Continente", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: O Efeito das Concessões
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#0284c7', linewidth=2)
ax.text(0.5, 0.64,
        "[ O IMPACTO DAS CONCESSÕES ]\n\n"
        "Mais de 90% dos passageiros hoje embarcam em terminais\n"
        "geridos por concessões privadas, que injetaram bilhões\n"
        "em modernização de pistas, novos fingers e tecnologia.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: O Salto das Cargas Aéreas
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ LOGÍSTICA DE ALTO VALOR ]\n\n"
        "• Viracopos e Guarulhos lideram a entrada de fármacos e chips\n"
        "• Explosão do e-commerce rápido com entregas no mesmo dia\n"
        "• Ligação vital para capitais do Norte isoladas por terra",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Anac / Infraero / Aena / ABR", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-240/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
