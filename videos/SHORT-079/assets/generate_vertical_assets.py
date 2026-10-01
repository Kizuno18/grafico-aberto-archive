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
    
    fig.text(0.5, 0.88, 'CRIPTOATIVOS NO BRASIL (RECEITA FEDERAL)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A EXPLOSÃO DO CRIPTO', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O dinheiro declarado nas corretoras', ha='center', fontsize=22, color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'VOLUME DECLARADO POR ANO', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'R$ 200 BI', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_YELLOW)
    fig.text(0.5, 0.44, 'Mas o líder absoluto NÃO é o Bitcoin!', ha='center', fontsize=18, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Relatórios de Criptoativos — Receita Federal', ha='center', fontsize=16, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-079/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'PARTICIPAÇÃO NO VOLUME FINANCEIRO (RFB)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O DOMÍNIO DO TETHER (USDT)', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    moedas = ['Tether (USDT)', 'Bitcoin', 'Ethereum', 'Outros']
    fatias = [80.0, 12.0, 4.0, 4.0]
    colors = [ACCENT_GREEN, ACCENT_YELLOW, ACCENT_BLUE, TEXT_MUTED]
    bars = sub_ax.bar(moedas, fatias, color=colors, width=0.55, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 100)
    sub_ax.set_ylabel('Volume Negociado (%)', color=TEXT_MUTED, fontsize=11)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=10)
    for b in bars:
        yval = b.get_height()
        sub_ax.text(b.get_x() + b.get_width()/2.0, yval + 2, f'{yval:.0f}%', ha='center', 
                    color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    fig.text(0.5, 0.33, '8 de cada 10 reais vão para o dólar digital (USDT)!', ha='center', fontsize=16, fontweight='bold', color=ACCENT_GREEN)
    fig.text(0.5, 0.28, 'Brasileiro usando cripto para se proteger da inflação', ha='center', fontsize=13, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Estatísticas IN 1.888 / RFB | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-079/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'ADOÇÃO NO BRASIL (CHAINALYSIS)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'BASE DE INVESTIDORES', ha='center', fontsize=33, fontweight='bold', color=ACCENT_CYAN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CYAN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'PESSOAS FÍSICAS DECLARANTES', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '4,8 MILHÕES', ha='center', fontsize=48, fontweight='heavy', color=ACCENT_CYAN)
    fig.text(0.5, 0.50, 'Brasil consolidado no Top 10 global de adoção!', ha='center', fontsize=15, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-079/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
