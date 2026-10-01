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
# CENA 1: Gancho R$ 100 = R$ 11,23
# ==========================================
def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ECONOMIA EM DADOS', ha='center', fontsize=24, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUANTO VALE R$ 100?', ha='center', fontsize=38, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O impacto de 32 anos de inflação', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    # Card Central
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'PODER DE COMPRA REAL DE R$ 100', ha='center', fontsize=18, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.30, 0.54, '1994\nR$ 100', ha='center', fontsize=28, fontweight='bold', color=ACCENT_BLUE)
    fig.text(0.50, 0.54, '➔', ha='center', fontsize=36, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.70, 0.54, 'Hoje\nR$ 11,23', ha='center', fontsize=28, fontweight='bold', color=ACCENT_CORAL)
    
    fig.text(0.5, 0.42, 'PERDA DE 88,8% DO VALOR REAL', ha='center', fontsize=20, fontweight='bold', color=ACCENT_CORAL)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Banco Central do Brasil (IPCA)', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-002/assets/scene1.png')

# ==========================================
# CENA 2: O Que Comprava em 1994
# ==========================================
def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'JULHO DE 1994 (ESTREIA DO REAL)', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O QUE UMA NOTA PAGAVA?', ha='center', fontsize=38, fontweight='bold', color=ACCENT_GREEN)
    
    # 2 Cards Grandes
    c1 = plt.Rectangle((0.12, 0.56), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c1)
    fig.text(0.5, 0.71, 'SALÁRIO MÍNIMO DA ÉPOCA', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.65, 'R$ 64,79', ha='center', fontsize=34, fontweight='bold', color=ACCENT_BLUE)
    fig.text(0.5, 0.59, '1 nota de R$ 100 pagava 1,5 salário mínimo!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    c2 = plt.Rectangle((0.12, 0.32), 0.76, 0.20, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                       linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(c2)
    fig.text(0.5, 0.47, 'CESTA BÁSICA DO DIEESE (SP)', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.41, 'R$ 64,30', ha='center', fontsize=34, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.35, '1 nota de R$ 100 pagava 1,5 cesta básica inteira!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    fig.text(0.5, 0.22, 'Fontes: DIEESE & Diário Oficial da União | Gráfico Aberto', ha='center', fontsize=15, color=TEXT_MUTED)
    save_vertical(fig, 'videos/SHORT-002/assets/scene2.png')

# ==========================================
# CENA 3: O Que Precisa Hoje e Conclusão
# ==========================================
def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A INFLAÇÃO ACUMULADA', ha='center', fontsize=22, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'QUANTO VOCÊ PRECISA HOJE?', ha='center', fontsize=36, fontweight='bold', color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'PARA COMPRAR O MESMO DE R$ 100 DE 1994', ha='center', fontsize=16, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.60, 'R$ 890,00', ha='center', fontsize=52, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.52, 'Multiplicou por quase 9 vezes (+790%)', ha='center', fontsize=18, color=TEXT_MAIN)
    
    # CTA Card
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'VÍDEO COMPLETO NO CANAL', ha='center', fontsize=20, fontweight='bold', color=ACCENT_BLUE)
    fig.text(0.5, 0.31, 'Veja a análise histórica completa com todos os dados', ha='center', fontsize=14, color=TEXT_MAIN)
    fig.text(0.5, 0.27, '@ograficoaberto | Gráfico Aberto', ha='center', fontsize=16, fontweight='bold', color=TEXT_MAIN)
    
    save_vertical(fig, 'videos/SHORT-002/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
