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
