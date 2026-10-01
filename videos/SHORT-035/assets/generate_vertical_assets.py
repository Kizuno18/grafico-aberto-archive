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
# CENA 1: Gancho - Queda dos Assassinatos
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'SEGURANÇA PÚBLICA (IPEA/FBSP)', ha='center', fontsize=23, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A QUEDA DOS HOMICÍDIOS', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O que os dados oficiais revelam?', ha='center', fontsize=22, color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'REDUÇÃO EM RELAÇÃO AO PICO DE 2017', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '- 35%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.44, 'Menor número de mortes em mais de 10 anos no país', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Atlas da Violência — IPEA / FBSP', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-035/assets/scene1.png')

# ==========================================
# CENA 2: Trajetória da Taxa por 100k
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'HOMICÍDIOS POR 100 MIL HABITANTES', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DO PICO HISTÓRICO AO RECUO', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    anos = ['2017 (Pico)', '2019', '2022', 'Atual']
    taxas = [31.6, 21.7, 21.2, 21.0]
    colors = [ACCENT_CORAL, ACCENT_YELLOW, ACCENT_BLUE, ACCENT_GREEN]
    bars = sub_ax.bar(anos, taxas, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 36)
    sub_ax.set_ylabel('Taxa por 100 mil hab.', color=TEXT_MUTED, fontsize=12)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 0.8, f'{yval:.1f}', ha='center', 
                    color=TEXT_MAIN, fontsize=15, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Em 2017 foram mais de 65 mil mortes!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_CORAL)
    fig.text(0.5, 0.28, 'Taxa atual recuou para o patamar de ~21 por 100k', ha='center', fontsize=14, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: IPEA / FBSP | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-035/assets/scene2.png')

# ==========================================
# CENA 3: Abismo Regional e CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'CONTRASTES REGIONAIS', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'DISPARIDADE BRUTAL', ha='center', fontsize=34, fontweight='bold', color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'SÃO PAULO (<7) vs NORTE/NORDESTE (>35)', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '5x DIFERENÇA', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_YELLOW)
    fig.text(0.5, 0.50, 'Violência ainda é crítica em vários estados!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-035/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
