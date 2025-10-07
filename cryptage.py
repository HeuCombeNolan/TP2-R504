import string

caracteres = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message, pas=1):
    resultat = ""
    for c in message:
        if c in caracteres:
            index = (caracteres.index(c) + pas) % len(caracteres)
            resultat += caracteres[index]
        else:
            resultat += c
    return resultat + str(pas)

def decrypt(message):
    pas = int(message[-1])
    message = message[:-1]
    resultat = ""
    for c in message:
        if c in caracteres:
            index = (caracteres.index(c) - pas) % len(caracteres)
            resultat += caracteres[index]
        else:
            resultat += c
    return resultat
