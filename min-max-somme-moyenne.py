nb = 1
S = 0
c = 1
maax = 0
miin = 0
while c < 11  :
    print("Entrer le nombre numero ",c," :")
    nb = int(input())
    S += nb
    if  nb == 1 :
        miin = nb
        maax = nb
    else:
        if maax <= nb :
            maax = nb
    if miin > nb :
        miin = nb
    c += 1
print("le Max est : ",maax)
print("le minimum est :",miin)
print("la somme est : ",S)
print("la moyenne est : ", S / 10)
