#lezione 2 by PietroVolpe
#somma della lista di valori

def sum_list(lst):
    output = funzione(lst)
    return output
def funzione(lst):
    output = 0
    if not lst:
        return None
    for i in lst:
        if type(i) == int:
            output += i
        else:
            continue
    return output