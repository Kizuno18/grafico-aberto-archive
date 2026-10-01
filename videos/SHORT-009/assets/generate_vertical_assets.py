import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

BG_COLOR = '#0B0F15'
CARD_COLOR = '#141D28'
TEXT_MAIN = '#F0F4F8'
TEXT_MUTED = '#8B9BAE'
ACCENT_GREEN = '#00D287'
ACCENT_BLUE = '#2E86DE'
ACCENT_CYAN = '#00CEC9'
ACCENT_CORAL = '#FF5A5F'

def save_vertical(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', dpi=100)
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gancho Produtividade
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'POR QUE O SALÁRIO É BAIXO?', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'A armadilha da produtividade no Brasil', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'HORAS TRABALHADAS vs VALOR GERADO', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '4x MENOS', ha='center', fontsize=56, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Valor gerado por hora em relação aos EUA', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fontes: The Conference Board & IPEA', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-009/assets/scene1.png')

# ==========================================
# CENA 2: Gráfico Comparativo de Produtividade
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'VALOR GERADO POR HORA TRABALHADA', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'PRODUTIVIDADE DO TRABALHO', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    countries = ['Brasil', 'Coreia do Sul', 'Alemanha', 'EUA']
    vals = [20.0, 49.0, 78.0, 87.0]
    colors = [ACCENT_CORAL, ACCENT_CYAN, ACCENT_BLUE, ACCENT_GREEN]
    bars = sub_ax.bar(countries, vals, color=colors, width=0.55, edgecolor='#2C3A47', lw=2)
    sub_ax.set_ylim(0, 105)
    sub_ax.set_ylabel('Dólares PPC por Hora (US$)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=14)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 2, f'US$ {int(yval)}', ha='center', 
                    color=TEXT_MAIN, fontsize=16, fontweight='bold')
        
    fig.text(0.5, 0.33, 'EUA geram US$ 87/h contra US$ 20/h no Brasil!', ha='center', fontsize=19, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'O trabalhador americano produz em 1h o que fazemos em 4h', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: The Conference Board Total Economy Database', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-009/assets/scene2.png')

# ==========================================
# CENA 3: A Causa Real (Estrutural)
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'POR QUE PRODUZIMOS MENOS?', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'NÃO É FALTA DE ESFORÇO!', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CORAL)
    
    # 3 Cards diagnósticos
    points = [
        ("FALTA DE TECNOLOGIA", "Menos máquinas modernas e automação na indústria", ACCENT_BLUE, 0.65),
        ("INFRAESTRUTURA RUIM", "Estradas e portos encarecem e atrasam a produção", ACCENT_CORAL, 0.51),
        ("BAIXO INVESTIMENTO", "A taxa de investimento do Brasil é de apenas ~17% do PIB", ACCENT_CYAN, 0.37)
    ]
    for tag, desc, col, ypos in points:
        box = plt.Rectangle((0.12, ypos), 0.76, 0.11, facecolor=CARD_COLOR, edgecolor=col, 
                            linewidth=2.5, transform=fig.transFigure, zorder=2)
        fig.patches.append(box)
        fig.text(0.16, ypos + 0.07, tag, fontsize=15, fontweight='bold', color=col)
        fig.text(0.16, ypos + 0.03, desc, fontsize=15, color=TEXT_MAIN)
        
    # CTA Card
    cta_box = plt.Rectangle((0.12, 0.18), 0.76, 0.13, facecolor='#111A24', edgecolor=ACCENT_GREEN, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.26, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.21, 'Inscreva-se para ver a realidade dos dados', ha='center', fontsize=15, color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-009/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
