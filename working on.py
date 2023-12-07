l: list[int] = [0,2,0,2,4,4]


#merger tout
# => [0,4,0,0,8,0]

for i in range (len(l)):
    if l[i] == 0:
        continue
        
    for j in range(i + 1, len(l)): #any number after i, until the last one
        if l[j] == 0:
            continue
        
        if l[i] == l[j]:
            l[i] *= 2
            l[j] = 0
            
        break

#déplacer tout à gauche
# => [4,8,0,0,0,0]
def left(l):
    for i in range (len(l)):
        if l[i] != 0:
            continue
            
        for j in range (i + 1, len(l)):
            if l[j] == 0:
                continue
                
            if l[j] != 0:
                l[i] = l[j]
                l[j] = 0

            break

#--------------------------
#deplacer tout à droite
# => [0,0,0,0,4,8]

def right(l):
    l = list(reversed(l))
    left()
    l = list(reversed(l))

left(l)

print(l)

right(l)

print(l)



