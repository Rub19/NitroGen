import requests
import random
import string


print("Ceci est un générateur de code nitro discord fais un python est aussi un checker .\n\n\n")
num = int(input('Combien de code voulais vous crée :\n'))


with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Vos codes nitro sont en train d'être généré, soyez patient!")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n") #si le code nitro est valide cela va l'afficher 
        else:
            print(f"*", end = "")   #Cela écris "*" si le code est invalide

print("\n\n\nVous avez généré les code et les checker regardez si vous avez des valides ^^")