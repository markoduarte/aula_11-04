peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura**2)
imc_formatado = "{:.2f}".format(imc)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 25:
    classificacao ="Peso normal" 
elif 25 <= imc < 30:
    classificacao ="Sobrepeso" 
else:
    classificacao = "Obesidade" 

print('Seu IMC é',(imc_formatado),'e sua classificação é:', (classificacao))

 