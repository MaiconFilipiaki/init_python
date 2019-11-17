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

convites_com_valor = { 'vip': 60, 'norma': 40, 'meia': 30, 'cortesia': 0 }
convites_com_valor['vip'] # <- acessar valor

convites_com_valor.keys() # <- retorna somente as keys
convites_com_valor.values() # <- retorna somente os valores das keys