def soma(n1: float, n2: float) -> float:
    return n1 + n2

def subtracao(n1: float, n2: float) -> float:
    return n1 - n2

def multiplicacao(n1: float, n2: float) -> float:
    return n1 * n2

def divisao(n1: float, n2: float) -> float | str:
    if n2 == 0:
        return "Erro: Divisão por zero"
    return n1 / n2

def obter_numero(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def calculadora():
    operacoes = {
        '1': ('Soma', soma),
        '2': ('Subtração', subtracao),
        '3': ('Multiplicação', multiplicacao),
        '4': ('Divisão', divisao)
    }

    while True:
        print('\n' + '='*30)
        print('CALCULADORA SIMPLES')
        print('Operações disponíveis:')
        for chave, (nome, _) in operacoes.items():
            print(f'{chave} - {nome}')
        print('5 - Sair')
        print('='*30)
        
        opcao = input('Escolha a operação (1-5): ').strip()
        
        if opcao == '5':
            print('Saindo da calculadora. Até logo!')
            break
            
        if opcao in operacoes:
            n1 = obter_numero('Insira o primeiro número: ')
            n2 = obter_numero('Insira o segundo número: ')
            
            nome_op, funcao_op = operacoes[opcao]
            resultado = funcao_op(n1, n2)
            
            print(f'\nResultado da {nome_op.lower()}: {resultado}')
        else:
            print('Operação inválida. Tente novamente.')

if __name__ == "__main__":
    calculadora()
