from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
def signe(w,Xi):                                   # Fonction signe pour calculer le produit scalaire et retourner le signe
    scalar = np.dot(w,Xi) 
    print("SCALAR IS SCALAR",scalar)  
    if scalar >0:
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
    donnees = []                                      # Donnees est une liste
    for i in range(len(x1b)):
        donnees.append(((x1b[i],x2b[i]),-1))          # J'ai changer true et false par 1 et -1 pour presenter les 2 classes
        donnees.append(((x1r[i],x2r[i]),1))
    return donnees  

############# Perceptron Binaire 

def perceptron(weight, Data, N):                        # La fonction de pereceptron avec les parametres a la liste des donnees et w le vecteur de penderation
    erreur = 0
    print("the data is " ,Data)
    print("*" *60) 
    for j in range(N) :                                          
        for i in range(len(Data)) :                      # Pour chaque xi yi de l'ensemble S 
            print("the weight is ",weight)
            data = np.array(Data[i][0])                  # Recuperer les xi 
            print("the tuple to test is ",Data[i][0])                                                                                         
            ŷ = signe(weight,data)
            print("le y chapeaua ",ŷ)
            print("le Y ", Data[i][1])      
            if ŷ != Data[i][1] :                         # Si ŷ != de yi 
                erreur = erreur + 1
            print("L'erreur : " ,erreur)
            if (ŷ != Data[i][1] and Data[i][1] == 1):    # Data[i][1] = yi 
                weight = weight + data                   # Ajuster le vecteur W 
                print("the new Value of weight is :" ,weight)
                print("*" *60)
            elif (ŷ != Data[i][1] and Data[i][1] == -1):
                weight = weight - data                   # Ajuster le vecteur W     
                print("the new Value of weight is :" ,weight)
                print("*" *60)
    return weight                                                          

def draw_point(Data):
    Tabx1 = []
    Tabx2 = []
    Tabx3 = []
    Tabx4 = []
    print(Data)
    for i in range(len(Data)) :
        
        if Data[i][1] == 1 :
            Tabx1.append(Data[i][0][0])             # Recuperer les abscisses des xi de la classe 1 
            Tabx2.append(Data[i][0][1])             # Recuperer les ordonnees des xi de la classe 1 
        else :
            Tabx3.append(Data[i][0][0])             # Recuperer les abscisses des xi de la classe -1 
            Tabx4.append(Data[i][0][1])             # Recuperer les ordonnees des xi de la classe -1 

    print("*" *60)
    print("tab1",Tabx1,  "ET" ,Tabx2)
    print("tab1",Tabx3,  "ET" ,Tabx4)
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
Data = genererDonnees(50)
weight = perceptron(w_init,Data,1)
Data_tst = genererDonnees(10)
w_tst = perceptron(weight,Data_tst,1)

print("-" *60)
print(w_tst)
draw_point(Data_tst)


#if __name__ == '__main__':
#    main()

