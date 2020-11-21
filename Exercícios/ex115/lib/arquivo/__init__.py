def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro, arquivo não foi criado.')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<33}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, n='Desconhecido', i=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve erro ao abrir o arquivo.')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('Houve erro ao cadastrar o indivíduo.')
        else:
            print(f'{n} cadastrado com sucesso.')
