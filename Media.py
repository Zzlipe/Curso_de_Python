# Programa de media
# Desenvolvido por lipe

print("**************************************")
print("*           Media Escolar            *")
print("**************************************")

# CRIAÇÃO DAS VARIÁVEIS

nome= ""
primeiro_bimestre = 0.0
segundo_bimestre = 0.0
terceiro_bimestre = 0.0
quarto_bimestre = 0.0


#Entrada dos Dados
nome = input("Digite o seu nome: ")
nota_bimestre_1 = float(input("Digite a sua nota do 1 Bimestre: "))
nota_bimestre_2 = float(input("Digite a sua nota do 2 Bimestre: "))
nota_bimestre_3 = float(input("Digite a sua nota do 3 Bimestre: "))
quarto_bimestre = float(input("Digite a sua nota do 4 Bimestre: "))


# Processar os valores para obter IMC
media = (nota_bimestre_1 + nota_bimestre_2 + nota_bimestre_3 + quarto_bimestre)/4

situacao = ""

#YERR
if media >= 7.0:
    situacao = "APROVADO, PARABENS"
elif media < 5:
    situacao = "RECUPERÇÃO, VOCÊ AINDA TEM UMA CHANCE"
else:
    situacao = "REPROVADO, SE ESFORCE MAIS DA PROXIMA"


# Resultado do precessameto
print ()
print ("********************************")
print ("-          Resultado           -")
print ()
print ("NOME: " + nome)
print ("MEDIA: " + str (media)+ " Media Final")
print (f"Olà {nome}, você está {situacao}, com Média {media}")
print ()
print ("********************************")
