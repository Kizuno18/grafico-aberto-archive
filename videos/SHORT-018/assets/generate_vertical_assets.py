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
# CENA 1: Gancho Reservas Cambiais
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O COFRE DO BRASIL', ha='center', fontsize=36, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'Por que guardamos tantos dólares?', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'RESERVAS INTERNACIONAIS (BACEN)', ha='center', fontsize=17, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'US$ 355 BI', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.44, 'Mais de 1,8 trilhão de reais em reservas!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Banco Central do Brasil (Série 3546)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-018/assets/scene1.png')

# ==========================================
# CENA 2: Gráfico Histórico das Reservas
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'HISTÓRICO DE 30 ANOS', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DE US$ 10 BI A US$ 355 BI', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    years = ['1990', '1998', '2005', '2012', '2020', 'Hoje']
    res_vals = [10.0, 44.0, 53.0, 370.0, 355.0, 355.0]
    sub_ax.plot(years, res_vals, marker='o', linewidth=3.5, markersize=10, color=ACCENT_GREEN)
    sub_ax.fill_between(years, res_vals, color=ACCENT_GREEN, alpha=0.15)
    sub_ax.set_ylim(0, 420)
    sub_ax.set_ylabel('Bilhões de Dólares (US$)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(True, linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=13)
    for i, v in enumerate(res_vals):
        sub_ax.text(i, v + 14, f'{int(v)}', ha='center', color=TEXT_MAIN, fontsize=14, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Garante mais de 1 ano de todas as importações!', ha='center', fontsize=17, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Em 1990 vivíamos em crise de liquidez externa', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Banco Central do Brasil | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-018/assets/scene2.png')

# ==========================================
# CENA 3: O Que Esse Dinheiro Faz
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'PARA QUE SERVE O COFRE?', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O ESCUDO DO BRASIL', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CYAN)
    
    # 3 Cards explicativos
    points = [
        ("BLINDAGEM CAMBIAL", "Evita corridas especulativas contra o Real", ACCENT_GREEN, 0.65),
        ("PAGAMENTO GARANTIDO", "Assegura importação de petróleo, remédios e trigo", ACCENT_BLUE, 0.51),
        ("CREDOR INTERNACIONAL", "O Brasil não depende mais de socorro do FMI", ACCENT_CYAN, 0.37)
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
    
    save_vertical(fig, 'videos/SHORT-018/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
