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
    #Déroulement de la partie si l'IA ne triche pas
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
                if inf == "inférieur": #VComparaison du nombre avec la proposition du joueur
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
                else: #Géstion d'une réponse incorrecte
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
                    e = e + 1
                else:
                    print("Alice:Je ne comprends pas.")
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
                print("Bob:Est-il suppérieur à",b_temp,"?")
                r = input("Alice:")
                if r == "non":
                    b_supp = b_temp
                else:
                    b_inf = b_temp
            else:
                found = True
        print("Bob:C'est",b_inf + 1)
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
        maximum = int(input("Choisissez le maximum:"))
        ft_Bob_Mode(maximum, False)
        print("Alice:... Tsss bien joué")
    elif player == "Alice":
        ft_Alice_Mode()
        print("Bob:Je suis imbattable !")
def ft_mode_h():
    print("LUMA:Alice vous a défié !")
    print("LUMA:Survivez à 6 manches, vous êtes limité à 10 essais pour trouver le chiffre.")
    print("LUMA:Il se pourrait qu'Alice s'énerve si elle viens a perdre, soyez vigilant.")
    print("Alice:On va commencer en douceur, il ne faudrais pas brusquer ton QI d'huitre.")
    print("Alice:Je vais choisir un chiffre pour commencer.")
    ft_Bob_Mode(10, False)
    print("Alice:Tu ne serais pas une huitre, étonant.")
    print("Alice:Et si on augmentait la difficulté.")
    print("Alice:Entre 0 et 50 cette fois.")
    ft_Bob_Mode(50, False)
    print("Alice:Hmpf, ne t'emporte pas c'était encore simple.")
    print("Alice:Et si l'on passais à 150.")
    ft_Bob_Mode(150, False)
    print("Alice:Admettons que tu ne sois pas un animal, n'éspère pas gagner longtemps.")
    lvl4 = random. randint(400, 425)
    print("Alice:Passons à ",lvl4,".")
    ft_Bob_Mode(lvl4, False)
    print("LUMA:Attention! Alice s'emporte il est probable qu'elle triche.")
    print("LUMA:Si vous la suspectez de tricher dites le, elle l'admettra si c'est le cas.")
    print("Alice: Encore une fois jusqu'à",lvl4,".")
    ft_Bob_Mode(lvl4, True)
    print("Alice: OK, maintenant on passe aux choses sérieuses on va jusqu'à 999.")
    ft_Bob_Mode(999, True)
    print("Alice: C'EST IMPOSSIBLE JE SUIS IMBATTABLE MISERABLE CLOPORTE...")
    print("LUMA:Je suis terriblement désolé du comportement d'Alice, elle s'emporte quelque peu.")
    print("LUMA:Ne lui en voulez pas, elle voue une haine certaine aux humains depuis les evenements de la tour.")


mode = str(input("Voulez-vous jouer en Partie rapide ou au mode Histoire:"))
while mode != "Histoire" and mode != "Partie rapide":
    print("Je n'ai pas compris")
    mode = str(input("Voulez-vous jouer en Partie rapide ou au mode Histoire:"))

if mode == "Histoire":
    ft_mode_h()

else :
    ft_mode_Pr()
