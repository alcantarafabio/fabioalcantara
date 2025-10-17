# Tuplas são imutáveis.

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5,2,6,8,4,5,6,7,4,0,12,22,3,4,5)
print(max(t1))

# Operações não disponíveis em tuplas: .sort(), .append(), .reverse(), pop()...
# Enfim, todos os métodos que alteram o conteúda da tupla não estão disponíveis.

# Iteração
# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# Para criar uma lista

# grupo17 = list(halogenios)
# grupo17[0] = 'h'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(type(alcalinos))

# Como não podemos alterar o conteúdo de uma tupla, tão pouco conseguimos alterar a ordem dos elementos.
# Mas podemos criar uma nova tupla com os elementos classificados.

print(sorted(alcalinos)) # Ordem alfabéticas


