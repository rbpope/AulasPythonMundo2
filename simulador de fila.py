import random  # biblioteca para geração de números aleatórios
from matplotlib import pyplot as plt  # biblioteca gráfica
from termcolor import colored  # biblioteca para impressão colorida
from random import randint
random.seed(1)  # define semente fixa para geração de números pseudo-aleatórios
dist = int(input('Qual a distribuição de hora do próximo cliente(em segundos): ')) #item 1
qtde_caixas = int(input('Selecione a quantidade de caixas: ')) #item 2
#cx_priori = 2

idade = randint(15, 95) # define se o paciente é idoso
if idade >= 65:
    cliente = 'idoso'
else:
    cliente = 'não idoso'
print(cliente)
cx_priori = round(0.2 * qtde_caixas)
if cx_priori < 1:
  cx_priori = 1
print(f'O número de caixas prioritários é {cx_priori}')
'''while cx_priori != 0 and cx_priori != 1:
  cx_priori = int(input('Digite "1" para acrescentar 1 caixa para terceira idade ou "0" para continuar sem caixa adicional: ')) #item 3'''# Substituí para sempre ter pelo menos um caixa prioritário

if cx_priori == 1:       #item 4
  nao_idoso = int(input('Digite "1" se o caixa para terceira idade for exclusivo ou "0" se qualquer um puder usar caso não haja idoso na fila: '))

# Horário corrente (inteiro, em segundos) começa em zero.
# (instante 0 da simulação)
horario = 0

# A lista de eventos começa, de início, com um único evento: a chegada de um
# cliente. Este evento está programado para ocorrer no instante 0.
eventos = [-1]  # aqui marcamos o tipo do evento (-1 = chegada de um cliente)
horario_eventos = [0]  # aqui marcamos o instante programado para o evento.

# Aqui está o estado inicial dos postos de atendimento (caixas).
# Ao colocar aqui uma lista de 3 elementos, estamos dizendo que o banco tem 3 caixas.
# Para aumentar o número de caixas, basta aumentar esta lista.
caixas = []
x=1
while x <= qtde_caixas:
  caixas.append('livre') #Modificação 2 do professor
  x += 1

# A fila de atendimento começa vazia (nenhum cliente esperando na fila).
fila = []

# Não há registros de tempos de espera pelos clientes.
# Nenhum cliente foi devidamente atendido ainda.
tempos_espera = []

# Trata eventos programados durante as 3 primeiras horas (loop com uso do WHILE).
# No intante "3 horas", encerra a simulação.
while horario < 60 * 60 * 3:  # 60 segundos * 60 minutos * 3 horas

    # Descobre qual o próximo evento a tratar na lista de eventos.
    # (-1 = chegada de cliente, 0, 1, 2... = término de# atendimento em um caixa).
    # Para tanto procura em horario-eventos o horário mais próximo (o menor deles).
    # Apaga o evento e o horário do eventos das respectivas listas.
    pos = horario_eventos.index(min(horario_eventos))  # index do próximo evento
    evento = eventos[pos]  # obtém evento
    horario = horario_eventos[pos]  # obtém horário do evento
    print(colored("\nRelógio marca agora: " + str(round(horario, 1)) + " segundos.", "magenta"))
    if evento == -1:
        e = "chegada de cliente"
    else:
        e = "término de atendimento no caixa " + str(evento)
    print("Tratando agora o evento = " + e)
    eventos.pop(pos)  # apaga o referido evento da lista de eventos
    horario_eventos.pop(pos)  # apaga horário do evento na lista dos horários

    # **** Tratamento do evento CHEGADA DE UM NOVO CLIENTE   *****
    if evento == -1:

        # Programa a chegada de um próximo cliente após um tempo aleatório.
        eventos.append(-1)
        h = horario + random.expovariate(1 / dist)  # exponencial, especificando média = 70 seg
        # Algumas outras possibilidades para determinar o horário de chegada do próximo cliente:
        # h = horario + random.gauss(mu,sigma)   # normal, especificando média e desvio-padrão
        # h = horario + random.expovariate(1/mu) # exponencial, especificando a média
        horario_eventos.append(h)
        print("Programado evento de chegada de NOVO cliente aos", round(h, 1), "segundos")

        # Se há caixa livre, programa o evento do término do atendimento desse cliente
        # recém chegado neste caixa.
        # Se não há caixa livre, cliente vai para fila de espera.
        if "livre" in caixas:  # verifica aqui se há caixa livre
            i = caixas.index("livre")  # em havendo caixa livre, descobre qual caixa
            caixas[i] = "ocupado"  # o caixa passa a estar acupado agora
            eventos.append(i)  # gera evento do término do atendimento
            h = horario + random.gauss(180, 30)  # normal, especificando média e dp
            horario_eventos.append(h)  # registra o horário programado para o final desse atendimento
            tempos_espera.append(0)  # registra a espera deste cliente (0 seg, porque não ficou na fila!)
            print("Programado NOVO evento de final de atendimento no caixa ", i, " aos", round(h, 1), "segundos")
        else:
            fila.append(horario)  # estando todos os caixas ocupados,
            # põe cliente na fila (anota-se na fila o
            # o instante de chegada deste cliente)

    # **** Tratamento do evento Término do Atendimento de um Cliente no Caixa   *****
    if evento != -1:
        i = evento  # i passa a guardar o número do caixa que sendo liberado agora.
        if len(fila) == 0:  # Caixa foi liberado, mas não há cliente.
            caixas[i] = "livre"  # na fila --> muda status deste caixa para livre.
        else:
            # Havendo cliente na fila, registra quantos minutos ele esperou
            # para ser atendido e registra essa informação.
            # Retira o cliente da fila.
            # Programa o final do atendimento do novo cliente nesse caixa.
            tempos_espera.append((horario - fila[0]) / 60)  # espera = agora - chegada
            del fila[0]
            eventos.append(i)
            y = horario + random.gauss(180, 30)
            horario_eventos.append(y)
            print("Programado NOVO evento de final de atendimento no caixa ", i, " aos", round(y, 1), "segundos")

    # **** Ao final do tratamento do evento (qualquer que seja ele) *****
    print("Tamanho da fila = ", len(fila))  # imprime tamanho da fila
    print("Caixas: ", caixas)  # imprime situação dos caixas

#  Terminado o período de simulação, imprimimos os resultados-resumo da simulação.
print()
print("**** Tempo máximo de espera na fila (minutos): ", round(max(tempos_espera), 1))
print("**** Tempo médio de espera na fila (minutos): ", round(sum(tempos_espera) / len(tempos_espera), 1))
print()
print()

# gera histograma dos tempos de espera na fila
plt.hist(tempos_espera, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.title('Histograma dos tempos de espera na fila')
plt.xlabel("Tempo de espera na fila para ser atendido (minutos)")
plt.ylabel("Contagem de clientes")
plt.grid(True)
plt.show()

# gera line plot dos tempos de espera na fila
plt.plot(tempos_espera, color="r")
plt.title('Timeplot dos tempos de espera na fila')
plt.xlabel("Número de ordem de chegada dos clientes")
plt.ylabel("Tempo de espera na fila para ser atendido (minutos)")
plt.grid(True)
plt.show()