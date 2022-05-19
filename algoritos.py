num=int(input("numero: "))
pot=int(input("potencia: "))
mo=int(input("mod: "))


def alg1(n,p,m):
    binar=bin(p)
    binario=(binar[2:])[::-1]
    res=1
    for i in range(len(binario)):
        if i==0:
            g=n
            if binario[i]=="1":
                res=res*g
        else:
            g=(g**2)%m
            if binario[i]=="1":
                res=res*g
    return res%m

def alg2(n,p,m):
    if p==0:
        return 1
    else:
        return ((n%m)*alg2(n,p-1,m))%m
    
def alg3(n,p,m):
    if p==0:
        return 1
    if p%2==0:
        return (alg3(n,p/2,m)**2)%m
    else:
        return (n*alg3(n,(p-1)/2,m)**2)%m
    
print(alg1(num,pot,mo))
try:
    print(alg2(num,pot,mo))
except:
    print("algoritmo 2 no ejecutado -- maxima recursion alcanzada")

print(alg3(num,pot,mo))
##print((num**pot)%mo)