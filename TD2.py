#!/usr/bin/env python
# coding: utf-8

# In[7]:


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


# In[10]:


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


# In[11]:


# Exo 3 | 1-2
n = input("Entrer des mots separes par un espace : ")
user_list = n.split()
list_triee = sorted(user_list)
print(list_triee)


# In[ ]:


#Exo 4 
couleurs = ["Pique","Trefle","Carreau","Coeur"]
valeurs= ["as","2", "3", "4", "5", "6", "7", "8", "9", "10","valet","dame","roi"]
for x in couleurs :
     for y in valeurs :
        print( y +" de "+ x )


# In[ ]:


from random import shuffle;

couleurs = ["Pique","Trefle","Carreau","Coeur"]
valeurs= ["as","2", "3", "4", "5", "6", "7", "8", "9", "10","valet","dame","roi"]

shuffle (valeurs),(couleurs)
print (valeurs), (couleurs)


# In[3]:


#Exo 6
prenom = input ("Quel est votre prenom ? ")
nom = input("Quel est votre nom ? ")
numero = input ("Quel est votre numéro de matricule ? ")
print("Mon prénom est " + prenom  + " , mon nom est " + nom + " , et mon matricule est " + numero) 


# In[ ]:




