from services.track_ip import get_local_ip
from services.open_cmd import lance_commande_cmd
from services.utils import getListCommande, getJsonContent

ip = get_local_ip()

def loopCommande(commande_json_path): 
    
    list_projects = getJsonContent(commande_json_path)

    main_menu = getListCommande(list_projects)

    stop = False

    while not stop:
        try:
            answer = printCommandeAndGetAnswer(main_menu)

            if answer in ["e", "exit", "q", "quit"]:
                print("good bey!")
                stop = True
                break

            project = list_projects[main_menu[answer]]
            sub_menu = getListCommande(project["commande"], additional_commande={"b": "back", "e": "exit", "all": "lance all commande"})
            sub_answer = printCommandeAndGetAnswer(sub_menu)

            print("you choose: ", sub_menu[sub_answer])
            if sub_answer in ["b", "back"]:
                continue
            if sub_answer in ["e", "exit", "q", "quit"]:
                print("good bey!")
                stop = True
                break
            if sub_answer == "all":
                execute_answer(project["path"], project["commande"])
            else:
                execute_answer(project["path"], sub_menu[sub_answer])

            project = None
            sub_menu = None
            sub_answer = None

        except Exception as e:
            print("error: ", e)
            stop = True
            break


def execute_answer(path, commande):
    if isinstance(commande, list):
        for cmd in commande:
            lance_commande_cmd(path, cmd)
    elif isinstance(commande, str):
        lance_commande_cmd(path, commande)


def printCommandeAndGetAnswer(avaible_commande):
    for i in avaible_commande:
        print(f"{i}: {avaible_commande[i]}")

    answer = input("choose a commande: ")

    if answer not in avaible_commande:
        print("commande not avaible")
        return printCommandeAndGetAnswer(avaible_commande)
    return answer