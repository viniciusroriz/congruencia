# Vinícius Roriz - 190020814

from math import gcd, prod

def main():
    x = 0                   # solução do sistema
    C = []                  # soluções de cada equação tal que aC = b(mod n)
    M = []                  # Mi = N/ni
    W = []                  # inverso de M
    a = []                  
    b = []
    n = []

    # ----------------------- lê as entradas
    k = int(input('informe a quantidade de equações: '))
    leEntradas(k,a,b,n)

    # ----------------------- Checa se o teorema é aplicável
    for i in range(k):
        for j in range(1+i,k):
            if gcd(n[i],n[j]) != 1:
                print('O teorema chinês dos restos não é aplicável')
                exit()  

    # ----------------------- Resolve cada equação e encontra Ci
    for i in range(k):
        C.append(resolveEq(a[i], b[i], n[i]))
    
    # ----------------------- Encontra Mi e Wi
    N = prod(n)           
    for i in range(k):
        M.append(int(N/n[i]))
    
    for i in range(k):
        W.append(achaInverso(M[i], n[i]))
    
    # ----------------------- Solução = C0*M0*W0 + ... + Ck*Mk*Wk
    for i in range(k):
        x += C[i]*M[i]*W[i]

    print('A solução do sistema é:', x%N)


def leEntradas(k,a,b,n):
    for i in range(k):
        a.append(int(input('informe o valor de a{}: '.format(i))))
        b.append(int(input('informe o valor de b{}: '.format(i))))
        n.append(int(input('informe o valor de n{}: '.format(i))))
        print('\n---- {}ª equação: {}x ≅ {}(mod {})\n'.format(i+1,a[i],b[i],n[i]))

def isPrime(a):
    if a < 2: return False
    for i in range(2, int((a**0.5)+1)):
        if a%i == 0: return False
    return True

def achaInverso(a, n):
    for i in range(1,n):
            if (a*i)%n == 1:
                return i

def resolveEq(a, b, n):
    if b%gcd(a,n) != 0:
        print('a equação {}x ≅ {}(mod {}) não tem solução pois b não divide mdc(a,n)'.format(a,b,n))
        exit()

    a = a%n
    b = b%n

    if a == 1:
        return b

    if not isPrime(n) and gcd(a,n) != 1:
        # ----------------------- busca
        for i in range(1,n):
            if (a*i)%n == b:
                x = i
                break
        
    else:
        # ----------------------- inversao                                 
        inverso = achaInverso(a, n)
        x = (b*inverso)%n

    return x    

if __name__ == "__main__":
    main()