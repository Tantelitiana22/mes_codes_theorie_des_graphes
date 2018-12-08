####################################
# Andrianarivo RAKOTAORIJAONA
###################################

import numpy as np

## Algo de Ford
def ford(init,arcs,sommet,poid,N=10000):
    # initialiser pred avec a ou le vide
    pred=[init if arcs[i][0]==init else "" for i in range(len(sommet))]
    # Initialisation de k et de n:nombre de sommet-1
    k=0
    n=len(sommet)-1
    # initialisation du potentiel d avec 0 et 10000
    d=np.repeat(N,n+1).tolist()
    d[sommet.index(init)]=0
    d=np.array(d)
    # condition bol pour s'arreter lorsque l'on obtient la même d sur 2 itération.
    bol=True
    # corps de l'algo
    while(k<=n and bol):
        k=k+1
        d_pred=d.copy()
        for i in range(len(arcs)):
            ind1=int(list(np.where([ sommet[k]==arcs[i][0] for k in range(len(sommet))]))[0])
            ind2=int(list(np.where([ sommet[k]==arcs[i][1] for k in range(len(sommet))]))[0])
            if d[ind2]-d[ind1]>poid[i]:
                d[ind2]=d[ind1]+poid[i]
                pred[ind2]=sommet[ind1]

        bol=(sum(d_pred==d)!=len(d))
    
    return({"potentiel":d.tolist(),"predecesseur":pred})


## Algo de Dijkstra version ma méthode
def dijkstra_v1(init,arcs,sommet,poid,N=10000):
    n=len(sommet)
    ## Potentiel
    V=np.repeat(N,n)
    V={sommet[k]:V[k] for k in range(len(V))}
    V[init]=0
    # marqueur qui vaut 0 ou #0 si k est maquer pour k dans sommet.
    marque={sommet[k]:0 for k in range(len(sommet))}
    # Dictionnaire
    poid={arcs[k]:poid[k] for k in range(len(arcs))}
    # Predecesseur
    P=np.repeat(init,n)
    P={sommet[i]:P[i] for i in range(len(P))}

    Vmin=0
    x=""
    while Vmin<10000:
        Vmin=10000
        for y in sommet:
            if marque[y]==0 and V[y]<Vmin:
                x=y
                Vmin=V[y]
        if Vmin<10000:
            marque[x]=1
            x_succ=[arcs[k][1] for k in range(len(arcs)) if arcs[k][0]==x]
            for y in x_succ:
                if marque[y]==0 and V[x]+poid[x+y]<V[y]:
                    V[y]=V[x]+poid[x+y]
                    P[y]=x
    V_res=[V[k] for k in sommet]
    P_res=[P[k] for k in sommet]
    return({"potentiel":V_res,"predecesseur":P_res})

## Algo Dijkstra methode du cours
def dijkstra_v2(init,arcs,sommet,poid,N=10000):
    
    S=[init]
    S_bar=[sommet[i] for i in range(len(sommet)) if sommet[i]!=init]
    omega={arcs[t][0]:[arcs[k][1] for k in range(len(arcs)) if arcs[k][0]==arcs[t][0]] for t in range(len(arcs))}
    pred=[init if arcs[i][0]==init else "" for i in range(len(sommet))]
    poids={arcs[u]:poid[u] for u in range(len(poid))}
    sommet=np.array(sommet)
    P=[]
    for k in range(len(sommet)):
        if sommet[k]==init:
            P.append(0)
        elif sommet[k] in omega[init]:
            P.append(poids[init+sommet[k]])
        else:
            P.append(N)
    P=np.array(P)
    while len(S_bar)!=0:
        P_bar=[P[int(np.where(sommet==t)[0])] for t in S_bar ]
        j=np.argmin(P_bar)
        sj=S_bar[j]
        S.append(sj)
        del S_bar[j]
    
        if len(S_bar)!=0:
            if sj in omega.keys():
                inter=[i for i in omega[sj] if i in S_bar ]
            else:
                inter=[]
            for i in range(len(inter)):
                si=inter[i]
                i_new=int(np.where(sommet==si)[0])
                j_new=int(np.where(sommet==sj)[0])
                if P[i_new]-P[j_new]>poids[sj+si]:
                    P[i_new]=P[j_new]+poids[sj+si]
                    pred[i_new]=sj    
    return({"potentiel":P.tolist(),"predeceseur":pred})

if __name__=="__main__":

    ## Définition du graphe
    ### Arcs
    arcs=["ac","ab","cb","ce","bd","be","ef","fb","fd","cf"]
    ### Les poids des arcs
    poid=[1,7,5,7,4,2,3,2,5,2]
    ### Les sommets
    sommet=["a","b","c","d","e","f"]
    ### Initiateur
    init="a"
    print("Résultat de Ford:{}".format(ford(init,arcs,sommet,poid)))
    print("Résultat deDejkstra version 1:{}".format(dijkstra_v1(init,arcs,sommet,poid)))
    print("Résultat deDejkstra version 2:{}".format(dijkstra_v2(init,arcs,sommet,poid)))
    
