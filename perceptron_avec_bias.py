from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from random import *

bias = [                                                # J'ai pris que les 10 premiers au lieux 1000
    (0.969158, False),
    (0.825657, False),
    (1.002526, True ),
    (1.603653, True ),
    (0.024345, False),
    (1.565128, True ),
    (1.888451, True ),
    (1.326667, True ),
    (1.795088, True ),
    (0.477552, False),
    ]

m = randint(0,10)                                         # Generer un entier entre 1 et 10 aleatoirement
b = bias[m][0]                                            # J'ai recupere la 1 ere partie du bias  l'entier possitif 
print(b)
def signe(w,Xi,b):
                                                       
    scalar = np.dot(w,Xi)
    scalar = scalar + b 
    print("SCALAR IS SCALAR",scalar)  
    if scalar > 0:
        return 1
    else:
        return -1

def genererDonnees(n):
    #modification de cette partie de code car il y'a un conflie entre l allias ou le pseudo dans (from pylab import rand) rand et la fonction rand de numpy 
    #générer un jeu de données 2D linéairement séparable de taille n.
    x1b = (np.random.rand(n)*2-1)/2-0.5
    x2b = (np.random.rand(n)*2-1)/2+0.5
    x1r = (np.random.rand(n)*2-1)/2+0.5
    x2r = (np.random.rand(n)*2-1)/2-0.5
    donnees = []                                                    
    for i in range(len(x1b)):
        donnees.append(((x1b[i],x2b[i]),-1))                       
        donnees.append(((x1r[i],x2r[i]),1))
    return donnees  
                                                    
######## AVEC BIAS ######

def perceptronbias(weight, Data):
                                   
   for i in range(len(Data)) : 
        data = np.array(Data[i][0])                                                                                          
        ŷ = signe(weight,data,b)
        if (ŷ != Data[i][1] and Data[i][1] == 1):
            weight = weight + data
            print("the new Value of weight is :" ,weight)
            print("*" *60)
        elif (ŷ != Data[i][1] and Data[i][1] == -1):
            weight = weight - data
            print("the new Value of weight is :" ,weight)
            print("*" *60)
        #draw_point([Data[0][0]],[Data[0][1]],ŷ)        
   return weight

def draw_point(Data):
    Tabx1 = []
    Tabx2 = []
    Tabx3 = []
    Tabx4 = []
    print(Data)
    for i in range(len(Data)) :
        
        if Data[i][1] == 1 :
            Tabx1.append(Data[i][0][0])
            Tabx2.append(Data[i][0][1])
        else :
            Tabx3.append(Data[i][0][0])
            Tabx4.append(Data[i][0][1])

    print("*" *60)
    print("tab1",Tabx1,  "ETTTTT" ,Tabx2)
    print("tab1",Tabx3,  "ETTTTT" ,Tabx4)
    fig = plt.figure(figsize= (100,100))
    ax = plt.axes()
  
    ax.scatter(Tabx1, Tabx2, c= "red")                           
    ax.scatter(Tabx3, Tabx4, c= "blue")  
    plt.xlabel("abscisses")
    plt.ylabel("ordonnees")
    plt.title("Representation des classes", fontsize=20)

    plt.show()

#def main():
w_init = np.zeros(2)
Data = genererDonnees(20)
weight = perceptronbias(w_init,Data)
Data_tst = genererDonnees(10)
w_tst = perceptronbias(weight,Data_tst)

print(w_tst)
draw_point(Data_tst)


#if __name__ == '__main__':
#    main()

