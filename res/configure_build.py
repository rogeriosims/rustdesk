#!/usr/bin/env python3
"""
Script de pré-compilação do RocketDesk:
Injeta as configurações do servidor próprio, chave pública e metadados no código Rust
e gera todos os ícones necessários antes do build.
"""

import os
import re
from pathlib import Path

def configure():
    root_dir = Path(__file__).resolve().parent.parent

    # 1. Configurações padrão
    host = "srdesk.tecnologiacorporativa.com.br"
    relay = "rdesk.tecnologiacorporativa.com.br"
    pub_key = "jcFHMczcmOe3VgmkP3lIguwZofMHAnYNhbdLgauzvoc="
    app_name = "RocketDesk"

    # Ler .env se existir
    env_file = root_dir / ".env"
    if env_file.exists():
        print(f"[+] Lendo configuracoes de {env_file}")
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                if k == "ROCKETDESK_HOST": host = v
                if k == "ROCKETDESK_RELAY": relay = v
                if k == "ROCKETDESK_KEY": pub_key = v
                if k == "APP_NAME": app_name = v

    print(f"[+] Configurando RocketDesk:")
    print(f"    Host: {host}")
    print(f"    Relay: {relay}")
    print(f"    Key: {pub_key}")
    print(f"    App Name: {app_name}")

    # 2. Injetar em libs/hbb_common/src/config.rs
    config_rs = root_dir / "libs" / "hbb_common" / "src" / "config.rs"
    if config_rs.exists():
        content = config_rs.read_text(encoding="utf-8")

        # Injetar APP_NAME
        content = re.sub(
            r'pub static ref APP_NAME: RwLock<String> = RwLock::new\(.*?\);',
            f'pub static ref APP_NAME: RwLock<String> = RwLock::new("{app_name}".to_owned());',
            content
        )

        # Injetar RENDEZVOUS_SERVERS
        servers_code = f'&["{host}", "{relay}"]' if relay and relay != host else f'&["{host}"]'
        content = re.sub(
            r'pub const RENDEZVOUS_SERVERS: &\[&str\] = &\[.*?\];',
            f'pub const RENDEZVOUS_SERVERS: &[&str] = {servers_code};',
            content
        )

        # Injetar RS_PUB_KEY
        content = re.sub(
            r'pub const RS_PUB_KEY: &str = ".*?";',
            f'pub const RS_PUB_KEY: &str = "{pub_key}";',
            content
        )

        config_rs.write_text(content, encoding="utf-8")
        print(f"  -> Injetado com sucesso em: {config_rs}")
    else:
        print(f"[!] Aviso: {config_rs} nao encontrado.")

    # 3. Gerar Assets/Icones se o logo existir
    logo_source = root_dir / "res" / "logo-source.png"
    if logo_source.exists():
        assets_script = root_dir / "res" / "generate_assets.py"
        if assets_script.exists():
            print("[+] Atualizando icones a partir de res/logo-source.png...")
            os.system(f'python "{assets_script}"')

    print("\n[SUCESSO] Configuracao de build concluida com sucesso!")

if __name__ == "__main__":
    configure()
