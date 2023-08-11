#Set is a gathering of unchangeble objects

#between parentheses, its a iterable
set1 = set('Kelwin')

#between keys, its a set list not ordered
set2 = {1,'Kelwin',25,(5,1)}

print(f'exemplo de set básico: {set2}')



set2.add(2)
set2.update((1,5,8)) # put it insede another parentheses
set2.discard(25)
#set2.clear()

#you can use for with set
for n in set2:
    print(n)


#Useful Operators
#Union | = Unite both sets
#Intersection & = Items present in both lists
#Difference - = Items present just in left side
#Symmetric difference ^ = Items aren't present in both

exe1={1,2,3}
exe2={2,3,4}
exe3=exe1.symmetric_difference(exe2)

print(exe3)