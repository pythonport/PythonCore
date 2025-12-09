'''
Created on Dec 2, 2025

@author: admin
'''

def update_scores(data):
    top = []
    for name in data:
        scores = list(data[name])
        scores.append(sum(scores) // len(scores))
        data[name] = tuple(scores)
        if scores[-1] >= 90:
            top.append(name)
    return top
marks = {"Anya": (88, 92), "Lia": (85, 87), "Zoya": (90, 95), "Isha": (78, 82)}
print(update_scores(marks))
