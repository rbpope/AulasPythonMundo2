nome = str(input('Como é o nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
n3 = float(input('Digite a terceira nota do aluno: '))
ma = float(input('Digite a nota média para aprovação da instituição: '))
mr = float(input('Qual a nota média para reprovação da instituição: '))
m = float((n1 + n2 + n3) / 3)
'''ma = float(7.0)
mr = float(5.0)'''
if m >= ma:
    print('==='*20)
    print('{}, sua média foi {:.2f} e você está Aprovado, Boas Férias!!!'.format(nome, m))
    print('==='* 20)
elif mr <= m < ma:
    print('=' * 50)
    print('{}, sua média foi {:.2f}. Vamos fazer recuperação!!!'.format(nome,m))
    print('='* 50)
elif  m < mr:
    print('=' * 50)
    print('{}, sua média foi {:.2f} e você foi Reprovado!!!'.format(nome, m))
    print('='* 50)
