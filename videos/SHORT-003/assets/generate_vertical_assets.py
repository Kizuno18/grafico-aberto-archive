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
# CENA 1: Gancho 88% Renovável
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'BRASIL vs MUNDO', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DE ONDE VEM NOSSA LUZ?', ha='center', fontsize=36, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O gráfico que surpreende o planeta', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'ENERGIA RENOVÁVEL NO BRASIL', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.53, '87,9%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.42, 'Quase 9 de cada 10 lâmpadas são limpas', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fontes: Empresa de Pesquisa Energética (EPE/BEN)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-003/assets/scene1.png')

# ==========================================
# CENA 2: O Choque com o Resto do Mundo
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'MATRIZ ELÉTRICA COMPARADA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'BRASIL vs MÉDIA MUNDIAL', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CYAN)
    
    # Gráfico de barras vertical
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    bars = sub_ax.bar(['Mundo\n(Global)', 'Brasil\n(Nacional)'], [30.2, 87.9], 
                      color=['#576574', ACCENT_GREEN], width=0.50, edgecolor='#233244', lw=2)
    sub_ax.set_ylim(0, 105)
    sub_ax.set_ylabel('% Renovável na Eletricidade', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=16)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 2, f'{yval:.1f}%', ha='center', 
                    color=TEXT_MAIN, fontsize=20, fontweight='bold')
        
    fig.text(0.5, 0.33, 'O mundo ainda queima 35% de CARVÃO!', ha='center', fontsize=20, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'E mais de 22% de gás fóssil para gerar luz', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fontes: IEA (Agência Internacional) & EPE', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-003/assets/scene2.png')

# ==========================================
# CENA 3: Conclusão e CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'VANTAGEM BRASILEIRA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUASE 3X MAIS LIMPO', ha='center', fontsize=36, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'ÁGUA, VENTO, SOL E CANA', ha='center', fontsize=17, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, '1/3 DA LUZ', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.52, 'Já vem de novas renováveis (vento + sol)', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'VÍDEO COMPLETO NO CANAL', ha='center', fontsize=20, fontweight='bold', color=ACCENT_BLUE)
    fig.text(0.5, 0.31, 'Entenda a nossa matriz elétrica com dados completos', ha='center', fontsize=14, color=TEXT_MAIN)
    fig.text(0.5, 0.27, '@ograficoaberto | Gráfico Aberto', ha='center', fontsize=16, fontweight='bold', color=TEXT_MAIN)
    
    save_vertical(fig, 'videos/SHORT-003/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
