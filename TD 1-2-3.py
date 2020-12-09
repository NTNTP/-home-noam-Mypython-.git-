#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Exo 1
x, y, z = 8, 3.6, 5 
addition = x + y + z
soustraction = x - y - z
produit = x * y * z
exp = x ** y
modulo = z % x
div = z / x
print("Exo 1 :\n", addition, soustraction, produit, exp, modulo, div,"\n\n")


# In[6]:


# Exo 2
s = "manger"
t = "regnam"
conc = s + t
rep = conc * 5
extract_l = s[1]
extract_last = s[-1]
substring = s[0:3]
longeur = len(s)


# In[7]:


# Exo 3
vrai = True
faux = False
x = 30
y = 15
egalite = vrai == faux
difference = vrai != faux
petit_ou_egale = y <= x


# In[10]:


# Exo 4
prenom, nom = "noam", "tkatch"
nom_complet = prenom + " " + nom
print((nom_complet + " * ") * 25)
initiales = "N T"
print((initiales + " * ") * 25)


# In[11]:


# Exo 5
prenom = input("Quel est votre prenom? ")
nom = input("Quel est votre nom? ")
print(prenom, nom)
print(prenom[0] + ".", nom[0] + ".")
print("Premiere lettre du nom de famille :", nom[0])


# In[ ]:


# Exo 6
temp_c = float(input("Quelle est la temperature ? "))
calcul_c = ((9/5) * temp_c) + 32
calcul_f = (temp_c - 32) * (5/9)
print(str(temp_c), "C = ", str(calcul_c), "F")
print(str(temp_c), "F = ", str(calcul_f), "C")


# In[ ]:


# Exo 7
A = bool(input("Entrer une valeur de verite pour A : "))
B = bool(input("Entrer une valeur de verite pour B : "))
C = bool(input("Entrer une valeur de verite pour C : "))
s = input('Entrer une expression Boolenne (exprimee avec des "non", "ou", "et" et des parentheses) : ')
new = s.replace("non", "not").replace("ou", "or").replace("et", "and")
print(bool(new))


# ### ################################ TD2

# In[2]:


c = "xs2536qjjp96j452jd45ssk5"
c_num = ""
c_alpha = ""
for caracters in c:
    if str.isdigit(caracters) == True:
        c_num += caracters
    else:
        c_alpha += caracters

print(c_num, c_alpha)

# Exo 1.3
str_find = "s25"
c.find(str_find)
if c.find(str_find) != -1:
    new_c = c.replace(str_find, "s26")
    print(new_c)

# Exo 1.4
list = ["p","9","6"]
for string in list:
    first = c.find(string)
    print(first)

print("\n")


# In[3]:


texte = "Je vais remonter ma note en python"
compteur = 0
for lettre in texte:
    compteur += 1
if compteur == len(texte):
    print("good")
else:
    print("not good")

# Sans les espaces
compteur_lettre = 0
for lettre in texte:
    if lettre == " ":
        pass
    else:
        compteur_lettre += 1
print(compteur_lettre)

# Compter tous les mots dans la variable txt
mots = len(texte.split())
print(mots)

# Exo 2.2


texte2 = "We introduce here the Python language. To learn more about the language, consider going through the excellent tutorial https://docs.python.org/ tutorial. Dedicated books are also available, such as http://www.diveintopython.net/."
mots2 = len(texte2.split())
print(mots2)

#Oui le script est toujours viable


# In[4]:


# Exo 3 | 1-2
n = input("Entrer des mots separes par un espace : ")
user_list = n.split()
list_triee = sorted(user_list)
print(list_triee)


# In[5]:


#Exo 4 
couleurs = ["Pique","Trefle","Carreau","Coeur"]
valeurs= ["as","2", "3", "4", "5", "6", "7", "8", "9", "10","valet","dame","roi"]
jeux=[]
for x in couleurs :
     for y in valeurs :
        card= y +" de "+ x
        jeux.append(card)
    


print(jeux)


# In[6]:


from random import shuffle;

couleurs = ["Pique","Trefle","Carreau","Coeur"]
valeurs= ["as","2", "3", "4", "5", "6", "7", "8", "9", "10","valet","dame","roi"]

shuffle (valeurs),(couleurs)
print (valeurs), (couleurs)


# In[7]:


#Exo 6
prenom = input ("Quel est votre prenom ? ")
nom = input("Quel est votre nom ? ")
numero = input ("Quel est votre numéro de matricule ? ")
print("Mon prénom est " + prenom  + " , mon nom est " + nom + " , et mon matricule est " + numero) 


# In[8]:


#Exo7

d = {"boite":"box",  "pied":"foot", "main": "hand", "ordinateur":"computer", "souris":"mouse" }
d["cerveau"] = "brain"; 
print (d) 

for i in d.items():
    print(i)
    
d["cerveau"]


a = {"box":"boite", "foot":"pied", "hand":"main", "computer":"ordinateur", "mouse":"souris", "brain":"cerveau"}

for i in a.items():
    print(i)
    
    
a["brain"]

a["chemin"] = ["path","way"];
print (a)

del a["chemin"]

print (a)


# In[9]:


#Exo8
prenom = input ("Quel est votre prenom ? ")
nom = input("Quel est votre nom ? ")
matricule = input ("Quel est votre numéro de matricule ? ")

a ={}
a["prenom"] = prenom;
a["nom"] = nom;
a["matricule"] = matricule
print (a)


# In[ ]:


############################### TD3 


# In[10]:


# Exo 1.1
personne = int(input("Entrer un nombre à multiplier : "))
for x in range(1,11):
    print(personne*x)


# In[11]:


# Exo 1.2
personne = int(input("Entrer un nombre entier à multiplier : "))
for x in range(1, 11):
    print(personne*x, end=" ")


# In[15]:


# Exo 1.3
personne = int(input("Entrer un nombre entier pour trouver sa table : "))
for x in range(personne):
    print("La Table de", int(x) + 1, " est :")
    for i in range(1, 11):
            print((x+1)*i,)


# In[16]:


# Exo 1.4
personne = int(input("Entrer un nombre pour l'afficher en asterisk : "))
for x in range(personne):
    print("*" * (x+1))


# In[18]:


# Exo 1.5
personne = int(input("Entrer un nombre pour  l'afficher en asterisk : "))
for x in range(personne):
    print(" " * ((personne-1)-x) + ("* " * (x+1)))


# In[19]:


# Exo 2.1
jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
moisjours = []
longueur = len(jours) - len(mois)
if longueur == 0:
    for x in range(len(jours)):
        moisjours.append((mois[x], jours[x]))
else:
    print("Je ne peux pas le faire")
print (moisjours)


# In[20]:


# Exo 2.2
annee = []
for month in moisjours:
     for x in range(month[1]):
        annee.append((str(x+1)) + " " + month[0])
print (annee)


# In[21]:


# Exo 2.3
annee2 = []
jours_semaine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for jour in range(365):
        annee2.append(jours_semaine[jour%len(jours_semaine)] + " " + annee[jour])
print (annee2)


# In[22]:


# Exo 2.4-5
dicionnaire = {}
jours_semaine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for jour in range(365):
        dicionnaire[annee[jour]] = jours_semaine[jour%len(jours_semaine)]
print(dicionnaire)
print(dicionnaire["28 October"])


# In[23]:


# Exo 3.1
liste_notes = []
while len(liste_notes) < 3:
    user = int(input("Entrer une note : "))
    liste_notes.append(user)

    minimum = min(liste_notes)
    maximum = max(liste_notes)
    somme = 0

    for notes in liste_notes:
        somme += int(notes)
    moyenne = float(somme)/len(liste_notes)

    print("moyenne " + str(moyenne), "minimum " + str(minimum), "maximum " + str(maximum))

#exo3_1()


# In[24]:


# Exo 3.2
user_nombres = int(input("Entrer le nombre de notes que vous voulez entrer ? "))
liste_notes = []
while len(liste_notes) < user_nombres:
        personne = int(input("Entrer une note sur 20 : "))
        liste_notes.append(personne)
mini = min(liste_notes)
maxi = max(liste_notes)
som = 0

for notes in liste_notes:
    som += int(notes)
    moy = float(som) / len(liste_notes)

    print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))


# In[26]:


# Exo 3.3
liste_notes = []
while True:
    personne = input("Entrer une note : (fin pour finir) ")
    if personne == "fin":
                break
    else:
        liste_notes.append(float(personne))
mini = min(liste_notes)
maxi = max(liste_notes)
som = 0
for notes in liste_notes:
    som += int(notes)
    moy = float(som) / len(liste_notes)


print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))


# In[28]:


#Exo 4
from random import *
nb_aleatoire1 = randint(1,100)
correct = False
while not correct:
    personne = int(input("Devine le nombre entre 1 et 100 "))
    if nb_aleatoire1 > personne:
        print("Trop petit")
    elif nb_aleatoire1 < personne:
        print("trop grand")
    elif nb_aleatoire1 == personne:
            break

    if nb_aleatoire1 == personne:
        rejoue = input ("Bravo magl, tu veux rejouer ? (y or n) ")
        if rejoue == 'y':
            
            
#print (nb_aleatoire)


# In[ ]:




