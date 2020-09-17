# input
#n = 5 # the number of dungeons
#ci = [7, 8, 10, 20, 4] # coin
#di = [4, 1, 3, 3, 2] # deadline

n=4
ci=[10,7,8,2]
di=[3,5,1,1]

def hunter_scheduling(n, ci, di):
    """
    input:
        add arguments whatever you want
    :return: int
        the maximum numbers of coins if a gamer clear dungeons optimally
    """
    cumsum = 0 # the maximum numbers of coins if a gamer clear dungeons optimally
    culi = []
    for i in range(n):
        culi2 = []
        for j in range(len(di)):
            
            if di[j] == i:
                culi2.append(j)
        if len(culi2)>1:
            print('두개이상')
            idx = [ci[x] for x in culi2]
            for i in range(1,len(culi2)):
                if len(culi) == 0:
                    idxx = ci.index(max(idx))
                    culi.append(idxx)
                if ci[culi[-i]] < min(idx):
                    culi[-1] = ci.index(min(idx))
                    culi2.remove(ci.index(min(idx)))
                    culi += culi2
                    print(culi)
                else:
                    continue
        elif len(culi2) != 0:
            culi += culi2
            print(culi)
        else:
            
    print(culi)
    cumsum = sum(ci[x] for x in culi)
    return cumsum

# output
cumsum = hunter_scheduling(n, ci, di)

print("Accepted Output", 45)
print("My Result", cumsum)
