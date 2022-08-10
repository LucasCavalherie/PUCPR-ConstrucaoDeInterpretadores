# NOME: Lucas Fernando Assunção Cavalherie

# ENUNCIADO:
# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
# linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de 
# entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
#  {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
# O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
# contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de 
# entrada. As linhas subsequentes contém uma string por linha. 
# Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será 
# representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e 
# somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado 
# da validação conforme o formato indicado a seguir: 
# abbaba: não pertence.   
# A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será 
# composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída. 
# Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
# contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes 
# devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor 
# irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de 
# testes criado pelo próprio professor.  

def s0(palavra):
  if(len(palavra) == 0):
    print('- Pertence')
    return
    
  if(palavra[0] == 'a'):
    s1(palavra[1:])
    return
    
  if(palavra[0] != 'b' and palavra[0] != 'c'):
    print('- Não pertence')
    return
    
  s0(palavra[1:])
  

# Quando recebe um 'a' deve ser seguido de 'bb'
def s1(palavra):
  if(len(palavra) < 2 or palavra[0] != 'b' or palavra[1] != 'b'):
    print('- Não pertence')
    return
    
  s0(palavra[2:])
  


while True:
  print('\n=====================')
  nomeDoArquivo = input('Insira o arquivo para ser lido (ex: texto2.txt): ')
  
  try:
    arquivo = open(nomeDoArquivo, 'r')
  except:
    print('Arquivo inválido, tente novamente!')
    continue

  print('================')
  print('Lendo o Arquivo: ' + nomeDoArquivo)

  quantidade = arquivo.readline()
  print('Quantidade de strings a serem informadas: ' + quantidade)
   
  for i in range(int(quantidade)):
    palavra = arquivo.readline().rstrip('\n')
    print(palavra + ':')
    s0(palavra)
