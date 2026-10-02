import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "ALUMÍNIO, RENDA & CLIMA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Eficiência que Poupa o Planeta", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Economia de Energia
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.64,
        "[ O GANHO AMBIENTAL IMEDIATO ]\n\n"
        "A reciclagem consome apenas 5% da energia elétrica\n"
        "necessária para produzir alumínio primário da bauxita,\n"
        "evitando milhões de toneladas de emissões de CO2.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Impacto Social
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.44,
        "[ DIGNIDADE E SUSTENTO SOCIAL ]\n\n"
        "• Renda direta garantida para cooperativas em todo o país\n"
        "• Logística reversa mais eficiente e consolidada do planeta\n"
        "• Exemplo de reciclabilidade infinita sem perda de qualidade",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Abal / Abralatas / Cempre / MMA", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-234/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
