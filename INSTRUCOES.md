# Instruções para Personalização e Desenvolvimento

Este documento detalha os passos necessários para personalizar e compilar o aplicativo com sua própria marca, incluindo logotipo, cores, configurações de servidor e um guia de desenvolvimento para Windows.

## 1. Personalização de Logotipo e Ícones

Para personalizar a aparência do aplicativo com a sua marca, você precisará substituir vários arquivos de imagem e ícone localizados principalmente no diretório `res/`. Abaixo estão listados os arquivos que você deve substituir, juntamente com suas especificações.

### Arquivos Principais de Logotipo

-   **`res/logo.svg`**: Este é o logotipo principal usado em várias partes da interface do usuário.
    *   **Formato**: SVG (Scalable Vector Graphics)
    *   **Especificações**: Recomenda-se um design quadrado ou circular para melhor ajuste.

-   **`res/logo-header.svg`**: Este logotipo aparece no cabeçalho da janela principal.
    *   **Formato**: SVG
    *   **Especificações**: Geralmente é uma versão mais larga ou estilizada do logotipo principal.

-   **`res/rustdesk-banner.svg`**: Banner exibido em algumas telas, como na página "Sobre".
    *   **Formato**: SVG
    *   **Especificações**: Design retangular.

### Ícones da Aplicação

-   **`res/icon.ico`**: Ícone principal para a aplicação em Windows.
    *   **Formato**: ICO (Windows Icon)
    *   **Especificações**: Deve conter múltiplos tamanhos (por exemplo, 16x16, 32x32, 48x48, 256x256) para garantir a exibição correta em diferentes contextos do Windows.

-   **`res/icon.png`**: Ícone padrão usado em contextos onde PNG é preferível (por exemplo, Linux).
    *   **Formato**: PNG (Portable Network Graphics)
    *   **Dimensões**: 512x512 pixels.

### Ícones para Diferentes Plataformas e Tamanhos

-   **Ícones PNG de Tamanho Específico**: Usados para menus, instaladores e diferentes densidades de tela.
    *   `res/32x32.png`: 32x32 pixels
    *   `res/64x64.png`: 64x64 pixels
    *   `res/128x128.png`: 128x128 pixels
    *   `res/128x128@2x.png`: 256x256 pixels (para telas de alta densidade)

-   **Ícone para macOS**:
    *   `res/mac-icon.png`: Ícone específico para o aplicativo no macOS.
    *   **Formato**: PNG
    *   **Dimensões**: 1024x1024 pixels para suportar o formato de ícone do macOS.

-   **Ícone da Bandeja do Sistema (System Tray)**:
    *   `res/tray-icon.ico`: Ícone exibido na bandeja do sistema no Windows.
    *   **Formato**: ICO
    *   **Especificações**: Geralmente 16x16 ou 32x32 pixels, com um design simples e claro.
    *   `res/mac-tray-dark-x2.png` e `res/mac-tray-light-x2.png`: Ícones da bandeja para macOS nos modos escuro e claro. Devem ser PNGs monocromáticos.

### Processo de Substituição

1.  Crie seus próprios arquivos de imagem e ícone seguindo as especificações acima.
2.  Nomeie seus arquivos para corresponder exatamente aos nomes dos arquivos originais.
3.  Substitua os arquivos existentes no diretório `res/` pelos seus arquivos personalizados.
4.  Após a substituição, recompile o aplicativo para que as alterações entrem em vigor.

## 2. Personalização de Cores e Estilo

As cores e o tema do aplicativo são definidos no código-fonte do Flutter. Para personalizar a paleta de cores, você precisará editar principalmente os seguintes arquivos:

### Arquivo de Constantes de Cor

-   **Arquivo**: `flutter/lib/consts.dart`
-   **Descrição**: Este arquivo contém definições de cores estáticas usadas em todo o aplicativo.

**Exemplo de Modificação**:

Localize as seguintes constantes de cor e altere seus valores hexadecimais (ARGB) para corresponder à sua paleta de marca:

```dart
// Exemplo de como as cores são definidas em consts.dart
const Color kColorWarn = Color.fromARGB(255, 245, 133, 59);
const Color kColorCanvas = Colors.black;
```

Para alterar a cor de aviso para um tom de vermelho, você poderia fazer:

```dart
// Novo valor para a cor de aviso
const Color kColorWarn = Color.fromARGB(255, 217, 30, 24); // Exemplo: Vermelho
```

### Arquivo de Tema Principal

-   **Arquivo**: `flutter/lib/main.dart` (e arquivos de tema relacionados que ele possa importar, como `flutter/lib/common.dart` ou um arquivo `theme.dart` dedicado, se existir).
-   **Descrição**: O arquivo `main.dart` define os temas claro (`lightTheme`) e escuro (`darkTheme`) para o aplicativo, incluindo cores primárias, de destaque, de fundo e de texto.

**Exemplo de Modificação**:

No arquivo `main.dart` ou em um arquivo de tema importado, procure pelas definições `ThemeData`. Você pode alterar a cor primária (usada em barras de aplicativos, botões, etc.) e outras propriedades do tema.

```dart
// Em algum lugar dentro da definição de ThemeData em seu código
// (pode estar em um arquivo como flutter/lib/common.dart -> MyTheme)

// Exemplo para o tema claro
static final lightTheme = ThemeData.light().copyWith(
  primaryColor: Colors.blue, // Altere para a cor primária da sua marca
  // Outras propriedades de cor...
);

// Exemplo para o tema escuro
static final darkTheme = ThemeData.dark().copyWith(
  primaryColor: Colors.teal, // Altere para a cor primária do seu tema escuro
  // Outras propriedades de cor...
);
```

**Mapeamento de Cores Comuns**:

-   `primaryColor`: A cor principal da sua marca, usada na maioria dos elementos da interface.
-   `accentColor` (ou `colorScheme.secondary` em temas mais recentes): Cor de destaque para elementos interativos como botões flutuantes.
-   `canvasColor`, `scaffoldBackgroundColor`: Cores de fundo principais.
-   `cardColor`: Cor de fundo para cartões e painéis.
-   `textTheme`: Para definir as cores do texto.

### Processo de Modificação

1.  Abra os arquivos mencionados (`flutter/lib/consts.dart`, `flutter/lib/main.dart`, etc.).
2.  Identifique as variáveis de cor e as definições de `ThemeData`.
3.  Substitua os valores de cor existentes pelos códigos de cor da sua marca.
4.  Recompile o aplicativo Flutter para aplicar as novas cores.

## 3. Configuração Padrão do Servidor

Para garantir que o aplicativo se conecte ao seu servidor auto-hospedado por padrão, sem exigir configuração manual do usuário, você pode embutir (hardcode) o endereço do servidor e a chave pública diretamente no código-fonte.

### Arquivo de Configuração

-   **Arquivo**: `libs/hbb_common/src/config.rs`
-   **Descrição**: Este arquivo define as configurações padrão de conexão, incluindo o servidor de rendezvous e a chave pública de criptografia.

### Modificando o Servidor de Rendezvous

1.  Abra o arquivo `libs/hbb_common/src/config.rs`.
2.  Localize a constante `RENDEZVOUS_SERVERS`.
3.  Substitua o valor padrão pelo endereço do seu servidor. Se você tiver mais de um servidor, pode listá-los separados por vírgula.

**Exemplo**:

```rust
// Original
pub const RENDEZVOUS_SERVERS: &[&str] = &["rs-ny.rustdesk.com"];

// Modificado
pub const RENDEZVOUS_SERVERS: &[&str] = &["seu.servidor.com"];
```

### Modificando a Chave Pública

1.  No mesmo arquivo (`libs/hbb_common/src/config.rs`), localize a constante `RS_PUB_KEY`.
2.  Substitua a chave pública padrão pela chave pública do seu servidor. A chave deve ser uma string codificada em base64.

**Exemplo**:

```rust
// Original
pub const RS_PUB_KEY: &str = "OeVuKk5nlHiXp+APNn0Y3pC1Iwpwn44JGqrQCsWqmBw=";

// Modificado
pub const RS_PUB_KEY: &str = "sua-chave-publica-em-base64";
```

### Importante

-   A chave pública (`RS_PUB_KEY`) que você insere no código-fonte do cliente **deve corresponder à chave pública usada pelo seu servidor `hbbs`**. Se as chaves não corresponderem, o cliente não conseguirá se conectar ao servidor.
-   Após fazer essas alterações, você deve recompile completamente o aplicativo para que as novas configurações padrão sejam incluídas no executável final.

## 4. Guia de Desenvolvimento para Windows 10

Esta seção fornece um guia passo a passo para configurar um ambiente de desenvolvimento no Windows 10, permitindo que você modifique, compile e teste o aplicativo.

### 4.1. Pré-requisitos e Instalação de Ferramentas

Você precisará das seguintes ferramentas:

1.  **Visual Studio Code**: Um editor de código-fonte leve e poderoso.
    *   **Instalação**: Baixe e instale a partir do [site oficial do VS Code](https://code.visualstudio.com/).
    *   **Extensões Recomendadas**:
        *   `rust-analyzer`: Para suporte à linguagem Rust.
        *   `Dart`: Para suporte à linguagem Dart.
        *   `Flutter`: Para desenvolvimento Flutter.

2.  **Rust**: A linguagem de programação usada para o backend do aplicativo.
    *   **Instalação**: Instale o Rust através do `rustup`. Baixe o `rustup-init.exe` do [site oficial do Rust](https://www.rust-lang.org/tools/install) e siga as instruções. A instalação padrão geralmente é suficiente.

3.  **Flutter SDK**: O kit de desenvolvimento para a interface do usuário do aplicativo.
    *   **Instalação**: Siga o [guia de instalação oficial do Flutter para Windows](https://flutter.dev/docs/get-started/install/windows). Isso inclui baixar o SDK, extraí-lo e adicionar o diretório `flutter/bin` ao seu PATH do sistema.
    *   **Verificação**: Após a instalação, execute `flutter doctor` no seu terminal para garantir que todas as dependências estejam corretas.

4.  **vcpkg**: Um gerenciador de pacotes da Microsoft para bibliotecas C++.
    *   **Instalação**: Siga o [guia oficial do vcpkg](https://github.com/microsoft/vcpkg). O processo geralmente envolve clonar o repositório e executar um script de bootstrap.
        ```bash
        git clone https://github.com/microsoft/vcpkg
        cd vcpkg
        ./bootstrap-vcpkg.bat
        ```
    *   **Variável de Ambiente**: Defina a variável de ambiente `VCPKG_ROOT` para o diretório onde você clonou o vcpkg.
    *   **Instalação de Dependências**: Use o vcpkg para instalar as bibliotecas necessárias, conforme listado no `README.md` do projeto.
        ```bash
        vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
        ```

### 4.2. Processo de Compilação e Teste

1.  **Obtenha o Código-Fonte**:
    *   Clone o repositório do aplicativo para o seu computador.
        ```bash
        git clone https://github.com/rustdesk/rustdesk.git
        cd rustdesk
        ```

2.  **Abra no VS Code**:
    *   Abra a pasta do projeto no Visual Studio Code.
        ```bash
        code .
        ```

3.  **Realize as Modificações**:
    *   Use o VS Code para editar os arquivos conforme descrito nas seções de personalização deste documento (logotipos, cores, configurações do servidor).

4.  **Compile o Aplicativo**:
    *   Abra um terminal dentro do VS Code (ou use um terminal externo).
    *   Execute o comando de compilação do Cargo. Este comando compilará tanto o backend Rust quanto a interface Flutter.
        ```bash
        cargo run
        ```
    *   A primeira compilação pode levar um tempo considerável, pois o Cargo baixará e compilará todas as dependências do Rust. As compilações subsequentes serão muito mais rápidas.

5.  **Teste o Aplicativo**:
    *   Após a compilação bem-sucedida, o aplicativo será iniciado automaticamente.
    *   Verifique se todas as suas personalizações (logotipo, cores, etc.) aparecem corretamente.
    *   Teste a funcionalidade principal, como estabelecer uma conexão remota, para garantir que as alterações no servidor padrão estão funcionando.

6.  **Gere o Executável para Distribuição**:
    *   Para criar uma versão otimizada de lançamento (release), use o seguinte comando:
        ```bash
        cargo build --release
        ```
    *   O executável final estará localizado no diretório `target/release/`. Este é o arquivo que você distribuirá.

## 5. Como Gerar um Executável Confiável (Assinatura de Código)

Para evitar que seu aplicativo seja sinalizado como um vírus ou software não confiável pelo Windows e por programas antivírus, é crucial assinar digitalmente o executável. A assinatura de código (Code Signing) valida a identidade do desenvolvedor e garante que o código não foi adulterado.

### 5.1. Entendendo a Assinatura de Código

-   **O que é?**: É um processo que adiciona uma assinatura digital a um executável.
-   **Por que é importante?**:
    *   **Reputação**: Aumenta a confiança do usuário e do sistema operacional. O Windows SmartScreen, por exemplo, é menos propenso a bloquear aplicativos assinados.
    *   **Integridade**: Garante que o software não foi modificado desde que foi assinado.
    *   **Identidade**: Prova que o software veio de você, o desenvolvedor.

### 5.2. Opções de Certificado de Assinatura de Código

Certificados totalmente gratuitos de Autoridades Certificadoras (CAs) comerciais não são mais comuns. No entanto, existem alternativas de baixo custo e opções para cenários específicos:

1.  **Certificados Comerciais (Opção Padrão)**:
    *   **O que são**: Certificados emitidos por CAs confiáveis como Sectigo, DigiCert, etc.
    *   **Custo**: Geralmente, custam a partir de $200 por ano. Revendedores como o `Code Signing Store` podem oferecer preços mais competitivos.
    *   **Vantagens**: Oferecem a maior compatibilidade e confiança, removendo a maioria dos avisos de segurança.

2.  **OSSign (Para Projetos de Código Aberto)**:
    *   **O que é**: Um serviço que oferece assinatura de código gratuita para projetos de código aberto qualificados.
    *   **Custo**: Gratuito, mas requer um processo de aplicação e qualificação.
    *   **Vantagens**: É a opção ideal se o seu projeto for de código aberto e atender aos critérios deles.

3.  **Certificados Autoassinados (Para Testes)**:
    *   **O que são**: Certificados que você mesmo gera, sem a validação de uma CA.
    *   **Custo**: Gratuito.
    *   **Desvantagens**: Não são confiáveis para sistemas de usuários finais. O Windows e os antivírus exibirão avisos de segurança severos, pois a identidade não pode ser verificada. São úteis apenas para desenvolvimento e testes internos.

### 5.3. Processo de Assinatura no Windows

Depois de obter um certificado (geralmente um arquivo `.pfx`), você usará a ferramenta `signtool.exe`, que faz parte do Windows SDK.

1.  **Instale o Windows SDK**:
    *   Você pode instalá-lo através do [Visual Studio Installer](https://visualstudio.microsoft.com/downloads/), selecionando a carga de trabalho "Desenvolvimento para desktop com C++" e garantindo que o componente "Windows 10 SDK" ou "Windows 11 SDK" esteja marcado.

2.  **Localize o `signtool.exe`**:
    *   A ferramenta geralmente está localizada em um caminho como: `C:\Program Files (x86)\Windows Kits\10\bin\<versão>\x64\signtool.exe`.

3.  **Execute o Comando de Assinatura**:
    *   Abra o "Prompt de Comando do Desenvolvedor para VS" (Developer Command Prompt for VS) para ter o `signtool` no seu PATH.
    *   Use o seguinte comando para assinar seu executável:
        ```bash
        signtool sign /f "Caminho\Para\Seu\Certificado.pfx" /p "SuaSenhaDoCertificado" /tr http://timestamp.digicert.com /td sha256 /fd sha256 "Caminho\Para\Seu\target\release\rustdesk.exe"
        ```
    *   **Explicação dos Parâmetros**:
        *   `/f`: Especifica o arquivo do seu certificado.
        *   `/p`: A senha para o seu arquivo de certificado.
        *   `/tr`: O URL de um servidor de timestamp (carimbo de data/hora). Isso garante que a assinatura permaneça válida mesmo após o vencimento do certificado.
        *   `/td` e `/fd`: Especificam os algoritmos de hash (SHA256 é o padrão moderno).
        *   O último argumento é o caminho para o executável que você compilou.

Após a execução bem-sucedida, seu executável estará assinado digitalmente, aumentando significativamente sua confiabilidade.
