import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "VENTO, MAR & TRANSIÇÃO", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Energia do Futuro nas Costas Brasileiras", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: O Polo do Hidrogênio Verde
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#0284c7', linewidth=2)
ax.text(0.5, 0.64,
        "[ HUBS DE EXPORTAÇÃO DE H2V ]\n\n"
        "Portos como Pecém no Ceará e Rio Grande no Sul\n"
        "se preparam para transformar o vento do mar em amônia\n"
        "e hidrogênio verde para abastecer indústrias da Europa.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Benefícios Ambientais e Emprego
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.44,
        "[ DESENVOLVIMENTO COSTEIRO ]\n\n"
        "• Indústria naval e portuária mobilizada para montagem em alto-mar\n"
        "• Menor impacto visual e acústico distante da orla litorânea\n"
        "• O Brasil posicionado no centro da transição energética do planeta",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Ibama / EPE / Abeeólica / CNI", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-243/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
