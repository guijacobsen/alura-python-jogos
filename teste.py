
# inteiros = [1,2,3,4,5,5,6,8,9,11,12]

# # lista = []
# # for n in inteiros:
# #     if( not n%2 ):
# #         lista.append(n)

# lista = [n for n in inteiros if not n%2]

# print('inteiros: ', inteiros)
# print('lista: ', lista)


file = open("palavras.txt", "r")

# content = file.read()
# print(content)

for linha in file:
    print(linha)

# file.write("melancia\n")
# file.write("banana\n")
# file.write("uva\n")
# file.write("morango\n")
# file.write("carro\n")
# file.write("macaco\n")
# file.write("cachorro\n")

file.close()