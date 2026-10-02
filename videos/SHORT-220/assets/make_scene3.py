import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "A NOVA ECONOMIA URBANA", color='#ffffff', fontsize=40, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Mobilidade Individual e Renda Flexível", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Inclusão Produtiva
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.64,
        "[ COLCHÃO CONTRA O DESEMPREGO ]\n\n"
        "As plataformas de transporte tornaram-se o maior amortecedor\n"
        "social do mercado de trabalho brasileiro, permitindo renda rápida\n"
        "para chefes de família em momentos de crise econômica.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: A Sobrevivência do Táxi
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#fbbf24', linewidth=2)
ax.text(0.5, 0.44,
        "[ O NOVO PAPEL DOS TÁXIS ]\n\n"
        "• Acesso prioritário a faixas e corredores exclusivos de ônibus\n"
        "• Isenção de impostos (IPI e ICMS) na compra de veículos novos\n"
        "• Forte presença corporativa e pontos em aeroportos e hotéis",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#38bdf8', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Amobitec / IBGE / Ipea / Fipe", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-220/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
