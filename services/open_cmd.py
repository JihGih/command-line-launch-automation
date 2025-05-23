import subprocess
import os


def lance_commande_cmd(path, commande):
    if ('no_shell' in commande):
        commande = commande.replace('no_shell', '')
        lance_commande_cmd_non_bloquant(path, commande)
    else:
        subprocess.Popen(f'start cmd /k "cd /d {path} && {commande}"', shell=True)


def lance_commande_cmd_bloquant(path, commande):
    try:
        result = subprocess.run(
            commande,
            cwd=path,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stderr:
            print("Erreurs :", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
        print("Sortie d'erreur :", e.stderr)
    except FileNotFoundError:
        print(f"Le chemin '{path}' n'existe pas ou la commande n'a pas été trouvée.")

def lance_commande_cmd_non_bloquant(path, commande):
    try:
        process = subprocess.Popen(
            commande,
            cwd=path,
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except FileNotFoundError:
        print(f"Erreur : Le chemin '{path}' n'existe pas ou la commande n'a pas été trouvée.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors du lancement de la commande : {e}")