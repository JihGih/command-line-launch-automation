from services.track_ip import get_local_ip
from services.open_cmd import lance_commande_cmd
from services.utils import getListCommande, getJsonContent

ip = get_local_ip()

def loopCommande(commande_json_path): 
    
    list_projects = getJsonContent(commande_json_path)

    avaible_commande = getListCommande(list_projects)

    stop = False

    while not stop:
        try:
            for i in avaible_commande:
                print(f"{i}: {avaible_commande[i]}")

            answer = input("choose a commande: ")
            if not answer in avaible_commande:
                print("wrong choice")

            if answer in ["e", "exit", "q", "quit"]:
                print("good bey!")
                stop = True
                break


            project = list_projects[avaible_commande[answer]]
            for commande in project["commande"]:
                lance_commande_cmd(project["path"], commande)

        except Exception as e:
            print("error: ", e)
            stop = True
            break


def lanceAllCommande(commande_json_path):
    list_projects = getJsonContent(commande_json_path)

    for key in list_projects:
        project = list_projects[key]
        for commande in project["commande"]:
            lance_commande_cmd(project["path"], commande)
