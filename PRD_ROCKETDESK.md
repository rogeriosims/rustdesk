# PRD: RocketDesk – Cliente Corporativo, Simplificação de UX, Modo Técnico e Distribuição MSIX / Web

## 1. Visão Geral e Objetivo
O **RocketDesk** é um fork customizado do RustDesk projetado para suporte corporativo. O objetivo é fornecer uma experiência "à prova de erros" para usuários leigos que recebem suporte, com identidade visual unificada (RocketDesk), servidores próprios embutidos (Rendezvous, Relay, API/Address Book) e geração de instaladores Windows (`.exe`, `.msi` e `.msix` para a Microsoft Store), além de suporte ao atendimento via **Cliente Web**.

---

## 2. Parâmetros e Credenciais Oficiais do Projeto

### 2.1 Servidores e Chaves de Criptografia
* **Host Rendezvous:** `srdesk.tecnologiacorporativa.com.br`
* **Relay Server:** `rdesk.tecnologiacorporativa.com.br`
* **API / Web Console:** `https://rdesk.tecnologiacorporativa.com.br`
* **Chave Pública (`RS_PUB_KEY`):** `jcFHMczcmOe3VgmkP3lIguwZofMHAnYNhbdLgauzvoc=`

### 2.2 Metadados da Microsoft Store (Partner Center)
* **Package/Identity/Name:** `NotaFcil.RocketDeskSuporteRemoto`
* **Package/Identity/Publisher:** `CN=23848FD3-96ED-48B3-B172-3D2EED3E1E8F`
* **Publisher Display Name:** `Nota Fácil`
* **Package Family Name (PFN):** `NotaFcil.RocketDeskSuporteRemoto_m8ny45tjkgn2c`
* **Store ID:** `9MVQVHFDDPTC`
* **Display Name do App:** `RocketDesk Suporte Remoto`

### 2.3 Logo e Identidade Visual
* **Arquivo Base:** `res/logo-source.png` (foguete estilizado, fundo transparente, 1024x1024).
* **Script de Geração:** `python res/generate_assets.py` gera automaticamente todos os formatos requeridos:
  - `res/icon.ico` (multi-resolução: 16, 32, 48, 64, 128, 256)
  - `res/icon.png` (512x512)
  - `res/tray-icon.ico` (bandeja do sistema)
  - Sincronização direta com `flutter/windows/runner/resources/app_icon.ico` e `res/msi/Package/Resources/icon.ico`.

---

## 3. Especificação Técnica de Implementação

### TAREFA 1: Simplificação da UX da Tela Inicial (Flutter)
Arquivo de foco: `flutter/lib/desktop/pages/desktop_home_page.dart`

1. **Hierarquia Visual com Foco no Leigo:**
   - A tela inicial deve ser dominada pelo card **"Permitir Acesso do Técnico"** (largura ~60-65%).
   - **Passo 1 (ID):** Exibir o número da ID em fonte grande (**36pt, negrito**), com botão destacado **[ Copiar ID ]** ao lado.
   - **Passo 2 (Senha):** Senha de uso único visível, com ações de mostrar e renovar senha.
   - **Status do Servidor:** Indicador visual verde no cabeçalho com o texto: *"Servidor RocketDesk: Online"*.
   - **Aviso Amigável:** Texto explicativo curto orientando o cliente a clicar em "Aceitar" quando o técnico solicitar a conexão.

2. **Área de Prestar Suporte (Secundária):**
   - Card lateral (~35% da largura) destinado a técnicos realizarem conexões:
   - Campo para digitar o ID remoto, botão **[ CONECTAR AGORA ]** em destaque (laranja da marca) e histórico dos computadores recentes.

---

### TAREFA 2: Modo Técnico / Acesso às Configurações Completas
**Requisito Crítico:** A tela simplificada para o usuário leigo **não deve eliminar** as configurações avançadas do RocketDesk. O técnico deve ter uma forma simples e garantida de acessar o painel de configurações completas:

1. **Ponto de Acesso na Interface:**
   - No cabeçalho superior direito da janela (ou menu de opções da barra), manter um ícone discreto de engrenagem ou botão **[ Configurações ]** / **[ Modo Técnico ]**.
2. **Acesso Completo ao Painel Original:**
   - Ao clicar, abrir a tela completa de configurações (`flutter/lib/desktop/pages/server_page.dart` / `settings_page.dart`), com todas as abas nativas:
     - **Geral:** Iniciar com o Windows, Tema (Claro/Escuro), Idioma.
     - **Segurança:** Configurar senha fixa para acesso desassistido, aprovação de conexão, permissões de teclado/mouse.
     - **Rede:** Exibição do servidor RocketDesk conectado (com opção de desbloquear caso o técnico queira alterar).
     - **Exibição & Codecs:** Qualidade de imagem, FPS, aceleração por hardware (hwcodec).
     - **Gravação & Áudio:** Gravação de sessão, microfone e som do sistema.
3. **Bloqueio Opcional por Senha:**
   - Manter compatibilidade com o recurso de **Senha de Administrador** do RustDesk (`Admin Password`), permitindo que a empresa bloqueie essa engrenagem de configurações com senha para que funcionários não alterem as opções de segurança da máquina.

---

### TAREFA 3: Configuração do Backend Rust (`libs/hbb_common/src/config.rs`)
Garantir que as seguintes constantes estejam fixas e ativas no backend:
* `APP_NAME`: `"RocketDesk"`
* `RENDEZVOUS_SERVERS`: `&["srdesk.tecnologiacorporativa.com.br", "rdesk.tecnologiacorporativa.com.br"]`
* `RS_PUB_KEY`: `"jcFHMczcmOe3VgmkP3lIguwZofMHAnYNhbdLgauzvoc="`
* Fallback de API apontando para `https://rdesk.tecnologiacorporativa.com.br`.

---

### TAREFA 4: Configuração da Microsoft Store e MSIX (`flutter/pubspec.yaml`)
Configurar o plugin `msix` com os dados oficiais validados:
```yaml
msix_config:
  display_name: RocketDesk Suporte Remoto
  publisher_display_name: Nota Fácil
  identity_name: NotaFcil.RocketDeskSuporteRemoto
  publisher: CN=23848FD3-96ED-48B3-B172-3D2EED3E1E8F
  msix_version: 1.4.4.0
  logo_path: assets/logo-rocketdesk.png
  store: true
  capabilities:
    - internetClient
    - runFullTrust
```

---

### TAREFA 5: Integração do Cliente Web (RocketDesk Web)
O ecossistema RocketDesk conta com a interface Web para atendimento sem instalação:
1. **Repositório Base:** `rustdesk-web` (WebAssembly + WebSockets).
2. **Conexão com os Mesmos Servidores:**
   - O cliente web conecta nas portas WebSocket do servidor RocketDesk (`WS_RENDEZVOUS_PORT: 21118` e `WS_RELAY_PORT: 21119`) configuradas no `srdesk.tecnologiacorporativa.com.br`.
   - Utiliza a mesma chave pública `jcFHMczcmOe3VgmkP3lIguwZofMHAnYNhbdLgauzvoc=`.
3. **Deploy:** Pode ser servido via Docker/Nginx com SSL em um subdomínio próprio (ex: `https://web.rockethub.com.br` ou `https://web.tecnologiacorporativa.com.br`).
4. **Aplicação do Branding:** Aplicar as cores oficiais (azul espacial e laranja) e a logo `logo-rocketdesk.png` na tela de login web.

---

### TAREFA 6: Pipeline de Build Automatizado no GitHub Actions
Workflow `.github/workflows/build-windows.yml`:
1. Disparo manual via `workflow_dispatch`.
2. Compilação exclusiva do target Windows:
   - `generate-bridge`
   - `build-RustDeskTempTopMostWindow`
   - `build-for-windows-flutter`
3. Upload direto para a aba **Artifacts** dos seguintes arquivos:
   - `rocketdesk-1.4.4-x86_64.exe` (Instalador portátil auto-extraível).
   - `rocketdesk-1.4.4-x86_64.msi` (Instalador corporativo MSI).
   - `rocketdesk-1.4.4-x86_64.msix` (Pacote pronto para upload na Microsoft Store).
4. Tempo total de execução: ~25 a 30 minutos.

---

## 4. Regras Rígidas para o Desenvolvedor (Definition of Done)
1. **Nenhum caminho absoluto local:** Qualquer menção a `C:\...` que não seja variável de ambiente do CI reprova o PR imediatamente.
2. **Nenhum arquivo de log committed:** Arquivos temporários como `flutter_run.log` não devem ser comitados.
3. **Veracidade no PR:** A descrição do PR deve refletir estritamente as alterações presentes no `git diff`.
4. **Preservação das Configurações Avançadas:** A simplificação da tela não pode remover o acesso às configurações completas pelo técnico.
