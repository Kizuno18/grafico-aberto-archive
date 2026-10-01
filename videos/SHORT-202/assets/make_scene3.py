import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "O DESAFIO DO FUTURO", color='#ffffff', fontsize=42, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "Impactos Sociais e Econômicos", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Envelhecimento Previdenciário
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#f43f5e', linewidth=2)
ax.text(0.5, 0.64,
        "[ PREVIDÊNCIA E MERCADO DE TRABALHO ]\n\n"
        "Menos jovens ingressando na força de trabalho\n"
        "significa maior pressão sobre aposentadorias,\n"
        "saúde pública e demanda por cuidadores.",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: A Janela de Produtividade
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#38bdf8', linewidth=2)
ax.text(0.5, 0.44,
        "[ TRANSIÇÃO DEMOGRÁFICA ]\n\n"
        "• Fechamento do bônus demográfico brasileiro\n"
        "• Urgência em salto educacional e tecnologia\n"
        "• Envelhecer rico vs envelhecer emergente",
        color='#f8fafc', fontsize=26, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: IBGE / Ipea / Ministério da Previdência", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-202/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
