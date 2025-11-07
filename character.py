#FPSemana01

lista_grande = []
for i in range (3):
    array_do_personagem = []
    tuplo_dos_valores = ()

    nome_do_personagem = str(input())
    valor_de_ataque = int(input())
    valor_de_defesa = int(input())
    tuplo_dos_valores = (valor_de_ataque, valor_de_defesa)
    array_do_personagem.append (nome_do_personagem[:])
    array_do_personagem.append (tuplo_dos_valores[:])
    lista_grande.append (array_do_personagem[:])
    array_do_personagem.clear

personagem_maior_ataque = ['nome', 0]
personagem_maior_defesa = ['nome', 0]
for personagem in lista_grande: 
    if personagem[1][0] >= personagem_maior_ataque[1]: 
        personagem_maior_ataque[0] = personagem[0]
        personagem_maior_ataque[1] = personagem[1][0]
    if personagem[1][1] >= personagem_maior_defesa[1]: 
        personagem_maior_defesa[0] = personagem[0]
        personagem_maior_defesa[1] = personagem[1][1]

print(lista_grande)
print("Ataque" ,personagem_maior_ataque[0] ,personagem_maior_ataque[1], "\nDefesa",personagem_maior_defesa[0] ,personagem_maior_defesa[1] )
#print("Ataque " ,personagem_maior_ataque[0] ,personagem_maior_ataque[1])


