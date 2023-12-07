# To do list

#le projet est à faire en MODE CONSOLE pas de Pygame (si vous avez terminé le projet vous me le montrez et ensuite on pourra éventuellement parler d'interface graphique)

# Fonctions a importer

def AskInt(sMessage: str) -> int:
    while True:
        try:
            print(sMessage)
            iInput: int = int(input())
            return iInput
        except ValueError:
            print("Veuillez entrer des nombres valides.")

'''
def AskIntMax(sMessage: str, iMax: int, allow_equal: bool = False) -> int:
    while True:
        try:
            value: int = AskInt(sMessage)
            if 0 <= value <= iMax or (allow_equal and 0 <= value <= iMax + 1):
                return value
            else:
                if allow_equal:
                    print(f"Veuillez entrer un nombre entre 0 et {iMax + 1}.")
                else:
                    print(f"Veuillez entrer un nombre entre 0 et {iMax}.")
        except ValueError:
            print("Veuillez entrer des nombres valides.")
'''