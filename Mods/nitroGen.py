import random, string
from colorama import init, Fore
import webbrowser

num = input('ecrit le nombre de nitro que tu veut généré : ')
charSet = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
bigStr = ""

with open("DB/Nitro.txt","w", encoding='utf-8') as file:

    print(f'{Fore.BLUE}veuillez attendre nous creons vos nitro')

    for i in range(int(num)):
        bigStr += f'https://discord.gift/{"".join(random.choices(charSet, k = 16))}\n'
        if i % 100_000 == 0:
            file.write(f'{bigStr}\n')
            bigStr = ""


    print(f'{Fore.CYAN} tu a bien generé tes code nitro"')
    input("!")