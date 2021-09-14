def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat

    chaine=""
    if(n%3==0):
        chaine += "fizz"
    if(n%5==0):
        chaine+= "Buzz"
    if(chaine == ""):
        chaine =str(n)
    #print(chaine)

    resultat = chaine
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
