nom = input("Quel est votre nom ?")
age = input("Quel est votre age ?")

try:
    age_prochain = int(age) + 1
except:
    print("ERROR: vous devez entre un nombre pour l'age")
else:
    print("Vous vous appellez " + nom + ", vous avez " + str(age) + " ans ")
    print("L'an prochain vous aurai " + str(age_prochain) + " ans ")
