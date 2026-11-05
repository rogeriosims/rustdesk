#!/usr/bin/env python3
"""
Script de geração automática de todos os ícones e dimensões do RocketDesk
a partir de um único arquivo de logo em alta resolução (res/logo-source.png).
"""

import os
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Instalando dependência Pillow para manipulação de imagens...")
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image

def generate_assets():
    root_dir = Path(__file__).resolve().parent.parent
    res_dir = root_dir / "res"
    source_logo = res_dir / "logo-source.png"

    if not source_logo.exists():
        print(f"[ERRO] Arquivo de logo original não encontrado em: {source_logo}")
        print("Por favor, coloque seu logo em PNG (fundo transparente) em 'res/logo-source.png'.")
        sys.exit(1)

    print(f"[+] Carregando logo base: {source_logo}")
    img = Image.open(source_logo).convert("RGBA")

    # 1. Gerar tamanhos PNG padrão
    sizes = {
        "icon.png": (512, 512),
        "32x32.png": (32, 32),
        "64x64.png": (64, 64),
        "128x128.png": (128, 128),
        "128x128@2x.png": (256, 256),
    }

    for filename, size in sizes.items():
        out_path = res_dir / filename
        resized = img.resize(size, Image.Resampling.LANCZOS)
        resized.save(out_path, format="PNG")
        print(f"  -> Gerado: res/{filename} ({size[0]}x{size[1]})")

    # 2. Gerar icon.ico com camadas multi-resolução para o Windows
    ico_path = res_dir / "icon.ico"
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save(ico_path, format="ICO", sizes=ico_sizes)
    print("  -> Gerado: res/icon.ico (camadas 16, 32, 48, 64, 128, 256)")

    # 3. Gerar tray-icon.ico (bandeja do sistema)
    tray_ico_path = res_dir / "tray-icon.ico"
    img.save(tray_ico_path, format="ICO", sizes=[(16, 16), (32, 32)])
    print("  -> Gerado: res/tray-icon.ico (16x16, 32x32)")

    # 4. Copiar para os caminhos usados pelo Flutter e pelo instalador MSI
    flutter_ico = root_dir / "flutter" / "windows" / "runner" / "resources" / "app_icon.ico"
    if flutter_ico.parent.exists():
        shutil.copy2(ico_path, flutter_ico)
        print("  -> Sincronizado: flutter/windows/runner/resources/app_icon.ico")

    msi_ico = res_dir / "msi" / "Package" / "Resources" / "icon.ico"
    if msi_ico.parent.exists():
        shutil.copy2(ico_path, msi_ico)
        print("  -> Sincronizado: res/msi/Package/Resources/icon.ico")

    print("\n[SUCESSO] Todos os assets do RocketDesk foram gerados com sucesso!")

if __name__ == "__main__":
    generate_assets()
