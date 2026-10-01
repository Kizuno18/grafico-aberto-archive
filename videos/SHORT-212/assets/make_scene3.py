import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "A TRANSIÇÃO ACELERADA", color='#ffffff', fontsize=40, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Impactos no Mercado de Trabalho e Previdência", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Produtividade do Trabalho
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#ef4444', linewidth=2)
ax.text(0.5, 0.64,
        "[ A EQUAÇÃO DA PRODUTIVIDADE ]\n\n"
        "Com menos jovens ingressando na força de trabalho,\n"
        "o país não poderá crescer apenas somando braços:\n"
        "o salto de renda dependerá de qualificação técnica.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Educação Superior e Técnica
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.44,
        "[ PRIORIDADES NACIONAIS ]\n\n"
        "• Redução do contingente Nem-Nem (sem estudo e sem emprego)\n"
        "• Formação tecnológica acelerada em inteligência e indústria\n"
        "• Retenção de talentos qualificados dentro do Brasil",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#ef4444', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#ffffff', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: IBGE / Ipea / FGV Ibre", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-212/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
