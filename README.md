# p0_Basico
Extrair e-mails, telefones e URLs de um texto


## Problema escolhido:
    Extrair automaticamente dados de contato (e-mails, telefones e URLs) presentes em textos não estruturados. Exemplos de uso incluem mensagens recebidas por e-mail, anúncios, formulários, documentos e notas contendo informações de contato misturadas ao texto.

## Usuário ou público-alvo:
    O projeto é destinado a pessoas ou organizações que precisam localizar rapidamente informações de contato em textos sem realizar a busca manual.
    Exemplos:
    - estudantes;
    - profissionais administrativos;
    - pequenos negócios;
    - usuários que precisam organizar informações recebidas por mensagens ou documentos.


## Justificativa para não utilização de LLM:
    Apesar de a disciplina abordar a utilização de Modelos de Linguagem de Grande Escala (LLMs), neste P0-Básico optou-se por não utilizar um LLM, conforme video explicativo.
    A justificativa técnica é que o problema escolhido possui padrões bem definidos e previsíveis:

    - e-mails seguem estruturas conhecidas;
    - telefones seguem formatos padronizados;
    - URLs possuem sintaxe própria.
    Essas características permitem a utilização de expressões regulares (Regex), que resolvem o problema de forma simples, eficiente e determinística.
    Assim, o uso de um LLM nesta etapa aumentaria a complexidade da solução sem oferecer benefícios significativos.
    Nas próximas etapas do projeto (P0-Intermediário e P0-Avançado), pretende-se introduzir um modelo de linguagem para resolver problemas que exijam interpretação semântica e compreensão contextual do texto.


## Funcionamento da solução:
    O fluxo de execução é composto pelas seguintes etapas:

    1. O usuário fornece um texto pelo terminal.
    2. O sistema aplica expressões regulares para localizar: 
    - e-mails;
    - telefones;
    - URLs.
    3. Os dados encontrados são organizados.
    4. O resultado é exibido na tela.

    Fluxo simplificado;
    Texto de entrada
    ↓
    Processamento com Regex
    ↓
    Extração das informações
    ↓
    Exibição dos resultados


## Limites do projeto:
    O sistema foi desenvolvido com foco em formatos comuns de contato.
    O projeto não realiza:

    - validação da existência dos e-mails;
    - verificação de URLs acessíveis;
    - validação de números telefônicos;
    - interpretação de informações escritas de maneira ambígua.


## Pré-requisitos:

    - Python 3.10 ou superior
    Clonar o repositório
    git clone https://github.com/SEU-USUARIO/extrator-contatos.git
    cd extrator-contatos

## Configuração do acesso ao LLM

    Nesta etapa (P0\-Básico) não há integração com modelos de linguagem.

    A escolha foi intencional, pois o problema pode ser resolvido adequadamente utilizando expressões regulares (Regex).

    Dessa forma, não são necessárias:

    - chaves de API;
    - tokens de autenticação;
    - variáveis de ambiente;
    - configuração de provedores de IA.

    A integração com um LLM será realizada nas próximas etapas do projeto.

## Execução:
    Execute o arquivo principal;
    python p0_basico.py
    Uma janela será aberta permitindo inserir o texto para análise.
    Após clicar no botão de extração, os e-mails, telefones e URLs identificados serão exibidos na interface

## Exemplos de Entrada e Saída

    # Exemplo 1

    ## Entrada

    ```text
    Olá!

    Meu e-mail é maria.silva@email.com.
    Meu telefone é (11) 98765-4321.

    Nosso site é https://www.empresa.com.br.
    ```

    ## Saída

    ```text
    E-mails encontrados:
    - maria.silva@email.com

    Telefones encontrados:
    - (11) 98765-4321

    URLs encontradas:
    - https://www.empresa.com.br
    ```

    ---

    # Exemplo 2

    ## Entrada

    ```text
    Entre em contato pelo endereço suporte@exemplo.com ou visite www.exemplo.com.
    ```

    ## Saída

    ```text
    E-mails encontrados:
    - suporte@exemplo.com

    Telefones encontrados:
    Nenhum encontrado.

    URLs encontradas:
    - www.exemplo.com
    ```

## Execução dos Testes:

    Para executar os testes automatizados;

    pytest

    Exemplo de resultado esperado;
    ========================================= test session starts===============================================
    platform win32 -- Python 3.13.4, pytest-9.2.0, pluggy-1.7.0
    rootdir: ...\MeusProjetos\p0_Basico
    collected 4 items                                                                                                                                                                                                                                

    tests\test_extracao.py ....                                                                                                                                                                                                                 [100%]

    ===================================== 4 passed in 0.23s ======================================================

    Os testes verificam:

    - extração correta de e\-mails;
    - extração correta de telefones;
    - extração correta de URLs;
    - comportamento quando o texto não contém informações de contato.

## Limitações Conhecidas

    A versão atual possui as seguintes limitações:

    - Nem todos os formatos internacionais de telefone são reconhecidos.
    - URLs contendo caracteres especiais podem exigir ajustes na expressão regular.
    - O sistema identifica padrões de texto, mas não valida se o e\-mail ou telefone realmente existe.
    - O sistema não detecta informações de contato escritas por extenso (por exemplo: "meu e\-mail é joão arroba empresa ponto com").
    - Não há integração com banco de dados ou serviços externos.
    - Não há interpretação semântica do texto, pois não é utilizado um modelo de linguagem nesta versão.

    Essas limitações poderão ser reduzidas nas próximas etapas do projeto com a introdução de técnicas mais avançadas de processamento de texto e, quando justificável, do uso de LLMs.


