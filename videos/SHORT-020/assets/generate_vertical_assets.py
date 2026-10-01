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
# CENA 1: Gancho Ferrovias Brasileiras
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'INFRAESTRUTURA EM DADOS', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O QUE HOUVE COM OS TRENS?', ha='center', fontsize=32, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Por que o Brasil quase não tem ferrovias?', ha='center', fontsize=20, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'EXTENSÃO DA MALHA FERROVIÁRIA', ha='center', fontsize=17, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '30 MIL KM', ha='center', fontsize=56, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'A mesma extensão da década de 1950!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fontes: ANTT & Ministério dos Transportes', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-020/assets/scene1.png')

# ==========================================
# CENA 2: Comparativo Internacional de Trilhos
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'MALHA FERROVIÁRIA (MIL KM)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'BRASIL vs GIGANTES GLOBAIS', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    countries = ['Brasil', 'Rússia', 'China', 'EUA']
    vals = [30.5, 85.0, 150.0, 250.0]
    colors = [ACCENT_CORAL, ACCENT_CYAN, ACCENT_BLUE, ACCENT_GREEN]
    bars = sub_ax.bar(countries, vals, color=colors, width=0.55, edgecolor='#2C3A47', lw=2)
    sub_ax.set_ylim(0, 290)
    sub_ax.set_ylabel('Extensão (mil km)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=14)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 6, f'{int(yval)}k', ha='center', 
                    color=TEXT_MAIN, fontsize=16, fontweight='bold')
        
    fig.text(0.5, 0.34, 'Mais de 75% da carga é minério de ferro!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.29, 'E só existem 2 linhas regulares de passageiros', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: ANTT & Banco Mundial | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-020/assets/scene2.png')

# ==========================================
# CENA 3: O Peso das Rodovias e Conclusão
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A MATRIZ DE CARGAS NACIONAL', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DEPENDÊNCIA DO ASFALTO', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'CARGA TRANSPORTADA POR CAMINHÃO', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '~65%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.50, 'Encarecendo o frete, comida e combustíveis', ha='center', fontsize=16, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-020/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
