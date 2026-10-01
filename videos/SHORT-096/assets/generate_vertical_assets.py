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
    
    fig.text(0.5, 0.88, 'VAREJO & LAZER (CENSO ABRASCE)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A FORÇA DOS SHOPPINGS', ha='center', fontsize=32, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O sucesso dos centros comerciais no Brasil', ha='center', fontsize=21, color=ACCENT_YELLOW)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_YELLOW, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'FATURAMENTO ANUAL CONSOLIDADO', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, 'R$ 195 BI', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_YELLOW)
    fig.text(0.5, 0.44, 'Mais de 115 mil lojas e 1,1 milhão de empregos!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Associação Brasileira de Shopping Centers — Abrasce', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-096/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'FLUXO E OPERAÇÃO NACIONAL (ABRASCE)', ha='center', fontsize=19, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, '440 MILHÕES DE VISITAS/MÊS', ha='center', fontsize=30, fontweight='bold', color=ACCENT_CYAN)
    
    sub_ax = fig.add_axes([0.15, 0.40, 0.70, 0.32], facecolor=CARD_COLOR)
    indicadores = ['Shoppings\nAtivos', 'Área Locável\n(Milhões m²)', 'Visitas/Mês\n(Dezenas Mi)']
    valores = [640, 17.8, 44.0]
    colors = [ACCENT_BLUE, ACCENT_YELLOW, ACCENT_GREEN]
    bars = sub_ax.bar(indicadores, valores, color=colors, width=0.50, edgecolor='#2C3A47', lw=1.5)
    sub_ax.set_ylim(0, 750)
    sub_ax.set_ylabel('Escala Operacional', color=TEXT_MUTED, fontsize=11)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=10)
    
    sub_ax.text(bars[0].get_x() + bars[0].get_width()/2.0, 640 + 15, '640 un', ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
    sub_ax.text(bars[1].get_x() + bars[1].get_width()/2.0, 17.8 + 15, '17,8M m²', ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
    sub_ax.text(bars[2].get_x() + bars[2].get_width()/2.0, 44.0 + 15, '440M visitas', ha='center', color=TEXT_MAIN, fontsize=13, fontweight='bold')
        
    fig.text(0.5, 0.33, 'Mais de 14 milhões de visitantes por dia no país!', ha='center', fontsize=16, fontweight='bold', color=ACCENT_YELLOW)
    fig.text(0.5, 0.28, 'Ao contrário dos EUA, shoppings no Brasil continuam crescendo', ha='center', fontsize=13, color=TEXT_MUTED)
    fig.text(0.5, 0.22, 'Fonte: Censo Brasileiro de Shopping Centers | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-096/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'O DIFERENCIAL BRASILEIRO (ABRASCE)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'POLO DE SERVIÇO & LAZER', ha='center', fontsize=32, fontweight='bold', color=ACCENT_GREEN)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_GREEN, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'TRANSFORMAÇÃO DO ESPAÇO URBANO', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, 'LAZER & SEGURANÇA', ha='center', fontsize=40, fontweight='heavy', color=ACCENT_GREEN)
    fig.text(0.5, 0.50, 'Gastronomia, clínicas e cinema climatizado nas cidades!', ha='center', fontsize=14, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-096/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
