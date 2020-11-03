aluno = dict()

aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('-='*30)
print(f'O aluno {aluno["nome"]} tem média {aluno["média"]} e sua situação é: {aluno["situação"]}.')
print('-='*30)
for k, v in aluno.items():
    print(f' - {k} é {v}.')
