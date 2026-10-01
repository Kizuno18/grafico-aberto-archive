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
# CENA 1: Gancho - A Invasão Elétrica
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'MERCADO AUTOMOTIVO (ABVE)', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A INVASÃO ELÉTRICA', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O salto dos eletrificados no Brasil', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'CRESCIMENTO DE VENDAS (2020 a 2024)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '+ 700%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.44, 'Vendas multiplicaram por quase 8 vezes em 4 anos!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Associação Brasileira do Veículo Elétrico', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-033/assets/scene1.png')

# ==========================================
# CENA 2: Evolução das Vendas Anuais
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'VENDAS DE VEÍCULOS ELETRIFICADOS (ABVE)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'CRESCIMENTO EXPONENCIAL', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    anos = ['2020', '2022', '2023', '2024*']
    vendas = [19.7, 49.2, 93.8, 155.0]
    colors = [ACCENT_BLUE, ACCENT_YELLOW, ACCENT_CYAN, ACCENT_GREEN]
    bars = sub_ax.bar(anos, vendas, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 180)
    sub_ax.set_ylabel('Milhares de Unidades / Ano', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=12)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 3.5, f'{yval:.0f} mil', ha='center', 
                    color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Eletrificados já são ~8% dos carros novos no país!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Impulsionados por híbridos plug-in e 100% elétricos', ha='center', fontsize=14, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: ABVE / Anfavea | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-033/assets/scene2.png')

# ==========================================
# CENA 3: Frota Total e CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'FROTA TOTAL DE ELETRIFICADOS', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A MARCA DOS 300 MIL', ha='center', fontsize=34, fontweight='bold', color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'FROTA CIRCULANTE NO BRASIL', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '> 300 MIL', ha='center', fontsize=60, fontweight='heavy', color=ACCENT_YELLOW)
    fig.text(0.5, 0.50, 'Mais de 4.500 eletropostos instalados!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-033/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
