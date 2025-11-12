import os
import sys
import json


def getDictionnaryKey(dictionnary):
    dictionnary_label = {}

    for index, key in enumerate(dictionnary):
        dictionnary_label[f"{index+1}"] = key

    return dictionnary_label

def getListKey(list_data):
    list_label = {}

    for index, item in enumerate(list_data):
        list_label[f"{index+1}"] = item

    return list_label

def getListCommande(dictionnary, additional_commande={"e": "exit"}):
    avaible_commande = {}

    if (isinstance(dictionnary, dict)):
        avaible_commande = getDictionnaryKey(dictionnary)
    elif (isinstance(dictionnary, list)):
        avaible_commande = getListKey(dictionnary)

    avaible_commande = {**avaible_commande, **additional_commande}
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