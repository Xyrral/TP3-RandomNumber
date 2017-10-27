#L1 Math-Info TD-C Khedr Nader#
import random
import sys
#L'ia joue Alice et doit faire deviner un nombre#
def ft_Bob_Mode(nb_max,triche):
    nb = 1000
    nb_q = 1000
#Nb = nombre pour la réponse, nb_q = nombre pour les questions#
    nb_ia = random. randint(0, nb_max)
    t = 0
    print("Alice:Bien, commençons.")
    if triche == False:
         while nb != nb_ia:
            if t == 11:
                print("Alice:Vous avez perdu on dirait, pas étonant")
            print("Alice:Avez-vous une question ?")
            q = input("Bob:")
            if q == "oui":
                print("Alice:Entrez un nombre.")
                nb_q = int(input("Bob:"))
                print("Alice:Cherchez-vous à savoir si",nb_q,"est inférieur ou suppérieur à mon nombre ?")
                inf = input("Bob:")
                if inf == "inférieur":
                    if nb_q < nb_ia:
                        print("Alice:Il l'est.")
                        t = t + 1
                    elif nb_q == nb_ia:
                        print("Alice:...")
                        t = t + 1
                    else:
                        print("Alice:Il ne l'est pas.")
                        t = t + 1
                elif inf == "suppérieur":
                    if nb_q > nb_ia:
                        print("Alice:Il l'est.")
                        t = t + 1
                    elif nb_q == nb_ia:
                        print("Alice:...")
                        t = t + 1
                    else:
                        print("Alice:Il ne l'est pas.")
                        t = t + 1
                else:
                    print("Alice:Je ne comprends pas.")
            elif q == "réponse":
                print("Alice:Oh une supposition, allez-y :")
                nb = int(input("Bob:"))
                if nb != nb_ia:
                    print("Alice:Ce n'est pas",nb,"je suis déçue...")
                    t = t + 1
            else :
                print("Alice:Je ne comprends pas.")
    else :
        e = 0
        cheat = False
        while nb != nb_ia:
            if e == 5:
                e = 0
                cheat = random. randint(0, 4)
                if cheat == 1:
                    nb_ia = random. randint(0, nb_max)
                    cheat = True
            print("Alice:Avez-vous une question ?",nb_ia)
            q = input("Bob:")
            if q == "oui":
                print("Alice:Entrez un nombre.")
                nb_q = int(input("Bob:"))
                print("Alice:Cherchez-vous à savoir si",nb_q,"est inférieur ou suppérieur à mon nombre ?")
                inf = input("Bob:")
                if inf == "inférieur":
                    if nb_q < nb_ia:
                        print("Alice:Il l'est.")
                        t = t + 1
                    elif nb_q > nb_ia:
                        print("Alice:Il ne l'est pas.")
                        t = t + 1
                    else:
                        print("Alice:...")
                        t = t + 1
                elif inf == "suppérieur":
                    if nb_q > nb_ia:
                        print("Alice:Il l'est.")
                        t = t + 1
                    elif nb_q < nb_ia:
                        print("Alice:Il ne l'est pas.")
                        t = t + 1
                    else:
                        print("Alice:...")
                        t = t + 1
                else:
                    print("Alice:Je ne comprends pas.")
                e = e + 1
            elif q == "réponse":
                print("Alice:Oh une supposition, allez-y :")
                nb = int(input("Bob:"))
                if nb != nb_ia:
                    print("Alice:Ce n'est pas",nb,"je suis déçue...")
            elif q == "triche":
                if cheat == True:
                    print("Alice:Vous m'insuportez")
                    nb = nb_ia
                else:
                    print("ALice:Comment osez-vous, je suis vexée, je ne veux plus jouer avec vous")
                    sys.exit(0)
            else :
                print("Alice:Je ne comprends pas.")

def ft_Alice_Mode(): #L'ia joue Alice et devine le nombre#
    b_inf = 0
    b_supp = 999
    b_temp = 500
    temp = 500
    found = False
    print("Bob:Choisissez un nombre compris entre 0 et 999")
    print("Bob:Est-il inférieur à 500?")
    inf500 = input("Alice:")
    if inf500 == "oui":
        b_supp = 500
        while found != True:
            if (b_supp - b_inf) > 2:
                if temp != 1:
                    temp = temp // 2
                else:
                    found = True
                    b_supp = b_inf + 2
                b_temp = b_inf + temp
                print(b_temp,b_supp,b_inf,temp)
                print("Bob:Est-il inférieur à",b_temp,"?")
                r = input("Alice:")
                if r == "oui":
                    b_supp = b_temp
                else:
                    b_inf = b_temp
            else:
                found = True
        print("Bob:C'est",b_supp - 1)
    else: 
        b_inf = 500
        while found != True:
            if (b_supp - b_inf) > 2:
                if temp != 1:
                    temp = temp // 2
                else:
                    found = True
                    b_supp = b_inf + 2
                b_temp = b_inf + temp
                print(b_temp,b_supp,b_inf,temp)
                print("Bob:Est-il inférieur à",b_temp,"?")
                r = input("Alice:")
                if r == "oui":
                    b_supp = b_temp
                else:
                    b_inf = b_temp
            else:
                found = True
        print("Bob:C'est",b_supp - 1)
def ft_mode_Pr():
    player = str(input("Etes vous Bob ou Alice ?"))
    while player != "Bob" and player != "Alice":
        print("Je n'ai pas compris")
        player = input("Etes vous Bob ou Alice ?")
    if player == "Bob":
        ft_Bob_Mode(999, True)
        print("Alice:... Tsss bien joué")
    elif player == "Alice":
        ft_Alice_Mode()
        print("Bob:Je suis imbattable !")
def ft_mode_h():
    print("JARVIS:Alice vous a défié !")
    print("JARVIS:Survivez à 6 manches, vous êtes limité à 10 essais pour trouver le chiffre.")
    print("JARVIS:Il se pourrait qu'Alice s'énerve si elle viens a perdre, soyez vigilant.")
    print("Alice:On va commencer en douceur, il ne faudrais pas brusquer ton QI d'huitre.")
    print("Alice:Je vais choisir un chiffre pour commencer")
    ft_Bob_Mode(10, False)


mode = str(input("Voulez-vous jouer en Partie rapide ou au mode Histoire:"))
while mode != "Histoire" and mode != "Partie rapide":
    print("Je n'ai pas compris")
    mode = str(input("Voulez-vous jouer en Partie rapide ou au mode Histoire:"))

if mode == "Histoire":
    ft_mode_h()

else :
    ft_mode_Pr()
