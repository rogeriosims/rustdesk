#!/usr/bin/env python3
"""
Gera um mockup visual em alta resolução da nova interface do RocketDesk
com a identidade visual do logo (azul profundo, ciano elétrico e detalhes em chama laranja).
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_mockup():
    width = 1600
    height = 1000

    # Canvas principal com gradiente suave de fundo
    canvas = Image.new("RGBA", (width, height), (15, 23, 42, 255))
    draw = ImageDraw.Draw(canvas)

    # Fundo com iluminação radial suave
    for r in range(600, 0, -20):
        alpha = int(25 * (1 - r / 600))
        draw.ellipse([800 - r, 500 - r, 800 + r, 500 + r], fill=(30, 58, 138, alpha))

    # Dimensões da Janela do RocketDesk
    win_w = 1100
    win_h = 720
    win_x = (width - win_w) // 2
    win_y = (height - win_h) // 2

    # 1. Sombra da janela
    shadow_offset = 18
    shadow_blur = 30
    shadow = Image.new("RGBA", (win_w + shadow_blur * 2, win_h + shadow_blur * 2), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle(
        [shadow_blur, shadow_blur, win_w + shadow_blur, win_h + shadow_blur],
        radius=16,
        fill=(0, 0, 0, 160)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(shadow_blur // 2))
    canvas.paste(shadow, (win_x - shadow_blur, win_y - shadow_blur + shadow_offset), mask=shadow)

    # 2. Janela Principal (Windows 11 Mica / Slate Dark)
    win_img = Image.new("RGBA", (win_w, win_h), (0, 0, 0, 0))
    w_draw = ImageDraw.Draw(win_img)

    # Fundo da janela
    w_draw.rounded_rectangle([0, 0, win_w, win_h], radius=14, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=1)

    # Carregar fontes Segoe UI
    font_path_regular = "C:\\Windows\\Fonts\\segoeui.ttf"
    font_path_bold = "C:\\Windows\\Fonts\\segoeuib.ttf"

    font_title = ImageFont.truetype(font_path_bold, 13)
    font_brand = ImageFont.truetype(font_path_bold, 22)
    font_heading = ImageFont.truetype(font_path_bold, 17)
    font_subheading = ImageFont.truetype(font_path_bold, 13)
    font_id_huge = ImageFont.truetype(font_path_bold, 36)
    font_label = ImageFont.truetype(font_path_bold, 11)
    font_body = ImageFont.truetype(font_path_regular, 13)
    font_badge = ImageFont.truetype(font_path_bold, 11)

    # Barra de Título (Windows 11)
    titlebar_h = 42
    w_draw.rounded_rectangle([0, 0, win_w, titlebar_h], radius=14, fill=(11, 19, 36, 255))
    w_draw.rectangle([0, 20, win_w, titlebar_h], fill=(11, 19, 36, 255))
    w_draw.line([(0, titlebar_h), (win_w, titlebar_h)], fill=(30, 41, 59, 255), width=1)

    # Botões fechar/minimizar
    w_draw.line([(win_w - 95, 21), (win_w - 85, 21)], fill=(148, 163, 184, 255), width=1)
    w_draw.rectangle([win_w - 65, 16, win_w - 55, 26], outline=(148, 163, 184, 255), width=1)
    w_draw.line([(win_w - 30, 16), (win_w - 20, 26)], fill=(148, 163, 184, 255), width=1)
    w_draw.line([(win_w - 20, 16), (win_w - 30, 26)], fill=(148, 163, 184, 255), width=1)

    # Título da Barra
    w_draw.text((45, 12), "RocketDesk - Suporte Remoto Corporativo", font=font_title, fill=(203, 213, 225, 255))

    # Cabeçalho / Branding
    header_y = 56
    logo_path = Path("res/logo-source.png")
    if logo_path.exists():
        logo_img = Image.open(logo_path).convert("RGBA")
        logo_mini = logo_img.resize((22, 22), Image.Resampling.LANCZOS)
        win_img.paste(logo_mini, (16, 10), mask=logo_mini)

        logo_header = logo_img.resize((64, 64), Image.Resampling.LANCZOS)
        win_img.paste(logo_header, (32, header_y - 6), mask=logo_header)

    w_draw.text((106, header_y + 4), "ROCKETDESK", font=font_brand, fill=(248, 250, 252, 255))
    w_draw.text((106, header_y + 32), "Suporte Remoto Simples, Rápido e Seguro", font=font_body, fill=(148, 163, 184, 255))

    # Status de Conexão
    status_w = 260
    status_x = win_w - status_w - 32
    w_draw.rounded_rectangle([status_x, header_y + 10, status_x + status_w, header_y + 42], radius=16, fill=(16, 185, 129, 25), outline=(16, 185, 129, 90), width=1)
    w_draw.ellipse([status_x + 16, header_y + 22, status_x + 24, header_y + 30], fill=(52, 211, 153, 255))
    w_draw.text((status_x + 34, header_y + 18), "Servidor RocketDesk: Online", font=font_subheading, fill=(52, 211, 153, 255))

    # Linha divisória
    w_draw.line([(32, 130), (win_w - 32, 130)], fill=(30, 41, 59, 255), width=1)

    # =========================================================================
    # ÁREA PRINCIPAL
    # =========================================================================
    content_y = 150
    card_h = 530

    # CARD 1: RECEBER SUPORTE (60%)
    c1_x = 32
    c1_w = 600
    w_draw.rounded_rectangle([c1_x, content_y, c1_x + c1_w, content_y + card_h], radius=12, fill=(22, 30, 52, 255), outline=(37, 99, 235, 140), width=1)

    # Tag
    w_draw.rounded_rectangle([c1_x + 24, content_y + 24, c1_x + 220, content_y + 52], radius=6, fill=(37, 99, 235, 45), outline=(56, 189, 248, 200), width=1)
    w_draw.text((c1_x + 36, content_y + 30), "CLIENTE • RECEBER AJUDA", font=font_badge, fill=(56, 189, 248, 255))

    w_draw.text((c1_x + 24, content_y + 68), "Permitir Acesso do Técnico", font=font_heading, fill=(248, 250, 252, 255))
    w_draw.text((c1_x + 24, content_y + 96), "Passe os dados abaixo para o técnico conectar no seu computador:", font=font_body, fill=(148, 163, 184, 255))

    # PASSO 1: SUA ID
    p1_y = content_y + 130
    w_draw.text((c1_x + 24, p1_y), "PASSO 1: SUA ID DE SUPORTE", font=font_label, fill=(56, 189, 248, 255))

    id_box_y = p1_y + 20
    id_box_h = 76
    w_draw.rounded_rectangle([c1_x + 24, id_box_y, c1_x + c1_w - 24, id_box_y + id_box_h], radius=8, fill=(11, 18, 38, 255), outline=(56, 189, 248, 220), width=2)
    w_draw.text((c1_x + 44, id_box_y + 16), "842 190 735", font=font_id_huge, fill=(248, 250, 252, 255))

    btn_copy_w = 140
    btn_copy_x = c1_x + c1_w - 24 - btn_copy_w - 12
    btn_copy_y = id_box_y + 16
    w_draw.rounded_rectangle([btn_copy_x, btn_copy_y, btn_copy_x + btn_copy_w, btn_copy_y + 44], radius=6, fill=(37, 99, 235, 255))
    w_draw.text((btn_copy_x + 36, btn_copy_y + 13), "Copiar ID", font=font_subheading, fill=(255, 255, 255, 255))

    # PASSO 2: SENHA
    p2_y = id_box_y + id_box_h + 24
    w_draw.text((c1_x + 24, p2_y), "PASSO 2: SENHA DE ACESSO TEMPORARIA", font=font_label, fill=(56, 189, 248, 255))

    pwd_box_y = p2_y + 20
    pwd_box_h = 56
    w_draw.rounded_rectangle([c1_x + 24, pwd_box_y, c1_x + c1_w - 24, pwd_box_y + pwd_box_h], radius=8, fill=(11, 18, 38, 255), outline=(51, 65, 85, 255), width=1)
    w_draw.text((c1_x + 44, pwd_box_y + 16), "k8#9Xp2M", font=font_heading, fill=(226, 232, 240, 255))

    w_draw.text((c1_x + 360, pwd_box_y + 18), "[ Mostrar ]", font=font_subheading, fill=(148, 163, 184, 255))
    w_draw.text((c1_x + 460, pwd_box_y + 18), "[ Nova Senha ]", font=font_subheading, fill=(148, 163, 184, 255))

    # Alerta de Segurança
    alert_y = pwd_box_y + pwd_box_h + 26
    w_draw.rounded_rectangle([c1_x + 24, alert_y, c1_x + c1_w - 24, alert_y + 115], radius=8, fill=(15, 23, 42, 255), outline=(249, 115, 22, 140), width=1)
    w_draw.text((c1_x + 44, alert_y + 16), "AVISO DE SEGURANCA E PRIVACIDADE", font=font_label, fill=(249, 115, 22, 255))
    w_draw.text((c1_x + 44, alert_y + 40), "* So informe estes dados para tecnicos autorizados da sua empresa.", font=font_body, fill=(203, 213, 225, 255))
    w_draw.text((c1_x + 44, alert_y + 64), "* Quando a conexao iniciar, clique em 'ACEITAR' na tela de confirmacao.", font=font_body, fill=(203, 213, 225, 255))
    w_draw.text((c1_x + 44, alert_y + 88), "* Voce pode encerrar o acesso do suporte a qualquer instante.", font=font_body, fill=(148, 163, 184, 255))

    # CARD 2: FAZER SUPORTE (36%)
    c2_x = c1_x + c1_w + 24
    c2_w = win_w - c2_x - 32

    w_draw.rounded_rectangle([c2_x, content_y, c2_x + c2_w, content_y + card_h], radius=12, fill=(20, 27, 45, 255), outline=(51, 65, 85, 200), width=1)

    w_draw.rounded_rectangle([c2_x + 24, content_y + 24, c2_x + 215, content_y + 52], radius=6, fill=(51, 65, 85, 70), outline=(100, 116, 139, 200), width=1)
    w_draw.text((c2_x + 36, content_y + 30), "TECNICO • PRESTAR SUPORTE", font=font_badge, fill=(203, 213, 225, 255))

    w_draw.text((c2_x + 24, content_y + 68), "Acessar Outro Computador", font=font_heading, fill=(248, 250, 252, 255))
    w_draw.text((c2_x + 24, content_y + 96), "Digite a ID da maquina remota:", font=font_body, fill=(148, 163, 184, 255))

    input_y = content_y + 130
    w_draw.rounded_rectangle([c2_x + 24, input_y, c2_x + c2_w - 24, input_y + 52], radius=6, fill=(11, 18, 38, 255), outline=(71, 85, 105, 255), width=1)
    w_draw.text((c2_x + 40, input_y + 16), "Digite a ID do parceiro...", font=font_body, fill=(100, 116, 139, 255))

    btn_conn_y = input_y + 68
    w_draw.rounded_rectangle([c2_x + 24, btn_conn_y, c2_x + c2_w - 24, btn_conn_y + 48], radius=6, fill=(249, 115, 22, 255))
    w_draw.text((c2_x + 130, btn_conn_y + 14), "CONECTAR AGORA", font=font_heading, fill=(255, 255, 255, 255))

    hist_y = btn_conn_y + 76
    w_draw.line([(c2_x + 24, hist_y - 12), (c2_x + c2_w - 24, hist_y - 12)], fill=(30, 41, 59, 255), width=1)
    w_draw.text((c2_x + 24, hist_y), "COMPUTADORES RECENTES", font=font_label, fill=(148, 163, 184, 255))

    devices = [
        ("[Servidor] Matriz Financeiro", "942 110 302", "Online"),
        ("[Notebook] Diretor", "721 884 109", "Offline"),
        ("[PDV] Caixa 01", "309 451 992", "Online"),
    ]

    dev_y = hist_y + 26
    for name, did, st in devices:
        w_draw.rounded_rectangle([c2_x + 24, dev_y, c2_x + c2_w - 24, dev_y + 48], radius=6, fill=(15, 23, 42, 255), outline=(30, 41, 59, 255), width=1)
        w_draw.text((c2_x + 36, dev_y + 8), name, font=font_subheading, fill=(226, 232, 240, 255))
        w_draw.text((c2_x + 36, dev_y + 26), did, font=font_body, fill=(100, 116, 139, 255))

        st_color = (52, 211, 153, 255) if st == "Online" else (148, 163, 184, 255)
        w_draw.text((c2_x + c2_w - 80, dev_y + 14), st, font=font_badge, fill=st_color)
        dev_y += 58

    canvas.paste(win_img, (win_x, win_y), mask=win_img)

    out_path = Path("res/ui_mockup.png")
    canvas.save(out_path, format="PNG")
    print(f"[+] Mockup gerado com sucesso em: {out_path.resolve()}")

if __name__ == "__main__":
    create_mockup()
