#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        valueurs = list(a_dictionary.values())
        cles = list(a_dictionary.keys())
        return cles[valeurs.index(max(valeurs))]
    else:
        return None

#The index() method returns the index of the specified element in the list.

   """ 
   if a_dictionary:
        score = 0
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                best = key
        return best
    return None
    """
