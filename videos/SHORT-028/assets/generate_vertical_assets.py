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
# CENA 1: Gancho - A Transição Religiosa
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO (IBGE)', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A TRANSIÇÃO RELIGIOSA', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, '40 anos de mudanças profundas', ha='center', fontsize=22, color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'MUDANÇA RELIGIOSA MAIS RÁPIDA DO OCIDENTE', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '89%  ➔  52%', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.44, 'A proporção de católicos no Brasil de 1980 a hoje', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Séries Históricas dos Censos — IBGE', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-028/assets/scene1.png')

# ==========================================
# CENA 2: Comparação 1980 vs Atual
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO (IBGE)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'COMO ERA E COMO ESTÁ HOJE', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    grupos = ['Católicos', 'Evangélicos', 'Sem Religião']
    val_1980 = [89.0, 6.6, 1.6]
    val_atual = [52.0, 31.0, 10.0]
    
    x = np.arange(len(grupos))
    w = 0.35
    b1 = sub_ax.bar(x - w/2, val_1980, width=w, label='1980', color=ACCENT_BLUE, edgecolor='#2C3A47')
    b2 = sub_ax.bar(x + w/2, val_atual, width=w, label='Atual (IBGE)', color=ACCENT_GREEN, edgecolor='#2C3A47')
    
    sub_ax.set_xticks(x)
    sub_ax.set_xticklabels(grupos, color=TEXT_MAIN, fontsize=12, fontweight='bold')
    sub_ax.set_ylim(0, 105)
    sub_ax.set_ylabel('% da População', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.legend(facecolor='#141D28', edgecolor='none', labelcolor=TEXT_MAIN, fontsize=11)
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    
    for b in b1:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 2, f'{yval:.0f}%', ha='center', color=TEXT_MAIN, fontsize=12, fontweight='bold')
    for b in b2:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 2, f'{yval:.0f}%', ha='center', color=TEXT_MAIN, fontsize=12, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Evangélicos saltaram de 7% para mais de 30%!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Participação quadruplicou em 4 décadas', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Censos Demográficos | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-028/assets/scene2.png')

# ==========================================
# CENA 3: Sem Religião / CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CENSO DEMOGRÁFICO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O AVANÇO DOS SEM RELIGIÃO', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'POPULAÇÃO SEM RELIGIÃO DECLARADA', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '2%  ➔  10%', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.50, 'Mais de 20 milhões de pessoas hoje!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-028/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
