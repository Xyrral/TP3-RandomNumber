#L1 Math-Info TD-C Khedr Nader#
import random
import sys
import os

def ft_Bob_Mode(): #L'ia joue Bob et fais deviner un nmobre#
    nb = 1000
    nb_ia = random. randint(0, 999)
    print("Bien, commençons.")

    while nb != nb_ia:
        print("Alice:Avez-vous une question ?")
        q = input("Bob:")
        if q == "Oui":
            nb = int(input("Entrez un chiffre :"))
            print("Alice:Cherchez-vous à savoir si",nb,"est inférieur ou suppérieur à mon nombre ?")
            inf = input("Bob:")
            if inf == "Inférieur":
                if nb < nb_ia:
                    print("Alice:Il l'est.")
                else:
                    print("Alice:Il ne l'est pas.")
            elif inf == "Suppérieur":
                if nb > nb_ia:
                    print("Alice:Il l'est.")
                else:
                    print("Alice:Il ne l'est pas.")
            else:
                print("Alice:Je ne comprends pas.")
        elif q == "Non":
            nb = int(input("Alice:Oh une supposition, allez-y :"))
            if nb != nb_ia:
                print("Alice:Ce n'est pas",nb,"je suis déçue...")
        else :
            print("Alice:Je ne comprends pas.")

def ft_Alice_Mode(): #L'ia joue Alice et devine le nombre#
    print("Choisissez un nombre compris entre 0 et 999")

mode = str(input("Etes vous Bob ou Alice ?"))
while mode != "Bob" and mode != "Alice":
    print("Je n'ai pas compris")
    mode = str(input("Etes vous Bob ou Alice ?"))
    sys.clear()
if mode == "Bob":
    ft_Bob_Mode()
    print("Je veux ma revanche")
elif mode == "Alice":
    ft_Alice_Mode()
    print("Je suis imbattable")
