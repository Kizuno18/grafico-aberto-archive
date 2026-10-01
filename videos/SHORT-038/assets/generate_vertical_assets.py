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
ACCENT_YELLOW = '#FDCB6E'
ACCENT_CORAL = '#FF5A5F'

def save_vertical(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', dpi=100)
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gancho - O Salto do E-commerce
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'VAREJO & INTERNET (ABCOMM)', ha='center', fontsize=23, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A EXPLOSÃO DO E-COMMERCE', ha='center', fontsize=33, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Como compramos mudou para sempre', ha='center', fontsize=22, color=ACCENT_BLUE)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'FATURAMENTO DO COMÉRCIO ELETRÔNICO', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'R$ 200 BI', ha='center', fontsize=60, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.44, 'Quase triplicou de tamanho em apenas 5 anos!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: ABComm / Ebit|Nielsen / IBGE', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-038/assets/scene1.png')

# ==========================================
# CENA 2: Trajetória do Faturamento
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'FATURAMENTO ANUAL (R$ BILHÕES)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DE R$ 75 BI A MAIS DE R$ 200 BI', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    anos = ['2019', '2020', '2022', '2024*']
    faturamento = [75.1, 126.3, 169.6, 204.0]
    colors = ['#7F8C8D', ACCENT_YELLOW, ACCENT_CYAN, ACCENT_GREEN]
    bars = sub_ax.bar(anos, faturamento, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 240)
    sub_ax.set_ylabel('R$ Bilhões no Ano', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=12)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 5, f'R$ {yval:.0f}B', ha='center', 
                    color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    fig.text(0.5, 0.33, 'E-commerce já é mais de 10% do varejo!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Em eletrônicos e informática passa de 40%', ha='center', fontsize=14, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Relatório Webshoppers | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-038/assets/scene2.png')

# ==========================================
# CENA 3: Compradores Ativos e CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'POPULAÇÃO CONECTADA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUASE METADE DO BRASIL', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'COMPRADORES VIRTUAIS ATIVOS', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '> 87 MI', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.50, 'Mais de 65% das compras pelo celular!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-038/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
