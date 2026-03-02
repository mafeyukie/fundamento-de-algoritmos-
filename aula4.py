A = float (input("Digite o lado A"))
B = float (input("Digite o lado B"))
C = float (input("Digite o lado C"))

# se é triângulo 
if A + B > C and B + C > A and A + C > B:
    print ("É um triangulo", end=" ")

    # se é retângulo
    if ( A ** 2 == B ** 2 + C ** 2) or (B**2 == C **2 + A **2) or ( C**2 == B**2 + A**2):
        print ("retângulo", end=" ")
    # se é equilatero 
    if A == B and A == C and B == C:
       print ("Triangulo equilátero")
    # se é isoceles 
    elif (A == B and A != C and B != C) or (A == C and A != B and C != B) or (B == C and B!=A and C!=A):
        print ("Triângulo Isóceles")
    # senão se é escaleno
    else:
       print("isoceles")
else:
     print ("Não contem um triâgulo")