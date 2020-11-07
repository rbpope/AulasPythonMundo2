def fatorial(n, show=False):
    """
        -> O fatorial de um número é calculado pela multiplicação desse número
        por todos os seus antecessores até chegar ao número 1.
        Note que nesses produtos, o zero (0) é excluído.
        O fatorial é representado por: n! = n. (n – 1). (n – 2). (n – 3)!
        :param n: O número a ser calculado
        :param show: (opcional) Mostrar ou não a conta
        :param return: o retorno do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' X ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


n = int(input('Digite um número: '))
print(fatorial(n, True))

