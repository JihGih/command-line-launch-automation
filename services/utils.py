import os
import sys
import json


def getDictionnaryKey(dictionnary):
    dictionnary_label = {}

    for index, key in enumerate(dictionnary):
        dictionnary_label[f"{index+1}"] = key

    return dictionnary_label

def getListCommande(dictionnary):
    avaible_commande = getDictionnaryKey(dictionnary)
    avaible_commande["e"] = "exit"
    avaible_commande["all"] = "all"

    return avaible_commande

def getJsonContent(relative_path):
    if getattr(sys, 'frozen', False):
        # Si exécutable compilé : utiliser le dossier temporaire de PyInstaller
        base_path = sys._MEIPASS
    else:
        # Sinon : partir du dossier contenant ce fichier (utils.py), puis remonter d’un niveau
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    full_path = os.path.join(base_path, relative_path)

    with open(full_path, "r", encoding="utf-8") as json_data:
        return json.load(json_data)