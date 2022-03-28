# -*- coding: utf-8 -*-


with open('neighborhoods.txt') as f:
    neighborhoods = f.readlines()
    
for zone in neighborhoods:
    print(zone)
    
