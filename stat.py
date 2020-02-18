# -*- coding: utf-8 -#-
#-------------------------------------------------------------------------------
#
# Auteur        : Cédric Kreis
# Programme     : Parser for html page : <li></li>
# Fonctions     : Récupération des balises <li> et les met dans un tableau,
#                 ensuite un traitment mathématique est effectué.
# Création      : 14.01.2020
# Modifié le    : 18.02.2020
# Version       : 1.6
#
#               : sudo pip install lxml
#               : sudo pip install bs4
#
# OS            : MacOSX
# Python        : 2.7.10
#
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
from decimal import *



def etendue() :

    #global permet de récupérer la valeur de la variable hors de cete fonction
    global etendue

    var1 = chiffres[0]
    var2 = chiffres[lastnumber]
    etendue = var2 - var1

    return etendue



def mediane() :

        #Contrôle si le nombre d'éléments du tableau est pair
        tableau = x % 2

        if(tableau  == 0) : # Si le tableau est égale à 0 il est pair
            #Formule mathématique pour le traitement des tableaux pairs
            etape1 = (x + 1) / 2
            etape2 = etape1 + 1

            moyennedeuxvaleurs = float(( chiffres[etape2] - chiffres[etape1] ))

            division = moyennedeuxvaleurs / 2
            medianepair = chiffres[etape1] + division


            print "Médiane    :",medianepair



            if (medianepair > etendue) :
                print "Dispersion : Forte"
            else :
                print "Dispersion : Faible"

        # Calcule de la médiane pour un tableau impaire
        else :

            medianetableauimpaire = x / 2

            print "Médiane    :",chiffres[medianetableauimpaire]

            if (medianetableauimpaire > etendue) :
                print "Dispersion : Forte"
            else :
                print "Dispersion : Faible"




def moyenne() :

    resultatmoyenne = float(somme / x)
    return resultatmoyenne




#Initialisation des variables
chiffres    = []
somme       = Decimal(0)
division    = Decimal(0)


#Demande à l'utilisateur du fichier à traiter
file = raw_input("Enter a file name : ")

#Test si un nom de fichier a été indiqué
if (file == ''):
    print ('Miss a filnename')
#Le programme se lance correctement
else :
    with open(file, 'r') as f :
        contents = f.read()
    #Code permettant l'utilisation de BeautifulSoup
    soup = BeautifulSoup(contents, 'lxml')

    #Lecture d'un fichier HTML avec BeautifulSoup
    for tag in soup.find_all("li") :
        h = str(tag)

        format = h.lstrip('<li>').rstrip('</li>')
        numbers = int(format)

        somme += numbers

        chiffres.append(numbers)
        chiffres.sort()
        x = len(chiffres)
        lastnumber = x - 1


    moyennefinale  = moyenne()
    etendue        = etendue()



    #Affichage des résultats à l'écran
    print ""

    print "Tableau    :",chiffres

    print"élément    :",x

    print "Somme      :",somme

    print "étendue    :",etendue

    print ""

    print "--- Tendance Centrale ---"

    print ""

    print "Moyenne    :",moyennefinale

    mediane = mediane()

    print ""
