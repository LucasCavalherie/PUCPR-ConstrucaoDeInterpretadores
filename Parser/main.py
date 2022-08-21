# NOME: Lucas Fernando Assunção Cavalherie

import re

constantesValores = ["T", "F"]
operadorUnario = "\lneg"
operadoresBinario = ["\lor", "\land", "\Rightarrow", "\Leftrightarrow"]
abreParen = "("
fechaParen = ")"


def Formula(indiceAtual, status):
    if vetorDeParametros[indiceAtual] == abreParen:
        status = AbreParen(indiceAtual)
    elif vetorDeParametros[indiceAtual] == fechaParen:
        status = FechaParen(indiceAtual)
    elif vetorDeParametros[indiceAtual] == operadorUnario:
        status = FormulaUnaria(indiceAtual)
    elif vetorDeParametros[indiceAtual] in operadoresBinario:
        status = FormulaBinaria(indiceAtual)
    elif vetorDeParametros[indiceAtual] not in constantesValores:
        status = Proposicao(indiceAtual)

    if status and (indiceAtual != ultimoIndice):
        status = Formula(indiceAtual + 1, status)

    return status


def Proposicao(indiceAtual):
    result = re.search("[a-z]|[a-z]+[0-9]", vetorDeParametros[indiceAtual])
    if not result:
        return False

    return True


def AbreParen(indiceAtual):
    global contadorDeParentes
    contadorDeParentes = contadorDeParentes + 1

    if (
            (indiceAtual > ultimoIndice - 1) or
            (vetorDeParametros[indiceAtual + 1] == operadorUnario) or
            (vetorDeParametros[indiceAtual + 1] in operadoresBinario)
    ):
        return False

    return True


def FechaParen(indiceAtual):
    global contadorDeParentes
    contadorDeParentes = contadorDeParentes - 1

    if (contadorDeParentes < 0):
        return False

    return True


def FormulaUnaria(indiceAtual):
    if (
            (indiceAtual == ultimoIndice) or
            (vetorDeParametros[indiceAtual + 1] == fechaParen) or
            (vetorDeParametros[indiceAtual + 1] in operadoresBinario)
    ):
        return False

    return True


def FormulaBinaria(indiceAtual):
    if (
            (indiceAtual == ultimoIndice) or
            (vetorDeParametros[indiceAtual + 1] == fechaParen) or
            (vetorDeParametros[indiceAtual + 1] in operadoresBinario)
    ):
        return False

    if (
            (indiceAtual == 0) or
            (vetorDeParametros[indiceAtual - 1] == abreParen) or
            (vetorDeParametros[indiceAtual - 1] == operadorUnario) or
            (vetorDeParametros[indiceAtual - 1] in operadoresBinario)
    ):
        return False

    return True


while True:
    print('\n=====================')
    nomeDoArquivo = input('Insira o arquivo para ser lido (ex: formulas1.txt): ')

    try:
        arquivo = open(nomeDoArquivo, 'r')
    except:
        print('Arquivo inválido, tente novamente!')
        continue

    print('================')
    print('Lendo o Arquivo: ' + nomeDoArquivo)

    quantidade = arquivo.readline()
    print('Quantidade de formulas a serem informadas: ' + quantidade)

    for i in range(int(quantidade)):
        vetorDeParametros = arquivo.readline().rstrip('\n').split()
        ultimoIndice = len(vetorDeParametros) - 1
        contadorDeParentes = 0
        status = Formula(0, True)
        if status and contadorDeParentes == 0:
            print('Válido')
        else:
            print('Inválido')

    break
