# input
"""
n = 5 # the number of dungeons
ci = [7, 8, 10, 20, 4] # coin
di = [4, 1, 3, 3, 2] # deadline
"""
n = int(input())
data = [None] * n
for i in range(n):
    c, d = input().split(' ')
    data[i] = [int(c),int(d)]

def hunter_scheduling(n, data):
    """
    input:
        add arguments whatever you want
    :return: int
        the maximum numbers of coins if a gamer clear dungeons optimally
    """
    cumsum = 0 # the maximum numbers of coins if a gamer clear dungeons optimally

    #data = zip(ci, di)
    data = sorted(data, key=lambda x: x[1])
    print(data)
    pq = []
    ix = n - 1

    for t in range(n, 0, -1):
        while ix >= 0 and t <= data[ix][1]:  # compare deadline_i and time
            pq.append(data[ix][0])  # push coin_i
            ix -= 1

        if len(pq) != 0:
            pq.sort()
            max_c = pq.pop(-1)
            cumsum += max_c

    return cumsum

# output
cumsum = hunter_scheduling(n, data)
print(cumsum)
