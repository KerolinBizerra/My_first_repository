frase = 'Curso em Vídeo Python'

#print(frase[3]) 
#fatiamento, mostra a quarta letra da frase.and

#print(frase[3:13]) 
#mostra do quarto caractere até o 12º

#print(frase[9:21:2]) 
#começa no índice 9 até o 21, saltando duas casas.

#print(frase[:5])
#começa do primeiro índice até o 4.

#print(frase[15:])
#Mostra a partir do 15 até o último caractere.

#print(frase[9::3])
#Mostra a partir do índice 9, até o final, pois não foi informado nenhum valor, saltando 3 casas.

#print(len(frase))
#Exibe a quantidade de caracteres

#print(frase.count('o'))
#Exibe a quantidade de caracteres 'o' na var

#print(frase.count('o', 0, 13))

#Para não escrever vários prints, basta colocar o print('''E digitar o texto, com quebra de linhas caso queira.''')

#print(frase.find('reo'))
#Retorna a posição que está a string digitada. Se retornar -1 é por que não foi encontrada.

#print('Curso' in frase)
#Realiza a pergunta dentro da variável eu enho a string 'curso'? Se sim, retornará true, se não false.

#print(frase.replace('Python', 'Android'))

#Ele vaiprocurar pela string 'Python e trocar para Android'

#print(frase.upper().count('O'))
#Pega a frase, coloca em maiúsculo e conta quantos 'O' tem.

#print(frase.lower())
#Ele transforma em minúsculo

#print(frase.capitalize())
#Deixa somente o primeiro caractere em maiúsculo.

#print(frase.title())
#Deixa o primeiro caractere e os que sucederem os espaços em Maiúsculo.

#print(frase.strip())
#Remove todos os espaços inúteis no inicio e no final da string.

#print(frase.rstrip())
#Remove somente os últimos espaços se houverem espaços no inicio ele deixa e exclui os outros

#print(frase.lstrip())
#igual ao rstrip só que na esquerda

#print(frase.split())
#dentro da frase ele transforma cada inicio de palavra em uma nova lista

#print('-'.join(frase))
#Une a string que antes estava separada em uma única cadeia de caracteres com o '-'
