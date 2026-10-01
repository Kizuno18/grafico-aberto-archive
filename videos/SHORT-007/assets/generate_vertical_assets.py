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
ACCENT_CORAL = '#FF5A5F'

def save_vertical(fig, path):
    fig.patch.set_facecolor(BG_COLOR)
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.savefig(path, facecolor=BG_COLOR, edgecolor='none', dpi=100)
    plt.close(fig)
    print(f"Salvo: {path}")

# ==========================================
# CENA 1: Gancho Salário Mínimo e Inflação
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'E SE NÃO HOUVESSE GANHO REAL?', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O salário mínimo corrigido só pela inflação', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'SE ACOMPANHASSE APENAS O IPCA', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'R$ 577,00', ha='center', fontsize=54, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Seria o valor do salário mínimo hoje!', ha='center', fontsize=20, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Banco Central do Brasil (SGS 433)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-007/assets/scene1.png')

# ==========================================
# CENA 2: Comparativo Inflação vs Realidade
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'EVOLUÇÃO REAL DESDE 1994', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUANTO O MÍNIMO SUBIU?', ha='center', fontsize=36, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    labels = ['Só Inflação\n(IPCA)', 'Salário Atual\n(Oficial)']
    vals = [577, 1621]
    bars = sub_ax.bar(labels, vals, color=['#576574', ACCENT_GREEN], width=0.48, edgecolor='#2C3A47', lw=2)
    sub_ax.set_ylim(0, 1950)
    sub_ax.set_ylabel('Valor em Reais (R$)', color=TEXT_MUTED, fontsize=13)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=16)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 40, f'R$ {yval}', ha='center', 
                    color=TEXT_MAIN, fontsize=18, fontweight='bold')
        
    fig.text(0.5, 0.33, '+181% DE GANHO REAL ACIMA DA INFLAÇÃO!', ha='center', fontsize=18, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Em 1994: R$ 64,79 | Inflação acumulada: 8,9 vezes', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fontes: BACEN Séries 1619 e 433 | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-007/assets/scene2.png')

# ==========================================
# CENA 3: Conclusão e CTA
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'PODER DE COMPRA DO TRABALHADOR', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUASE TRIPLICOU', ha='center', fontsize=38, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'CRESCIMENTO REAL EM 32 ANOS', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '2,8 VEZES', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.50, 'Mais poder de compra que em julho de 1994', ha='center', fontsize=17, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-007/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
