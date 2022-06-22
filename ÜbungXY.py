from math import sqrt

class Coord:
    x = 0
    y = 0
    dist = 0
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.dist = sqrt(x**2 + y**2)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x!r}, {self.y!r})'
    
    def __add__(self, target):
        """Überläd "+" operator
        if Unterscheidung für den Fall der Addition mit einert Klasse ungleich Coord"""
        if type(target) == type(self):
            return Coord(self.x + target.x, self.y + target.y)
        else:
            return Coord(self.x + target, self.y + target)
        

def read_coords():
    
    cords = []
    with open("coords.txt") as file:
        cords = file.readlines()
    
    listX = []
    listY = []  
    for i in range(1, len(cords)):
        row = cords[i].split(",")
        listX.append(float(row[0]))
        listY.append(float(row[1]))
        
    return listX, listY
    

def read_as_dict(file_name):
    data = {}
    with open(file_name) as fobj:
        keys = [x.strip() for x in next(fobj).split(',')] # nur 1. Zeile gelesen und in keys array gesteckt
        for key in keys:                                    # keys werden in tatsächliche dict keys verwandelt
            data[key] = []
        for line in fobj:                               # jeweils zwei Keys und Values
            for key, value in zip(keys, line.split(',')):
                data[key].append(float(value))
    return data


def sum_lists(X, Y):
    return sum(X), sum(Y)

def sum_dict(data):
    return sum(data['X']), sum(data['Y'])

"""Aufgabe 1 - 2 Korrektes Einlesen"""
X, Y = read_coords()
xy = read_as_dict("coords.txt")

"""Aufgabe 3 Summen auf vers Wegen bilden und überprüfen"""
print(sum_lists(X,Y))
print(sum_dict(xy))
print(sum_lists(X, Y) == sum_dict(xy) == (88.05864783223778, 120.76800430133447))

"""Aufgabe 5 Instanz wird erstellt und distance to (0, 0) wird korrekt berechnet"""
cord_ins = Coord(2, 3)
print(cord_ins.dist)

"""Aufgabe 6 Ergebnis der Representation"""
print(Coord(2, 3))

"""Aufgabe 7 mit List Comprehension"""
cord_lst = [Coord(X[i], Y[i]) for i in range(len(X))] 

"""Aufgabe 8. unten ist die Funktion des durch __add__ überladenen Operators zu sehen"""
print(cord_lst[0] + cord_lst[1])
