#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exercice 1

#1 et 2
from math import pi

def surf_cercle(r = 1):
	return pi*r**2

print(surf_cercle(3))
print(surf_cercle())


#3 et 4
def vol_boite(x1 = -1, x2 = -1, x3 = -1):
	if x1 != -1 and x2 == -1 and x3 == -1: # un argument fourni
		return x1**3
	elif x1 != -1 and x2 != -1 and x3 == -1: # deux arguments fournis
		return x1*x1*x2
	elif x1 != -1 and x2 != -1 and x3 != -1: # trois arguments fournis
		return 

print(vol_boite(1.7, 8.42, 5.48))
print(vol_boite(x1 = 2.0))
print(vol_boite(x1 = 2.0, x2 = 3))
print(vol_boite(x1 = 1.7, x2 = 8.42, x3 = 5.48))



#5 et 6
def remplacement(c1 = " ", c2 = "*", ch = ""):
	ch2 = ""
	for i in range(len(ch)):
		if ch[i] == c1:
			ch2 = ch2 + c2
		else:
			ch2 = ch2 + ch[i]
	return ch2
		

print(remplacement("C'est Beau", "Joyeux Noel", "Bonne année"))


# In[3]:



le_texte = "Un jour je serai le meilleur dresseur ,Je me battrai sans répit, Je ferai tout pour être vainqueur, Et gagner les défis, Je parcourrai la terre entière , Traquant avec espoir , Les Pokémon et leurs mystères ,Le secret de leurs pouvoirs "


def nb_car(texte):
	return len(texte)

print(nb_car(le_texte))


def nb_mots(texte):
	counter = 0
	for c in texte:
		# for every symbol found, we increment the number of words
		if  (c == " "):
			counter += 1
	# we add 1 to count the last word (note counted, since not followed by a ". " but only by a ".")
	counter += 1
	return counter

print(nb_mots(le_texte))


# In[5]:


# Exercice 3

#print("# *** 1 et 2 *** #")

def TableMult(n, debut = 1, fin = 10):
	print("Le Fragment de la table de multiplication de", n, ":")
	if debut <= fin:
		for i in range(debut, fin+1):
			print(i, 'x', n, '=', i * n)
			i = i + 1
	else:
		for i in range(debut, fin-1, -1):
			print(i, 'x', n, '=', i * n)
			i = i + 1


#print("# *** 3 *** #")

def TableMult2():
	n = input("Quelle est la base? ")
	debut = input("Le Debut: ")
	fin = input("La Fin: ")
	print("Le Fragment de la table de multiplication de", n, ":")
	if debut <= fin:
		for i in range(debut, fin+1):
			print(i, 'x', n, '=', i * n)
			i = i + 1
	else:
		for i in range(debut, fin-1, -1):
			print(i, 'x', n, '=', i * n)
			i = i + 1


# In[6]:


# Exercice 4 

from random import randint


mots = ["arbre", "grave", "piece", "nuage", "crane", "sonne", "table", "herbe", "ecrou", "mulet"]


def remplace(i, c, ch):
	ch2 = ""
	for j in range(len(ch)):
		if j == i:
			ch2 += c
		else:
			ch2 += ch[j]
	return ch2



def motus(n = 10):
	"""Le Jeu Motus"""
	mot_cache = mots[randint(0,len(mots)-1)]
	mot_devine = "....."
	essai = 0
	while essai < n:
		print("Essai N° ", essai+1)
		lettre = input("Entrer une lettre: ")
		for j in range(len(mot_cache)):
			if mot_cache[j] == lettre:
				mot_devine = remplace(j, lettre, mot_devine)
			else: 		# useless instructions
				pass	# ...
		print("\n" + mot_devine + "\n")
		if not("." in mot_devine):
			print("Bravo C'est gagné !")
			break
		else:
			essai += 1
			if essai == n:
				print("Dommage C'est Perdu!")


# In[ ]:




