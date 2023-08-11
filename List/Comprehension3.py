#Filter
#it should be write at RIGHT of the For list
#Left Map, Right Filter
alist = [(n * 2) if n > 3 else n for n in range(10) if n and (n * 2) > 2]
print(alist)

