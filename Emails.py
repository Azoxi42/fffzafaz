import random
import string

prenoms = [
    "Lucas", "Emma", "Noah", "Léa", "Hugo", "Chloé", "Louis", "Inès", "Gabriel", "Jade",
    "Nathan", "Manon", "Ethan", "Lina", "Enzo", "Louna", "Mathis", "Mila", "Tom", "Sarah"
]
suffixes = ["du75", "gamer", "pro", "lol", "xyz", "23", "off", "x", "dev", "yt", "pro2"]

def generate_username():
    prenom = random.choice(prenoms)
    suffix = random.choice(suffixes)
    return f"{prenom.lower()}{suffix}"

def generate_email_password_pairs(count, domain="golden_multitools.com", password_length=10):
    pairs = []
    used_usernames = set()

    for _ in range(count):
        username = generate_username()
        while username in used_usernames:
            username = generate_username()
        used_usernames.add(username)

        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
        email = f"{username}@{domain}"
        pairs.append((email, password))
    
    return pairs

def main():
    nombre = int(input("Combien d'emails veux-tu générer ? "))
    domain = input("Quel domaine veux-tu utiliser ?  ") or "golden_multitools.com"
    password_length = int(input("Longueur du mot de passe ?  ") or 10)

    pairs = generate_email_password_pairs(nombre, domain, password_length)
    
    with open("emails.txt", "w") as f:
        for email, password in pairs:
            line = f"{email} : {password}\n"
            print(line.strip())
            f.write(line)

    print(f"\nTous les emails ont été enregistrés dans 'emails.txt'.")

if __name__ == "__main__":
    main()