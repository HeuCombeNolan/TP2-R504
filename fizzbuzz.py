def affiche(*args):
    if len(args) == 0:
        n1, n2 = 1, 100
    elif len(args) == 1:
        n1, n2 = 1, args[0]
    elif len(args) == 2:
        n1, n2 = args
    else:
        raise ValueError("Trop d'arguments")

    resultat = ""
    for i in range(n1, n2 + 1):
        if i % 15 == 0:
            resultat += "FrisBee"
        elif i % 3 == 0:
            resultat += "Fizz"
        elif i % 5 == 0:
            resultat += "Buzz"
        else:
            resultat += str(i)
    return resultat
