from math import *

def dist(latA, latB, longA, longB):
    return (6371.01*acos(sin(latA)*sin(latB)+cos(latA)*cos(latB)*cos(longA-longB)))
    
def main():
    latA = radians(float(input('Digite a latitude A: ')))
    longA = radians(float(input('Digite a longitude A: ')))
    latB = radians(float(input('Digite a latitude B: ')))
    longB = radians(float(input('Digite a longitude B: ')))
    
    print('A distância é %.2fkm.' % dist(latA, latB, longA, longB))
    
main()