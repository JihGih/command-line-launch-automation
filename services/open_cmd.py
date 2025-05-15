import subprocess

def lance_commande_cmd(path, commande):
    subprocess.Popen(f'start cmd /k "cd /d {path} && {commande}"', shell=True)
