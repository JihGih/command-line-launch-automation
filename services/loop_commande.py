from services.track_ip import get_local_ip
from services.open_cmd import lance_commande_cmd
from services.utils import getListCommande, getJsonContent
import os

ip = get_local_ip()

def loopCommande(commande_json_path): 
    
    list_projects = getJsonContent(commande_json_path)

    main_menu = getListCommande(list_projects)

    stop = False

    while not stop:
        printTitle("Main Menu")
        try:
            answer = printCommandeAndGetAnswer(main_menu)

            if isExit(answer):
                print("good bey!")
                stop = True
                break

            back = False

            while not back:
                printTitle(f"Sub Menu: {main_menu[answer]}")
                
                project = list_projects[main_menu[answer]]
                sub_menu = getListCommande(project["commande"], additional_commande={"b": "back", "e": "exit", "all": "lance all commande"})
                sub_answer = printCommandeAndGetAnswer(sub_menu)

                if isExit(sub_answer):
                    print("good bey!")
                    stop = True
                    back = True
                    break
                if isBack(sub_answer):
                    back = True
                    break

                commande = project["commande"] if sub_answer == "all" else sub_menu[sub_answer]
                executeAnswer(project["path"], commande)

            project = None
            sub_menu = None
            sub_answer = None

        except Exception as e:
            print("error: ", e)
            stop = True
            break

def isExit(answer):
    return answer in ["e", "exit", "q", "quit"]

def isBack(answer):
    return answer in ["b", "back"]

def executeAnswer(path, commande):
    if isinstance(commande, list):
        for cmd in commande:
            lance_commande_cmd(path, cmd)
    elif isinstance(commande, str):
        lance_commande_cmd(path, commande)

def printTitle(title):
    clear_console()
    print("===================================")
    print(f"============ {title} =============")
    print("===================================")

def printCommandeAndGetAnswer(avaible_commande):
    for i in avaible_commande:
        print(f"{i}: {avaible_commande[i]}")

    answer = input("choose a commande: ")
    print("you choose: ", answer)

    if answer not in avaible_commande:
        print("commande not avaible")
        return printCommandeAndGetAnswer(avaible_commande)
    return answer

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
