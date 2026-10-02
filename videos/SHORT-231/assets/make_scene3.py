import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
ax.axis('off')

# Cabeçalho
ax.text(0.5, 0.90, "GRÁFICO ABERTO", color='#f59e0b', fontsize=36, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.84, "ROBÓTICA, DADOS & SAFRA", color='#ffffff', fontsize=38, fontweight='bold', ha='center', transform=ax.transAxes)
ax.text(0.5, 0.80, "A Agricultura 4.0 nos Céus do Brasil", color='#94a3b8', fontsize=26, ha='center', transform=ax.transAxes)

# Bloco 1: Precisão Cirúrgica
box1 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#10b981', linewidth=2)
ax.text(0.5, 0.64,
        "[ APLICAÇÃO CIRÚRGICA ]\n\n"
        "Softwares mapeiam ervas daninhas por inteligência artificial\n"
        "e os drones aplicam defensivo apenas no ponto exato,\n"
        "poupando recursos e protegendo o meio ambiente.",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box1, linespacing=1.6)

# Bloco 2: Sustentabilidade e Segurança
box2 = dict(boxstyle='round,pad=1.2', facecolor='#161e2e', edgecolor='#3b82f6', linewidth=2)
ax.text(0.5, 0.44,
        "[ SEGURANÇA E DESCARBONIZAÇÃO ]\n\n"
        "• Zero exposição humana direta a produtos químicos\n"
        "• Motores 100% elétricos a bateria com energia limpa\n"
        "• Menor consumo de combustível fóssil de maquinário pesado",
        color='#f8fafc', fontsize=25, ha='center', va='center', transform=ax.transAxes, bbox=box2, linespacing=1.6)

# Call to Action
box_cta = dict(boxstyle='round,pad=1.4', facecolor='#f59e0b', edgecolor='#ffffff', linewidth=2)
ax.text(0.5, 0.22,
        "DADOS REAIS SEM ENROLAÇÃO\n\n"
        "Inscreva-se no canal @ograficoaberto\n"
        "Novos Shorts de dados todos os dias!",
        color='#0f172a', fontsize=30, fontweight='bold', ha='center', va='center', transform=ax.transAxes, bbox=box_cta, linespacing=1.6)

ax.text(0.5, 0.08, "Fontes: Sindag / Anac / MAPA / Embrapa", color='#64748b', fontsize=22, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('videos/SHORT-231/assets/scene3.png', dpi=100, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("scene3.png gerada com sucesso!")
