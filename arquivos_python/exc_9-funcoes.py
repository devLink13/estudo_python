# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(*parciais, sit='False'):
    """
    :param parciais: empacotamento de notas parciais, coloque tantas notas quanto necessárias.
    :param sit: valor opcional, serve para mostrar a situação do aluno (aprovado, reprovado ou em recuperação)
    :return notas: retorna um dicionário contendo as informações do aluno.

    developed by Wesley Link
    """

    menor = 0
    soma = 0
    notas = dict()

    total_parciais = len(parciais)
    notas['total'] = total_parciais

    maior_parcial = max(parciais)
    notas['maior'] = maior_parcial

    for i, nota in enumerate(parciais):
        if i == 0:
            menor = nota
        if nota < menor:
            menor = nota
    notas['menor'] = menor

    # posso calcular o menor número da tupla da maneira acima ou usando a função min()
    # tanto faz, bom saber os dois

    # menor = min(parciais)

    for nota in parciais:
        soma = soma + nota
    media = soma / len(parciais)
    notas['media'] = media

    if sit == True:

        if media >= 6:
            notas['Situação'] = 'aprovado'
        elif media >= 4:
            notas['Situação'] = 'exame'
        elif media < 4:
            notas['Situação'] = 'reprovado'

    return notas


print(notas(0, 1, 10, 5, sit=True))
help(notas)
