import math

#Αλγοριθμος γρήγορης υψώσεις σε δύναμη για την υλοποιήσει της F(X) = (X^2 + 1) mod N
def Fast_Exponentiation(b , e , m):
 B = b #Base
 result = 1
 M = m #Μodulo
 E = e #exponent
 while (E > 0):
    if ((E % 2) == 1):
        result =(result * B) % M
    E = (E // 2) #Η πράξη // εκτελεί και επιστρέφει ακέραιο αποτέλεσμα ενώ η / δεκαδικό.
    B = ((B ** 2)+1) % M #Προσθέτω το +1 για να ικανοποιήσω την F(X)
 return result

def Pollard(N, X0, max_iterations):
    X = X0
    Y = X0
    i=0
    while True:
        i += 1
        # X ← F(X)
        X = Fast_Exponentiation(X,2,N)

        # Y ← F(F(Y))
        Z = Fast_Exponentiation(Y,2,N)
        Y = Fast_Exponentiation(Z,2,N)

        # gcd(|X − Y |, N)
        Absoluter_Wert =abs(X - Y)
        temp =math.gcd(Absoluter_Wert, N)
        # If 1 < gcd(|X − Y |, N) < N.
        if ( temp > 1 and temp < N):
            return temp
        if (i ==max_iterations):
            return 0

n = 2**257 - 1
X0 = 57108636
max_iterations = 100000000
result = Pollard(n, X0, max_iterations )
if result == 0:
    print('Δεν μπορεσε να βρει διαιρετη')
else :
    print('gcd(|X − Y |, N)',result)

