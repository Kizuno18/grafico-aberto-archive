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
    print(f'Salvo: {path}')

def make_scene1():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'APOSTAS ELETRÔNICAS (BANCO CENTRAL)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A EXPLOSÃO DAS BETS', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O volume assustador via Pix no Brasil', ha='center', fontsize=22, color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'VOLUME TRANSFERIDO POR MÊS VIA PIX', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'R$ 20 BI / MÊS', ha='center', fontsize=54, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.44, 'Cerca de R$ 240 bilhões por ano drenados!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Nota Técnica sobre Apostas — Banco Central', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-102/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'RAIO-X DOS APOSTADORES (BCB/CNC)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, '24 MILHÕES DE PESSOAS / MÊS', ha='center', fontsize=30, fontweight='bold', color=ACCENT_YELLOW)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    indicadores = ['Apostadores\n(Milhões/Mês)', 'Bolsa Família\n(Milhões Apos.)', 'Impacto Varejo\n(R$ Bi/Ano)']
    valores = [24.0, 5.0, 100.0]
    colors = [ACCENT_CORAL, ACCENT_YELLOW, ACCENT_BLUE]
    bars = sub_ax.bar(indicadores, valores, color=colors, width=0.50, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 120)
    sub_ax.set_ylabel('Escala e Valores', color=TEXT_MUTED, fontsize=11)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=10)
    
    sub_ax.text(bars[0].get_x() + bars[0].get_width()/2.0, 24 + 3, '24M pessoas', ha='center', color=TEXT_MAIN, fontsize=12, fontweight='bold')
    sub_ax.text(bars[1].get_x() + bars[1].get_width()/2.0, 5 + 3, '5M benef.', ha='center', color=TEXT_MAIN, fontsize=12, fontweight='bold')
    sub_ax.text(bars[2].get_x() + bars[2].get_width()/2.0, 100 + 3, '- R$ 100 Bi', ha='center', color=TEXT_MAIN, fontsize=12, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Dinheiro drenado de supermercados, farmácias e comércio!', ha='center', fontsize=15, fontweight='bold', color=ACCENT_YELLOW)
    fig.text(0.5, 0.28, '5 milhões de beneficiários do Bolsa Família transferiram R$ 3 bi/mês', ha='center', fontsize=12, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Análises Técnicas BCB / CNC | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-102/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ENDIVIDAMENTO E RISCO SOCIAL', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O ALERTA DA INADIMPLÊNCIA', ha='center', fontsize=32, fontweight='bold', color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'BRASILEIROS NEGATIVADOS POR BETS', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '+ 1,3 MILHÃO', ha='center', fontsize=50, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.50, 'Regulação urgente e impacto na economia popular!', ha='center', fontsize=14, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-102/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
