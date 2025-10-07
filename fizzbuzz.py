def affiche(*args):
    if len(args) == 0:
        n1, n2 = 1, 100
    elif len(args) == 1:
        n1, n2 = 1, args[0]
    elif len(args) == 2:
        n1, n2 = args
    else:
        raise ValueError("Trop d'arguments")
