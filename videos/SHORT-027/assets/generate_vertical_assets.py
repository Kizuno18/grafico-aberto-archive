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
# CENA 1: Gancho - Dependência do Caminhão
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'TRANSPORTE DE CARGA (CNT)', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A DEPENDÊNCIA DO ASFALTO', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Por que quase tudo vem de caminhão?', ha='center', fontsize=22, color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'CARGA TOTAL TRANSPORTADA NO PAÍS', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '65%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Dois terços de toda a carga roda em rodovias!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Boletim CNT do Transporte', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-027/assets/scene1.png')

# ==========================================
# CENA 2: Divisão dos Modais
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'MATRIZ DE CARGA NO BRASIL (CNT)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'COMO A CARGA SE MOVE?', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    modais = ['Dutoviário', 'Aquaviário', 'Ferroviário', 'Rodoviário']
    shares = [4.0, 11.0, 15.0, 65.0]
    colors = [ACCENT_YELLOW, ACCENT_CYAN, ACCENT_BLUE, ACCENT_CORAL]
    bars = sub_ax.barh(modais, shares, color=colors, height=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_xlim(0, 78)
    sub_ax.set_xlabel('% da Carga Nacional (TKU)', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='x', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=12)
    for b in bars:
        wval = b.get_width()
        sub_ax.text(wval + 1.5, b.get_y() + b.get_height()/2.0, f'{wval:.0f}%', va='center', 
                    color=TEXT_MAIN, fontsize=16, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Nos EUA, ferrovias transportam mais de 40%!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Brasil tem pouca integração multimodal', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: CNT / EPL | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-027/assets/scene2.png')

# ==========================================
# CENA 3: Eficiência / CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CUSTO E EFICIÊNCIA ENERGÉTICA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O PESO NO FRETE', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'TRENS EM LONGAS DISTÂNCIAS', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '4x MAIS', ha='center', fontsize=56, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.50, 'Eficientes em combustível por tonelada!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-027/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
