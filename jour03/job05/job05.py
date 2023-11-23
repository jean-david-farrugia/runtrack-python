def calcule(num1,operator,num2):
    if operator == "+":
        resultat = num1 + num2
    elif operator == "-":
        resultat = num1 - num2
    elif  operator == "*":
        resultat = num1 * num2
    elif  operator == "/":
        resultat = num1 / num2
    else :
        resultat = num1 % num2 
    print (resultat)

calcule(18,"%",15)
      