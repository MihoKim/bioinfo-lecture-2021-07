#! /usr/bin/env python

d_table = {'fruit':'apple','color':'red','dia':10}
print('apple' in d_table)
print('fruit' in d_table)
print('color' in d_table)
print('red' in d_table)

print(d_table.keys())                   #dict_keys(['fruit', 'color', 'dia'])
print(type(d_table.keys()))             #<class 'dict_keys'>

print(d_table.values())                 #dict_values(['apple', 'red', 10])
print(type(d_table.values()))           #<class 'dict_values'>

print(d_table.items())                  #dict_items([('fruit', 'apple'), ('color', 'red'), ('dia', 10)])
print(type(d_table.items()))            #<class 'dict_items'>

#print(d_table.items()[0])              #error; dictionary -> indexing x
print(list(d_table.items())[0])         #('fruit', 'apple')
print(type(list(d_table.items())[0]))   #<class 'tuple'>

