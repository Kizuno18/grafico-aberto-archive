import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "AGROFLORESTA & CHOCOLATE", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Força da Floresta Produtiva", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: A Revolução Agroflorestal
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.64,
        "[ FLORESTA EM PÉ E RENDA ]\n\n"
        "O cacau cultivado em agroflorestas e cabrucas\n"
        "recupera pastagens degradadas na Amazônia,\n"
        "preservando a biodiversidade e o solo fértil.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: O Mercado Bean-to-Bar
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#f59e0b', linewidth=2)
ax.text(0.5, 0.44,
        "[ O SALTO DO CHOCOLATE DE ORIGEM ]\n\n"
        "• Prêmios internacionais para o cacau de Ilhéus e Medicilândia\n"
        "• Explosão de marcas artesanais brasileiras bean-to-bar\n"
        "• Rastreabilidade, comércio ético e valorização do produtor",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Aipc / Ceplac / Conab / IBGE", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-226/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
