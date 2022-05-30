print(" \n\t\t\tTP INF2044\n\n\n 1) TABLEAU DE MOYENNE, VARIANCE TE ECART TYPE\n")
from math import sqrt
# tableau de donnee statiatique
tab=[
    ['etudiant','poids','taille','age','note'],
    [1,5,1.5,13,14],
    [2,50,1.6,13,16],
    [3,50,1.65,13,15],
    [4,60,1.75,15,9],
    [5,60,1.7,14,10],
    [6,60,1.7,14,7],
    [7,70,1.6,14,8],
    [8,65,1.6,13,13],
    [9,60,1.55,15,17],
    [10,65,1.7,14,11] 
    ]

# fonction qui affiche un tableau
def afficher(tabb):
    for i in tabb:
        print(i)
# optionnel; tableau pour chaque 
Etudiant= ['etudiant','poids','taille','age','note']
Poid=[45,50,50,60,60,60,70,65,60,65]
taille=[1.5,1.6,1.65,1.75,1.7,1.7,1.6,1.6,1.55,1.7]
age=[13,13,13,15,14,14,14,13,15,14]
note=[14,16,15,9,10,7,8,13,17,11]
#fonction qui retourne le coefficient le carre d'un nbre

def exp2(a):
    return a*a
#fonction moyenne
def moyenne(tab):
    b=0
    taill=len(tab)
    Moyenne=0
    for i in range(taill):
        b=b+tab[i]
    Moyenne=b/taill
    return Moyenne
#fonction variance
def variance (tab):
    moy=moyenne(tab)
    taille=len(tab)
    som=var=float(0)
    for i in range(taille):
        som=som+exp2(tab[i]-moy)
    var=som/taille
    return var

#fonction ecart type
def ecartType(tab):
    ecart=float(0)
    ecart=sqrt(variance(tab))
    return ecart


# affichage du tableau
Poids=['1)POIDS']*4
Tailles=['2)TAILLE']*4
Age=['3)AGE']*4
Note=['4)NOTE']*4
print('\t   1)moyenne','2)variance','3)ecart_Type\n')
Poids[1]=moyenne(Poid)
Poids[2] = variance(Poid)
Poids[3] = ecartType(Poid)
print(Poids)
print("\n")
Tailles[1]=moyenne(taille)
Tailles[2] = variance(taille)
Tailles[3] = ecartType(taille)
print(Tailles)
print("\n")
Age[1]=moyenne(age)
Age[2] = variance(age)
Age[3] = ecartType(age)
print(Age)
print("\n")
Note[1]=moyenne(note)
Note[2] = variance(note)
Note[3] = ecartType(note)
print(Note)
print("\n")

print ("\n\n2) TABLEAU CENTRE REDUIT DE L'ECHANTILLON\n")
#fonction qui retourne le coefficient la norme
def norme(tab):
    tail=len(tab)
    diff=temp=float(0)
    for i in range(tail):
        temp=(tab[i]-moyenne(tab))/ecartType(tab)
        tab[i]=temp
    return tab
# affiche du tableau
P=["POIDS", norme(Poid)]
T=["TAILLE", norme(taille)]
A=["AGE", norme(age)]
N=["NOTE", norme(note)]
print(P) 
print('\n')
print(T)
print('\n')
print(A)
print('\n')
print(N)


print("\n\n3) le coefficient de correlation renseigne sur la qualite de correlation entre 2 variable etudies\n\n")

#fonction qui retourne le coefficient de correlation
def covariance(tab1, tab2):
    tail=len(tab1)
    som=x=y=cov=temp=float(0)
    for i in range(tail):
        x=tab1[i]
        y=tab2[i]
        som+=(x*y)
    temp=som/tail
    cov=temp-(moyenne(tab1)*moyenne(tab2))
    return cov
#fonction qui retourne le coefficient de correlation
def coef_corr(tab1,tab2):
    e1=ecartType(tab1)
    e2=ecartType(tab2)
    coef=covariance(tab1,tab1)/(e1*e2)
    return coef
#affichage du tableau
ca=["              1) POIDS   ", "     2)TAILLE ", "      3) AGE  ", "        4)NOTE  " ]
Po=["1)POIDS", coef_corr(Poid, Poid) ,coef_corr(Poid, taille),coef_corr(Poid, age),coef_corr(Poid, note)]
Ta=["2)TAILLE",coef_corr(taille, Poid) ,coef_corr(taille, taille),coef_corr(taille, age),coef_corr(taille, note)]
Ag=["3)AGE", coef_corr(age, Poid) ,coef_corr(age, taille),coef_corr(age, age),coef_corr(age, note)]
No=["4)NOTE", coef_corr(note, Poid) ,coef_corr(note, taille),coef_corr(note, age),coef_corr(note, note)]
print(ca) 
print('\n')
print(Po) 
print('\n')
print(Ta)
print('\n')
print(Ag)
print('\n')
print(No)

print("\n\n 4) valeur propre de la matrice de correlation\n\n")