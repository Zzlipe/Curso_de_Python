    # Programa para calcular IMC
# Desenvolvido por lipe

print("**************************************")
print("*          Calculadora de IMC        *")
print("**************************************")

# CRIAÇÃO DAS VARIÁVEIS

nome= ""
peso= 0
altura = 0.0
imc= 0.0

#Entrada dos Dados
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float (input("Digite a sua altura: "))

# Processar os valores para obter IMC
imc = peso / altura ** 2

situacao = 0.0

if imc < 18.5:
    situacao = "Você está baixo do peso"
elif imc >= 18.5:
    situacao = "Você está com peso nomral"
elif imc >= 24.9:
    situacao = "Você esta acima do peso"
elif imc >= 29.9:
    situacao = "Você está com obsidade grau 1"
elif imc >= 34.9:
    situacao = "Você tem obesidade grau 2"
elif imc >= 40:
    situacao = "Você tem obesidade Morbida"
# Resultado do precessameto
print ()
print ("********************************")
print ("*         Resultado            *")
print ()
print ("NOME: " + nome)
print ("PESO: " + str (peso)+ "kg")
print ("Altura: " + str (altura) + "m")
print ("IMC: " + str (imc))
print (f"Olà {nome}, {situacao}.")
print ()
print ("********************************")
