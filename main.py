# PEDRA, PAPEL, TESOURA

import random
import sqlite3

# DATABASE OPÇÕES
conn = sqlite3.connect('opcoes.db')
cursor = conn.cursor()
  
cursor.execute(
  'CREATE TABLE IF NOT EXISTS opcoes (id INTEGER PRIMARY KEY AUTOINCREMENT, opcao TEXT)'
)
  
opcoes = ['pedra', 'papel', 'tesoura']

# DESAFIO HARDCORE MERMÃO
print(
  'Eu, computador, desafio-lhe para um jogo.\nEscolha entre pedra, papel ou tesoura.'
)

# VARIÁVEIS
Sair = False
vencedor = ''
pontos_vc = 0
pontos_pc = 0

# FUNÇÃO JOGAR
def jogar():
  for opcao in opcoes:
    cursor.execute('INSERT INTO opcoes (opcao) VALUES (?)', (opcao, ))
  
  conn.commit()
  
  cursor.execute('SELECT * FROM opcoes')
  result = cursor.fetchall()
  
  opcao_computador = random.choice(result)[1]

  global pontos_vc, pontos_pc
  
  print (100*'=')
  print ('\nPlacar:\nVocê {} x {} COMPUTADOR\n'.format(pontos_vc, pontos_pc))
  print (100*'=')
  
  jogada = input('\nEscolha a sua jogada:\n')
  print('\nMinha jogada:\n{}\n'.format(opcao_computador))
  print (100*'=')

  if jogada.upper() == opcao_computador.upper():
    print('\nEmpate.')
    pontos_vc += 1
    pontos_pc += 1
  else:
    if jogada.upper() == 'PEDRA' and opcao_computador.upper() == 'TESOURA':
      print('\nPedra quebra Tesoura, portando você venceu.')
      pontos_vc += 1
    else:
      if jogada.upper() == 'TESOURA' and opcao_computador.upper() == 'PEDRA':
        print('\nPedra quebra Tesoura, portando eu venci.')
        pontos_pc += 1
      else:
        if jogada.upper() == 'TESOURA' and opcao_computador.upper() == 'PAPEL':
          print('\nTesoura corta papel, portando você venceu.')
          pontos_vc += 1
        else:
          if jogada.upper() == 'PAPEL' and opcao_computador.upper(
          ) == 'TESOURA':
            print('\nTesoura corta Papel, portando eu venci.')
            pontos_pc += 1
          else:
            if jogada.upper() == 'PAPEL' and opcao_computador.upper(
            ) == 'PEDRA':
              print('\nPapel cobre Pedra, portando você venceu.')
              pontos_vc += 1
            else:
              if jogada.upper() == 'PEDRA' and opcao_computador.upper(
              ) == 'PAPEL':
                print('\nPapel cobre Pedra, portando eu venci.')
                pontos_pc += 1
              else:
                print(
                  '\nJoga esse negócio direito aí 2, digita coisa aleatória não 😠.'
                )
  print ('')
  print (100*'=')
  
# FUNÇÃO PARA CONTINUAR
def continuar():
  sair = input('\nDeseja continuar? (s / n):\n')

  if sair.upper() == 'S':
    Sair = False
  else:
    Sair = True
  return Sair
  
# LOOP JOGAR
while True:
  jogar() 
  Sair = continuar()
  if Sair == True:
    break
