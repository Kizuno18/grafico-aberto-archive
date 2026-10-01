import matplotlib.pyplot as plt
import numpy as np

# Configuração global de estilo visual profissional e limpo
plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 150

BG_COLOR = '#0E141B'
CARD_COLOR = '#17212D'
TEXT_MAIN = '#F0F4F8'
TEXT_MUTED = '#8B9BAE'
ACCENT_GREEN = '#00D287'
ACCENT_BLUE = '#2E86DE'
ACCENT_CORAL = '#FF5A5F'

def save_fig(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.tight_layout(pad=3.0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gráfico da Pirâmide Etária (1980 vs 2022)
# ==========================================
def make_scene1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('BRASIL: A MUDANÇA DA ESTRUTURA ETÁRIA\nCenso Demográfico (1980 vs 2022)', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    age_groups = ['0-14 anos\n(Crianças/Jovens)', '15-64 anos\n(Idade Ativa)', '65+ anos\n(Idosos)']
    
    # 1980
    vals_1980 = [38.2, 57.8, 4.0]
    colors_1980 = [ACCENT_BLUE, '#485460', ACCENT_CORAL]
    bars1 = ax1.bar(age_groups, vals_1980, color=colors_1980, width=0.55, edgecolor='#2C3A47', linewidth=1.5)
    ax1.set_title('1980: Pirâmide Jovem Tradicional\n(Base Larga / Topo Estreito)', fontsize=16, color=TEXT_MAIN, pad=15)
    ax1.set_ylim(0, 70)
    ax1.set_ylabel('Participação na População (%)', color=TEXT_MUTED, fontsize=13)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for bar in bars1:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f'{yval:.1f}%', ha='center', va='bottom', 
                 color=TEXT_MAIN, fontsize=14, fontweight='bold')
    
    # 2022
    vals_2022 = [19.8, 69.3, 10.9]
    colors_2022 = [ACCENT_BLUE, '#485460', ACCENT_CORAL]
    bars2 = ax2.bar(age_groups, vals_2022, color=colors_2022, width=0.55, edgecolor='#2C3A47', linewidth=1.5)
    ax2.set_title('2022: Transição Acelerada\n(Base Encolhida / Topo em Expansão)', fontsize=16, color=TEXT_MAIN, pad=15)
    ax2.set_ylim(0, 70)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f'{yval:.1f}%', ha='center', va='bottom', 
                 color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.04, 'Fonte Primária: IBGE - Séries Estatísticas & Censo Demográfico 2022 | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-001/assets/scene1.png')

# ==========================================
# CENA 2: Queda da Fecundidade e Jovens (0-14 anos)
# ==========================================
def make_scene2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('O ENCOLHIMENTO DA BASE: FECUNDIDADE E JOVENS', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Queda na Proporção de 0-14 anos
    years = ['1980', '1991', '2000', '2010', '2022']
    young_share = [38.2, 34.7, 29.6, 24.1, 19.8]
    ax1.plot(years, young_share, marker='o', linewidth=3.5, markersize=10, color=ACCENT_BLUE)
    ax1.set_title('Proporção de Crianças e Jovens (0 a 14 anos)', fontsize=16, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('Percentual da População (%)', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(10, 45)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(True, linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for i, txt in enumerate(young_share):
        ax1.annotate(f"{txt:.1f}%", (years[i], young_share[i]+1.3), ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    # Gráfico 2: Taxa de Fecundidade Total (Filhos por mulher)
    fec_years = ['1960', '1980', '2000', '2010', '2022']
    fec_rate = [6.3, 4.1, 2.38, 1.90, 1.57]
    bars = ax2.bar(fec_years, fec_rate, color=['#576574', '#576574', '#576574', ACCENT_CORAL, ACCENT_CORAL], width=0.5)
    ax2.axhline(y=2.1, color=ACCENT_GREEN, linestyle=':', linewidth=2, label='Nível de Reposição Populacional (2.1)')
    ax2.set_title('Taxa de Fecundidade Total (Filhos por Mulher)', fontsize=16, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('Filhos por Mulher', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 7.5)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    ax2.legend(loc='upper right', frameon=True, facecolor=CARD_COLOR, edgecolor='#2C3A47', labelcolor=TEXT_MAIN, fontsize=11)
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 0.18, f'{yval:.2f}', ha='center', va='bottom', 
                 color=TEXT_MAIN, fontsize=13, fontweight='bold')

    fig.text(0.5, 0.04, 'Fonte Primária: IBGE - Censo Demográfico & Estatísticas do Registro Civil | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-001/assets/scene2.png')

# ==========================================
# CENA 3: Índice de Envelhecimento e Idade Mediana
# ==========================================
def make_scene3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('ENVELHECIMENTO POPULACIONAL ACELERADO', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Índice de Envelhecimento (Idosos 65+ para cada 100 Jovens 0-14)
    censo_years = ['1980', '1991', '2000', '2010', '2022']
    aging_index = [10.5, 13.9, 19.8, 30.7, 55.2]
    bars = ax1.bar(censo_years, aging_index, color=ACCENT_CORAL, width=0.5, edgecolor='#2C3A47', linewidth=1.5)
    ax1.set_title('Índice de Envelhecimento\n(Número de Idosos 65+ para cada 100 Crianças)', fontsize=16, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('Idosos para cada 100 Crianças', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 65)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for bar in bars:
        yval = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1.2, f'{yval:.1f}', ha='center', va='bottom', 
                 color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    # Gráfico 2: Idade Mediana do Brasileiro
    years_median = ['2010', '2022']
    val_median = [29, 35]
    bars2 = ax2.bar(years_median, val_median, color=[ACCENT_BLUE, ACCENT_GREEN], width=0.4, edgecolor='#2C3A47', linewidth=1.5)
    ax2.set_title('Idade Mediana do Brasileiro\n(Metade da população é mais velha que isso)', fontsize=16, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('Idade Mediana (Anos)', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 45)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for bar in bars2:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1.0, f'{int(yval)} anos', ha='center', va='bottom', 
                 color=TEXT_MAIN, fontsize=15, fontweight='bold')
    ax2.text(0.5, 0.45, '+6 ANOS\nem apenas 12 anos', ha='center', va='center', transform=ax2.transAxes,
             fontsize=18, fontweight='bold', color=ACCENT_GREEN, 
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_GREEN, linewidth=2))

    fig.text(0.5, 0.04, 'Fonte Primária: IBGE - Censo Demográfico 2022 (Resultados do Universo) | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-001/assets/scene3.png')

# ==========================================
# CENA 4: Painel de Impactos Econômicos e Sociais
# ==========================================
def make_scene4():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    fig.suptitle('O FIM DO BÔNUS DEMOGRÁFICO: 3 GRANDES DESAFIOS', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.92)
    
    # 3 Cartões explicativos
    cards = [
        ("1. EDUCAÇÃO BÁSICA", 
         "• Redução contínua de matrículas no ensino fundamental\n• Oportunidade de aumentar investimento por aluno\n• Fechamento e readequação de turmas infantis", 
         0.12, ACCENT_BLUE),
        ("2. MERCADO DE TRABALHO", 
         "• Menor entrada de novos jovens trabalhadores\n• Aumento da idade média da mão de obra\n• Urgência de aumentar produtividade por trabalhador", 
         0.42, ACCENT_GREEN),
        ("3. SAÚDE E PREVIDÊNCIA", 
         "• Mais de 32 milhões de pessoas com 60 anos ou mais\n• Pressão crescente sobre custos do SUS\n• Desafio fiscal contínuo de sustentabilidade previdenciária", 
         0.72, ACCENT_CORAL)
    ]
    
    for title, content, xpos, color in cards:
        rect = plt.Rectangle((xpos, 0.20), 0.24, 0.58, facecolor='#111A24', edgecolor=color, linewidth=2.5, 
                             transform=fig.transFigure, zorder=2)
        fig.patches.append(rect)
        fig.text(xpos + 0.02, 0.73, title, fontsize=15, fontweight='bold', color=color, transform=fig.transFigure)
        fig.text(xpos + 0.02, 0.46, content, fontsize=12, color=TEXT_MAIN, transform=fig.transFigure, linespacing=1.8)

    fig.text(0.5, 0.10, 'Canal Gráfico Aberto | A realidade explicada através dos dados oficiais', 
             ha='center', fontsize=14, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.05, 'Fontes: IBGE (Censo 2022, SIDRA) / IPEA / Ministério da Saúde', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-001/assets/scene4.png')

# ==========================================
# MINIATURA (THUMBNAIL) 1280x720
# ==========================================
def make_thumbnail():
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100, facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    # Texto de altíssimo impacto e legibilidade
    fig.text(0.08, 0.80, 'O BRASIL ENVELHECEU', fontsize=34, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.08, 0.70, 'O que o Censo 2022 revelou sobre nosso futuro', fontsize=20, color=TEXT_MAIN)
    
    # Gráfico miniatura destacado na thumbnail
    sub_ax = fig.add_axes([0.08, 0.16, 0.45, 0.44], facecolor='#111A24')
    sub_ax.bar(['1980', '2022'], [38.2, 19.8], color=[ACCENT_BLUE, ACCENT_CORAL], width=0.45)
    sub_ax.set_title('Jovens no Brasil (%)', fontsize=13, color=TEXT_MUTED)
    sub_ax.set_ylim(0, 45)
    sub_ax.tick_params(colors=TEXT_MUTED, labelsize=11)
    sub_ax.text(0, 39.5, '38.2%', ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
    sub_ax.text(1, 21.0, '19.8%', ha='center', color=ACCENT_CORAL, fontsize=13, fontweight='bold')
    sub_ax.grid(axis='y', linestyle=':', alpha=0.3, color='#FFF')
    
    # Cartão de número impactante
    card_box = plt.Rectangle((0.58, 0.16), 0.34, 0.44, facecolor='#111A24', edgecolor=ACCENT_GREEN, linewidth=3, 
                             transform=fig.transFigure)
    fig.patches.append(card_box)
    fig.text(0.75, 0.48, 'IDADE MEDIANA', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.75, 0.34, '35 ANOS', ha='center', fontsize=38, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.75, 0.22, '+6 anos em 12 anos', ha='center', fontsize=15, color=TEXT_MAIN)
    
    # Tag de marca
    fig.text(0.92, 0.90, 'GRÁFICO ABERTO', ha='right', fontsize=14, fontweight='bold', color=TEXT_MUTED)

    fig.patch.set_facecolor(BG_COLOR)
    plt.savefig('videos/PILOTO-001/export/thumbnail.png', facecolor=BG_COLOR, edgecolor='none')
    plt.close(fig)
    print("Salvo: videos/PILOTO-001/export/thumbnail.png")

make_scene1()
make_scene2()
make_scene3()
make_scene4()
make_thumbnail()
