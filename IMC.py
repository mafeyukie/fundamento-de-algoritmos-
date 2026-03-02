peso = float (input("Digite seu peso"))
altura = float (input("Digite sua altura "))

imc = peso/ (altura **2)

imc+ round(imc,1)
print/(imc)

if imc < 18.5:
    classificaçao = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificaçao = "Peso ideal"
elif 25.0 <= imc <= 29.9:
    classificaçao = "Levemente acima do peso"
elif 30.0 <= imc <= 34.9:
    classificao = "Obesidade gra I"
elif 35.0 <= imc <= 39.9:
    classificaçao = "Obesidade grau II"
else:
    classificaçao = "Obesidade grau III"

 