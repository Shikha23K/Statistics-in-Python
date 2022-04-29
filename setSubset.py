import numpy as np
A={1,2,3,8}
B={3,4}
print(1 in A) #checking whether 1 in A or not
print(B.issubset(A)) #B is subset of A or not
def F_subset(A,B):
    for e in A:
        if e in B:
            pass
        else:
            return False
    return True

print(F_subset(B,A))    
#Universal set Omg
omg=set(np.arange(10))
print("Type of Omg :",type(omg))
P=set(np.arange(0,9,2))
Q=set(np.arange(1,9,3))
# PUQ
print("P U Q: ",P.union(Q))
# P intersection Q
print("P intersection Q: ",P.intersection(Q))
Q.add(6)
# P-Q
print("P-Q: ",P.difference(Q))
# P complement
p_comp=omg.difference(P)
print("P complement :",p_comp)
# Q complement
q_comp=omg.difference(Q)
print("Q complement :",q_comp)
# Omg-(PUQ)
print("Omg-(PUQ) :",omg.difference(P.union(Q)))
# P complement intersection Q complement
print(p_comp.intersection(q_comp))
# D' Morgen's :- Omg - (P intersection Q) = P complement union Q complement 
print(omg.difference(P.intersection(Q)))
print(p_comp.union(q_comp))
