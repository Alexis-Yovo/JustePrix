response = 14298

while True:
    avis = int(input("Quel est le nombre à deviner ? : "))
    
    if (avis > response):
        print("Moins")
    elif (avis < response):
        print("Plus")
    else:
        print("C'est gagné")
        break
