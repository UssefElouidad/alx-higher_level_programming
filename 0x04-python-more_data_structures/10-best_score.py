#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_student = None
    bigest_score = None

    for key, value in a_dictionary.items():
        if bigest_score is None or value > bigest_score:
            best_student = key
            bigest_score = value

    return best_student
