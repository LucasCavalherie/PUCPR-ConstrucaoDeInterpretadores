# Lucas Fernando Assunção Cavalherie

while True:
  print('\n=====================')
  nomeDoArquivo = input('Insira o arquivo para ser lido: ')
  
  try:
    arquivo = open(nomeDoArquivo, 'r')
  except:
    print('Arquivo inválido, tente novamente!')
    continue

  print('================')
  print('Lendo o Arquivo: ' + nomeDoArquivo)

  alfabetoPermitido = ['a', 'b', 'c']
  quantidade = arquivo.readline()
  print('Quantidade de strings a serem informadas: ' + quantidade)
  
  
  for i in range(int(quantidade)):
    error = False
    palavra = arquivo.readline().rstrip('\n')
    for j in range(len(palavra)):
      if(palavra[j] not in alfabetoPermitido):
        error = True
        
      if(palavra[j] == 'a'):
        if(j >= len(palavra) - 2 or 
           palavra[j+1] != 'b' or 
           palavra[j+2] != 'b'):
          error = True
  
    if(error):
      print(palavra + ' : não pertence')
    else:
      print(palavra + ' : pertence')
        