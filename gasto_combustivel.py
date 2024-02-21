#
print ("--------------------------------")
print ("*    CONSUMO DE COMBUSTÍVEL    *")
print ("--------------------------------")

#

modelo_do_carro="" 
combustivel=0
distancia_percorrida=0
preco_do_combustivel=0.0

#
modelo_do_carro=input("Modelo do veículo: ")
combustivel=int(input("autonomia do carro: "))
distancia_percorrida=float(input("Distância da viagem: "))
preco_do_combustivel=float(input("Preço do combustivel: "))

#
quantidade_de_combustivel_utilizado = distancia_percorrida / combustivel
total_gasto_na_viagem = (distancia_percorrida / combustivel) * preco_do_combustivel

#
print ("--------------------------------")
print ("*          RESULTADO           *")
print ("--------------------------------")
print (f"Modelo do carro: {modelo_carro}")
print (f"Autonomia do carro : {combustivel} km/1")
print (f"Distancia percorrida: {distancia_percorrida} km")
print (f"Valor do combustivel: R$ {preco_do_combustivel}")
print ("--------------------------------")
print (f"Quantidade de combustível utilizado:  {quantidade_de_combustivel_utilizado}")
print (f"Total gasto com a viagem: R$ {total_gasto_na_viagem}")
print ("--------------------------------")
