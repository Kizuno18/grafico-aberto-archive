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
    
    fig.text(0.5, 0.88, 'CENSO DA EDUCAÇÃO SUPERIOR (INEP/MEC)', ha='center', fontsize=19, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'A REVOLUÇÃO DO EAD', ha='center', fontsize=34, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.77, 'O ensino a distância superou o presencial', ha='center', fontsize=21, color=ACCENT_BLUE)
    
    rect = plt.Rectangle((0.10, 0.38), 0.80, 0.34, facecolor=CARD_COLOR, edgecolor=ACCENT_BLUE, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    
    fig.text(0.5, 0.66, 'FATIA DOS NOVOS CALOUROS NO EAD', ha='center', fontsize=14, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.54, '65%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_BLUE)
    fig.text(0.5, 0.44, 'Quase 2 em cada 3 novos alunos entram online!', ha='center', fontsize=17, color=TEXT_MAIN)
    
    fig.text(0.5, 0.28, 'Fonte oficial: Sinopse Estatística do Ensino Superior — Inep', ha='center', fontsize=15, color=TEXT_MUTED)
    fig.text(0.5, 0.22, '@ograficoaberto', ha='center', fontsize=20, fontweight='bold', color=ACCENT_GREEN)
    
    save_vertical(fig, 'videos/SHORT-078/assets/scene1.png')

def make_scene2():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'A INVERSÃO DAS MATRÍCULAS (2012 A 2024)', ha='center', fontsize=20, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'EAD VS PRESENCIAL (%)', ha='center', fontsize=33, fontweight='bold', color=ACCENT_YELLOW)
    
    sub_ax = fig.add_axes([0.15, 0.38, 0.70, 0.35], facecolor=CARD_COLOR)
    anos = ['2012', '2016', '2020', '2024']
    ead = [16, 28, 53, 65]
    pres = [84, 72, 47, 35]
    
    sub_ax.plot(anos, ead, marker='o', markersize=8, color=ACCENT_BLUE, linewidth=3, label='EAD (Online)')
    sub_ax.plot(anos, pres, marker='s', markersize=8, color=ACCENT_CORAL, linewidth=3, label='Presencial')
    sub_ax.set_ylim(0, 100)
    sub_ax.set_ylabel('% dos Novos Ingressantes', color=TEXT_MUTED, fontsize=11)
    sub_ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFF')
    sub_ax.tick_params(colors=TEXT_MAIN, labelsize=11)
    sub_ax.legend(facecolor='#141D28', edgecolor='none', labelcolor=TEXT_MAIN, loc='center right')
    
    sub_ax.annotate('65% EAD', ('2024', 65), textcoords='offset points', xytext=(0, 10), 
                     ha='center', color=ACCENT_BLUE, fontweight='bold', fontsize=11)
    sub_ax.annotate('35% Pres.', ('2024', 35), textcoords='offset points', xytext=(0, -18), 
                     ha='center', color=ACCENT_CORAL, fontweight='bold', fontsize=11)
        
    fig.text(0.5, 0.31, 'Cursos como Pedagogia e Administração passam de 80% EAD!', ha='center', fontsize=15, fontweight='bold', color=ACCENT_YELLOW)
    fig.text(0.5, 0.26, 'Mensalidades acessíveis atraíram trabalhadores assalariados', ha='center', fontsize=13, color=TEXT_MUTED)
    fig.text(0.5, 0.21, 'Fonte: Censo do Ensino Superior / Inep | Gráfico Aberto', ha='center', fontsize=14, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-078/assets/scene2.png')

def make_scene3():
    fig, ax = plt.subplots(figsize=(10.8, 19.2), dpi=100)
    ax.set_facecolor(BG_COLOR)
    ax.axis('off')
    
    fig.text(0.5, 0.88, 'QUALIDADE & RETENÇÃO (MEC/ABMES)', ha='center', fontsize=21, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.82, 'O DESAFIO DA EVASÃO', ha='center', fontsize=34, fontweight='bold', color=ACCENT_CORAL)
    
    rect = plt.Rectangle((0.10, 0.48), 0.80, 0.28, facecolor=CARD_COLOR, edgecolor=ACCENT_CORAL, 
                         linewidth=4, transform=fig.transFigure, zorder=2)
    fig.patches.append(rect)
    fig.text(0.5, 0.70, 'TAXA DE EVASÃO MÉDIA NO EAD', ha='center', fontsize=15, fontweight='bold', color=TEXT_MUTED)
    fig.text(0.5, 0.58, '> 50%', ha='center', fontsize=64, fontweight='heavy', color=ACCENT_CORAL)
    fig.text(0.5, 0.50, 'Mais de metade dos alunos abandonam o curso antes do fim!', ha='center', fontsize=14, color=TEXT_MAIN)
    
    cta_box = plt.Rectangle((0.10, 0.25), 0.80, 0.18, facecolor='#111A24', edgecolor=ACCENT_BLUE, 
                            linewidth=3, transform=fig.transFigure, zorder=2)
    fig.patches.append(cta_box)
    fig.text(0.5, 0.37, 'GRÁFICO ABERTO', ha='center', fontsize=22, fontweight='bold', color=TEXT_MAIN)
    fig.text(0.5, 0.31, 'A realidade explicada através de dados oficiais', ha='center', fontsize=14, color=ACCENT_GREEN)
    fig.text(0.5, 0.27, 'Inscreva-se em @ograficoaberto', ha='center', fontsize=15, color=TEXT_MUTED)
    
    save_vertical(fig, 'videos/SHORT-078/assets/scene3.png')

make_scene1()
make_scene2()
make_scene3()
