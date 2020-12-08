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

