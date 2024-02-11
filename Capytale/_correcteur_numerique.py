import matplotlib.pyplot as plt
import random as rd
import numpy as np
import math as m



def cor_creer_les_t(tf : float, h : float) -> np.array:
    return np.arange(0,tf,h)


def cor_creer_echelon(tf : float, h:float, E0: float) -> np.array :
    les_t = cor_creer_les_t(tf,h)
    nb = len(les_t)
    les_e = np.ones(nb)*E0
    return les_e

def cor_calculer_epsilon_s(tf : float, h : float, les_ek : np.array) -> (np.array,np.array,np.array) :
    n = len(les_ek)
    les_sk = np.zeros(n)
    les_eps = np.zeros(n)
    les_eps[0] = les_ek[0] - les_sk[0]
    Tv = 1
    Kv = 5
    for i in range (1,n) :
        les_eps[i] = les_ek[i]-les_sk[i-1]
        les_sk[i] = (1/(h+Tv))*(Tv*les_sk[i-1]+Kv*h*les_eps[i])
    return cor_creer_les_t(tf,h),les_eps,les_sk
    
    
    
def test_q01(foo):
    pts = 0
    total = 0
    
    les_tf = [1,3,5]
    les_h = [0.1, 0.01, 0.001]

    for tf in les_tf :
        for h in les_h :
            total +=1

            try :
                L_cor = cor_creer_les_t(tf,h)
                L_eleve = foo(tf,h)
                if (np.allclose(L_cor,L_eleve)):
                    pts +=1 
            except : 
                pass
    
    return pts,total


def test_q02(foo):
    pts = 0
    total = 0
    
    les_tf = [1, 3  ,5]
    les_h =  [0.1, 0.01, 0.001]
    les_e =  [1, 5,  10]
    for tf in les_tf :
        for h in les_h :
            for e0 in les_e :
                total +=1
    
                try :
                    L_cor = cor_creer_echelon(tf,h,e0)
                    L_eleve = foo(tf,h,e0)
                    if (np.allclose(L_cor,L_eleve)):
                        pts +=1 
                except : 
                    pass
    
    return pts,total

def test_q03(foo):
    pts = 0
    total = 0
    
    les_tf = [1, 3  ,5]
    les_h =  [0.1, 0.01, 0.001]
    les_e =  [1, 5,  10]
    
    for tf in les_tf :
        for h in les_h :
            for e in les_e :
                les_ek =  cor_creer_echelon(tf,h,e)
                
                total +=1
                try :
                    
                    L_cor = cor_calculer_epsilon_s(tf,h, les_ek)
                    L_eleve = foo(tf,h,les_ek)
                    if (np.allclose(L_cor,L_eleve)):
                        pts +=1 
                except : 
                    pass
        
    return pts,total


def go_p1(foo1,foo2,foo3):
    i = 0
    notes = {}
    tot = 0
    
    tests = [[test_q01,foo1],[test_q02,foo2],[test_q03,foo3]]
    
    for t in tests : 
        tq,f = t
        pts = 0
        i +=1
        try :
            pts,tot = tq(f)
        except : 
            pass
        print("Question "+str(i)+" : ",str(pts),"/",str(tot))
        notes[i] = (pts,tot)
       
    #bilan : 
    points,total = 0,0
    for n in notes.values() :
        points = points + n[0]
        total = total + n[1]
    print(points,total)
    print(points*20/total,20)
    