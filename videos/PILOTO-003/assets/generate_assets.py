import matplotlib.pyplot as plt
import numpy as np

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
ACCENT_CYAN = '#00CEC9'
ACCENT_YELLOW = '#FDCB6E'
ACCENT_CORAL = '#FF5A5F'

def save_fig(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.tight_layout(pad=3.0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', bbox_inches='tight')
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Brasil vs Mundo na Eletricidade Renovável
# ==========================================
def make_scene1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('DE ONDE VEM A NOSSA ENERGIA?\nParticipação de Fontes Renováveis na Matriz Elétrica (Brasil vs Mundo)', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Barras comparativas
    labels = ['Mundo\n(Média Global)', 'Brasil\n(Sistema Nacional)']
    vals = [30.2, 87.9]
    colors = ['#576574', ACCENT_GREEN]
    bars = ax1.bar(labels, vals, color=colors, width=0.45, edgecolor='#2C3A47', lw=2)
    ax1.set_title('Percentual de Energia Renovável na Geração Elétrica', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% da Matriz Elétrica', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 105)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 2, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax1.text(0.5, 0.45, 'O BRASIL TEM QUASE 3X MAIS\nRENOVÁVEIS QUE A MÉDIA GLOBAL', ha='center', va='center', 
             transform=ax1.transAxes, fontsize=15, fontweight='bold', color=ACCENT_GREEN,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_GREEN, lw=2))
        
    # Gráfico 2: Composição Renovável vs Não Renovável
    categories = ['Brasil', 'Mundo']
    renovaveis = [87.9, 30.2]
    fossil = [12.1, 69.8]
    ax2.barh(categories, renovaveis, color=ACCENT_GREEN, label='Renovável (Água, Vento, Sol, Biomassa)', height=0.4)
    ax2.barh(categories, fossil, left=renovaveis, color='#485460', label='Não Renovável (Carvão, Gás, Petróleo, Nuclear)', height=0.4)
    ax2.set_title('Divisão Geral da Eletricidade', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_xlabel('% do Total Gerado', color=TEXT_MUTED, fontsize=13)
    ax2.set_xlim(0, 100)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='x', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    ax2.legend(loc='lower center', frameon=True, facecolor=CARD_COLOR, edgecolor='#2C3A47', labelcolor=TEXT_MAIN, fontsize=11)
    
    fig.text(0.5, 0.04, 'Fontes Primárias: Empresa de Pesquisa Energética (EPE/BEN) & IEA (World Energy Outlook) | Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-003/assets/scene1.png')

# ==========================================
# CENA 2: A Matriz Elétrica Brasileira Detalhada
# ==========================================
def make_scene2():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('COMO O BRASIL GERA SUA ELETRICIDADE?\nComposição Detalhada da Matriz Elétrica Nacional', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Barras detalhadas por fonte
    sources = ['Hidrelétrica', 'Eólica\n(Vento)', 'Biomassa\n(Cana)', 'Solar\n(Sol)', 'Fósseis / Outras']
    shares = [58.0, 14.8, 8.4, 6.7, 12.1]
    colors = [ACCENT_BLUE, ACCENT_CYAN, ACCENT_GREEN, ACCENT_YELLOW, '#576574']
    bars = ax1.bar(sources, shares, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    ax1.set_title('Participação de Cada Fonte na Geração (%)', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% da Geração Total', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 70)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=11)
    for b in bars:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 1.2, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    # Gráfico 2: As Novas Renováveis (Eólica + Solar + Biomassa)
    ax2.bar(['Eólica + Solar + Biomassa\n(Geração Moderna)', 'Hidrelétricas\n(Base Tradicional)'], [29.9, 58.0],
            color=[ACCENT_CYAN, ACCENT_BLUE], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('A Revolução das Novas Renováveis', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('% da Eletricidade', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 70)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    ax2.text(0, 31.5, '29.9%', ha='center', color=TEXT_MAIN, fontsize=15, fontweight='bold')
    ax2.text(1, 59.5, '58.0%', ha='center', color=TEXT_MAIN, fontsize=15, fontweight='bold')
    ax2.text(0.5, 0.55, 'QUASE 1/3 DA LUZ DO PAÍS\nJÁ VEM DE VENTO, SOL E CANA!', ha='center', va='center', 
             transform=ax2.transAxes, fontsize=15, fontweight='bold', color=ACCENT_CYAN,
             bbox=dict(boxstyle='round,pad=0.6', facecolor='#0E141B', edgecolor=ACCENT_CYAN, lw=2))

    fig.text(0.5, 0.04, 'Fonte Primária: Balanço Energético Nacional (BEN/EPE) & ONS | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-003/assets/scene2.png')

# ==========================================
# CENA 3: O Contraste dos Combustíveis Fósseis (Carvão e Gás)
# ==========================================
def make_scene3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9), facecolor=BG_COLOR)
    fig.suptitle('O QUE O MUNDO QUEIMA vs O QUE O BRASIL USA\nO Contraste do Carvão Mineral e do Gás Natural na Eletricidade', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.96)
    
    # Gráfico 1: Carvão Mineral
    bars1 = ax1.bar(['Mundo\n(Maior fonte global!)', 'Brasil\n(Menos de 2%)'], [35.4, 1.8], 
                    color=[ACCENT_CORAL, ACCENT_GREEN], width=0.45, edgecolor='#2C3A47', lw=2)
    ax1.set_title('Participação do Carvão Mineral na Eletricidade', fontsize=15, color=TEXT_MAIN, pad=15)
    ax1.set_ylabel('% da Matriz Elétrica', color=TEXT_MUTED, fontsize=13)
    ax1.set_ylim(0, 45)
    ax1.set_facecolor(CARD_COLOR)
    ax1.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax1.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars1:
        yval = b.get_height()
        ax1.text(b.get_x() + b.get_width()/2.0, yval + 1.0, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')
    ax1.text(0.5, 0.65, 'O carvão é a fonte mais poluente\ne gera 35% de toda a luz do mundo!', ha='center', va='center', 
             transform=ax1.transAxes, fontsize=13, color=TEXT_MAIN,
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#0E141B', edgecolor=ACCENT_CORAL, lw=1.5))
        
    # Gráfico 2: Gás Natural Fóssil
    bars2 = ax2.bar(['Mundo\n(2ª maior fonte)', 'Brasil\n(Apenas apoio térmico)'], [22.7, 7.5], 
                    color=['#E17055', ACCENT_GREEN], width=0.45, edgecolor='#2C3A47', lw=2)
    ax2.set_title('Participação do Gás Natural na Eletricidade', fontsize=15, color=TEXT_MAIN, pad=15)
    ax2.set_ylabel('% da Matriz Elétrica', color=TEXT_MUTED, fontsize=13)
    ax2.set_ylim(0, 30)
    ax2.set_facecolor(CARD_COLOR)
    ax2.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF')
    ax2.tick_params(colors=TEXT_MUTED, labelsize=12)
    for b in bars2:
        yval = b.get_height()
        ax2.text(b.get_x() + b.get_width()/2.0, yval + 0.8, f'{yval:.1f}%', ha='center', 
                 color=TEXT_MAIN, fontsize=16, fontweight='bold')

    fig.text(0.5, 0.04, 'Fontes: International Energy Agency (IEA) & EPE | Canal Gráfico Aberto', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-003/assets/scene3.png')

# ==========================================
# CENA 4: Painel Estratégico e Conclusão
# ==========================================
def make_scene4():
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    fig.suptitle('3 PONTOS ESTRATÉGICOS DA ENERGIA NO BRASIL', 
                 fontsize=22, fontweight='bold', color=TEXT_MAIN, y=0.92)
    
    cards = [
        ("1. VANTAGEM COMPETITIVA", 
         "• 88% da eletricidade renovável atrai indústrias verdes\n• Pegada de carbono industrial muito inferior a EUA e China\n• Potencial gigantesco para produção de hidrogênio verde", 
         0.12, ACCENT_GREEN),
        ("2. O DESAFIO CLIMÁTICO", 
         "• Dependência de 58% de rios exige gestão de reservatórios\n• Períodos de seca severa exigem acionamento de térmicas caras\n• Eólica e solar compensam a variabilidade hídrica", 
         0.42, ACCENT_BLUE),
        ("3. ELETRICIDADE vs TRANSPORTE", 
         "• Na tomada somos 88% limpos, mas nos carros usamos petróleo\n• O etanol e o biodiesel elevam nossa matriz geral para 48%\n• A média mundial da energia total é de apenas 15% renovável", 
         0.72, ACCENT_YELLOW)
    ]
    
    for title, content, xpos, color in cards:
        rect = plt.Rectangle((xpos, 0.20), 0.24, 0.58, facecolor='#111A24', edgecolor=color, linewidth=2.5, 
                             transform=fig.transFigure, zorder=2)
        fig.patches.append(rect)
        fig.text(xpos + 0.02, 0.73, title, fontsize=15, fontweight='bold', color=color, transform=fig.transFigure)
        fig.text(xpos + 0.02, 0.46, content, fontsize=12, color=TEXT_MAIN, transform=fig.transFigure, linespacing=1.8)

    fig.text(0.5, 0.10, 'Canal Gráfico Aberto | A realidade explicada através dos dados oficiais', 
             ha='center', fontsize=14, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.05, 'Fontes: Empresa de Pesquisa Energética (EPE/BEN) / IEA / ONS', 
             ha='center', fontsize=12, color=TEXT_MUTED)
    save_fig(fig, 'videos/PILOTO-003/assets/scene4.png')

# ==========================================
# MINIATURA (THUMBNAIL) 1280x720
# ==========================================
def make_thumbnail():
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100, facecolor=BG_COLOR)
    ax.set_facecolor(CARD_COLOR)
    ax.axis('off')
    
    fig.text(0.08, 0.80, 'DE ONDE VEM NOSSA ENERGIA?', fontsize=32, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.08, 0.70, 'Brasil tem 88% renovável. E o resto do mundo?', fontsize=20, color=TEXT_MAIN)
    
    # Gráfico miniatura
    sub_ax = fig.add_axes([0.08, 0.16, 0.45, 0.44], facecolor='#111A24')
    sub_ax.bar(['Mundo', 'Brasil'], [30.2, 87.9], color=['#576574', ACCENT_GREEN], width=0.45)
    sub_ax.set_title('Eletricidade Renovável (%)', fontsize=13, color=TEXT_MUTED)
    sub_ax.set_ylim(0, 105)
    sub_ax.tick_params(colors=TEXT_MUTED, labelsize=11)
    sub_ax.text(0, 32, '30.2%', ha='center', color=TEXT_MAIN, fontsize=14, fontweight='bold')
    sub_ax.text(1, 90, '87.9%', ha='center', color=ACCENT_GREEN, fontsize=14, fontweight='bold')
    sub_ax.grid(axis='y', linestyle=':', alpha=0.3, color='#FFF')
    
    # Card de impacto
    card_box = plt.Rectangle((0.58, 0.16), 0.34, 0.44, facecolor='#111A24', edgecolor=ACCENT_GREEN, linewidth=3, 
                             transform=fig.transFigure)
    fig.patches.append(card_box)
    fig.text(0.75, 0.48, 'BRASIL LIMPO', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.75, 0.34, 'QUASE 3X', ha='center', fontsize=38, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.75, 0.22, 'Mais limpo que a média global', ha='center', fontsize=14, color=TEXT_MAIN)
    
    fig.text(0.92, 0.90, 'GRÁFICO ABERTO', ha='right', fontsize=14, fontweight='bold', color=TEXT_MUTED)

    fig.patch.set_facecolor(BG_COLOR)
    plt.savefig('videos/PILOTO-003/export/thumbnail.png', facecolor=BG_COLOR, edgecolor='none')
    plt.close(fig)
    print("Salvo: videos/PILOTO-003/export/thumbnail.png")

make_scene1()
make_scene2()
make_scene3()
make_scene4()
make_thumbnail()
