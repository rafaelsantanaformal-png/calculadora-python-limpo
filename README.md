# Calculadora Interativa em Python (Clean Code & Robustez)

Este projeto é uma calculadora via linha de comando desenvolvida em Python. Mais do que realizar operações matemáticas simples, o objetivo principal deste projeto foi aplicar **boas práticas de desenvolvimento**, garantindo um código limpo, escalável e imune a quebras por erros de usuários.

##  Diferenciais Técnicos Aplicados (O que este projeto demonstra):

*   **Tratamento de Exceções (`try/except`):** O sistema possui validação robusta de dados. Se o usuário digitar letras ou caracteres inválidos no lugar de números, o programa captura o erro amigavelmente e solicita uma nova entrada, impedindo o travamento do software.
*   **Escalabilidade com Dicionários (Mapeamento de Funções):** Substituí estruturas complexas e extensas de `if/elif` por um dicionário que armazena referências diretas das funções. Isso torna a adição de novas operações rápida e limpa (padrão de arquitetura escalável).
*   **Tipagem de Dados (Type Hints):** Uso de documentação estática nos argumentos e retornos das funções, facilitando a leitura do código e o uso de ferramentas de análise estática.
*   **Segurança Operacional:** Tratamento explícito para evitar o erro matemático de divisão por zero.
*   **Modularização:** Código estruturado sob a proteção de execução `if __name__ == "__main__"`, permitindo que as funções matemáticas sejam importadas por outros sistemas sem executar o menu principal por acidente.

## Tecnologias Utilizadas
*   Python 3.x
*   Conceitos de Clean Code, Dicionários estruturais e Blocos Try/Except.

