""" =========================================================
                CODE by fedora (per noia), tg @dictionnaire
    =========================================================
                                                           """
A1 = 1
A2 = 2
A3 = 3
B1 = 4
B2 = 5
B3 = 6
C1 = 7
C2 = 8
C3 = 9

MATRICE = [
    [A1, A2, A3],
    [B1, B2, B3],
    [C1, C2, C3]
]


def somma_s(x1, x2, x3):
    return x1 + x2 + x3

def diag(M):
    d1 = M[0][0]
    d2 = M[1][1]
    d3 = M[2][2]
    return d1 + d2 + d3

def antid(M):
    d1 = M[0][2]
    d2 = M[1][1]
    d3 = M[2][0]
    return d1 + d2 + d3

def ritmov(M):
    v1 = somma_s(*M[0])
    v2 = somma_s(*M[1])
    v3 = somma_s(*M[2])
    return v1, v2, v3

def ritmoO(M):
    h1 = sum([M[i][0] for i in range(3)])
    h2 = sum([M[i][1] for i in range(3)])
    h3 = sum([M[i][2] for i in range(3)])
    return h1, h2, h3

def cornice(t):
    line = "+" + "-"*(len(t)+2) + "+"
    print(line)
    print("| " + t + " |")
    print(line)

def stampa_matrice(M):
    cornice(" MATRICE SIMMETRICA ")
    for riga in M:
        print("  | " + " | ".join(f"{x:2}" for x in riga) + " |")   
    print("+----------------------+")
    
# big main
def main():
    stampa_matrice(MATRICE)

    d  = diag(MATRICE)
    ad = antid(MATRICE)
    v  = ritmov(MATRICE)
    h  = ritmoO(MATRICE)

    print("\nresultzzz:")
    print(f" D:         {d}")
    print(f" AD:    {ad}")
    print(f" RV:   {v}")
    print(f" RO: {h}\n")

if __name__ == "__main__":
    main()
