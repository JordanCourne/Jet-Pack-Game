from fractions import gcd

def PGCD(a,b) :
    if a > b :
        plusGrand = a
    else :
        plusGrand = b
    for i in range(plusGrand) :
        j = plusGrand - i
        for k in range(plusGrand +1) :
            for l in range(plusGrand +1) :
                if j * k == a and j * l == b :
                    return j

def PPCM(a,b) :
    if a > b :
        plusGrand = a
    else :
        plusGrand = b
    for i in range(plusGrand) :
        for j in range(plusGrand) :
            if a*(i+1) == b*(j+1) :
                return(a*(i+1))


for a in range(100000) :
    for b in range(a):
        PGCD = gcd(a,b)
        if PGCD != 0 :
            if ((a*b)/PGCD) - PGCD == 187 :
                print(a, " - ", b)
