convites = 12

convites_ano_passado = 20

convites, convites_ano_passado = 12,20

convites = 10L # <- numeros maiores que o permitido

salario = 7500.50j # <- numeros maiores que o permitido

# Python tem o mesmo contexto que o ECMA, dando faz a string
perfil_aspas_duplas = "Maicon Douglas"
perfil_aspas_simples = 'Maicon Douglas'

perfil_aspas_simples[0:2] # <- slice

primeiro_nome = perfil_aspas_simples[0:7] # <- passando valor do slice pra dentro de outra var

idade = 22

convite = 'Maicon Douglas Filipiaki'

'Convite do ' + perfil_aspas_simples 
# Estouro de TypeError (Nao deixa uma var int, float com string)
# Usar print
'Convite do ' + perfil_aspas_simples + ' com idade ' + idade
print('Convite do %s com idade %s' % (convite, idade))


convite1 = 'Maicon Douglas Filipiaki'
convite2 = 'Jose'
convite3 = 'Joao'

convites = ['Maicon Douglas Filipiaki', 'Jose', 'Joao']

convites[0]
convites[1]
convites[2]

convites[0:2]
convites[1:]
convites.append('Vitor')
convites.append(10)
convites.remove(10)
convites.remove('Vitor')


tipos_convite = ['vip', 'normal', 'meia', 'cortesia']
tipos_convite = ('vip', 'normal', 'meia', 'cortesia') # <- Tuple listas que nao podem ser mudadas, nao podem ser add e nem remover itens
tipos_convite.append('Teste')
tipos_convite.remove('vip')

#Dicionarios
convites_com_valor = { 'vip': 60, 'norma': 40, 'meia': 30, 'cortesia': 0 }
convites_com_valor['vip'] # <- acessar valor

convites_com_valor.keys() # <- retorna somente as keys
convites_com_valor.values() # <- retorna somente os valores das keys

convite = 'Maicon Douglas'
parte1 = convite[0:4]
parte2 = convite[10:14]

print '%s %s' % (parte1, parte2)

convite = 'Maicon Douglas Filipiaki'
posicao_final = len(convite)
posicao_inicial = posicao_final - 4
parte1 = convite[0:4]
parte2 = convite[posicao_inicial:posicao_final]

print '%s %s' % (parte1, parte2)




# pegar coisas digitadas
nome = raw_input() # <- vai tratar o terminal e esperar pela entrada, sempre retorna uma string
ano = raw_input()
# Para mudar o formato de uma string pra int 
ano_como_int = int(ano)
# Converte int para string
ano_teste = str(ano_como_int)

nomes = []
nome = raw_input()
nomes.append(nome)



#import a biblioteca que faz o controle das Regex
import re

re.match('Py', 'Python') # primeiro par e oq vai ser procurado, segundo a frase em questao para ver se confere
resultado = re.match('Py', 'Python')
resultado.group() # se tiver algo vai retorna
# senao vai dar um erro de NoneType
resultado = re.match('[pP]y', 'Python') #digo que a letra pode ser tanto maiúscula como minúscula
resultado = re.match('[A-Za-z]y', 'Python') # busca palavras que comecam de a - z
resultados = re.findall('[A-Za-z]y', 'Python pu jython') #pega todas as ocorrencias
resultados = re.findall('[A-Za-z]y[A-Za-z]+', 'Python pu jython') # retorna a palavra inteira
resultados = re.findall('\wy\w+', 'Python pu jython') # vai retorna qualquer coisa que tenha letra ou numero
