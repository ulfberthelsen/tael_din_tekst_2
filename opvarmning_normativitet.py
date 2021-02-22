# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 00:08:01 2021

@author: au100440
"""

print('Hvor mange kopper kaffe drikker du om dagen?')
a = int(input())
if a == 4: 
    print('Dit forbrug er gennemsnitligt')
elif a < 4: 
    print('Du bør drikke mere kaffe!')
elif a > 4:
    print('Du bør drikke mindre kaffe!')