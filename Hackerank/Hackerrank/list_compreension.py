x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
coord = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
print(coord)

filter_c = [c for c in coord if sum(c) != n]

print(coord)


        

