# Instruções para Personalização do Aplicativo

Este documento detalha os passos necessários para personalizar o aplicativo com sua própria marca, incluindo logotipo, cores e configurações de servidor.

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
