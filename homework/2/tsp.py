import random

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

def distance(p1, p2):
    #print('p1=', p1)
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
    return dist
#print(pathLength([5, 0, 2, 3, 1, 4, 6, 8, 10, 11, 9, 7]))
def Neighbor(p):
    neighbors=[]
    for i in range(len(p)):
        for j in range(i+1,len(p)):
           neighbor = p.copy()
           neighbor[i] = p[j]
           neighbor[j] = p[i]
           neighbors.append(neighbor) 
    return neighbors

def randomSolution(p):
    citys= list(range(len(p)))
    solution=[]
    
    for i in range(len(p)):
        randomCity= citys[random.randint(0,len(citys)-1)]
        solution.append(randomCity)
        citys.remove(randomCity)
    
    return solution

def Opt_n(neighbors):
    shortestPath = pathLength(neighbors[0])
    opt_n= neighbors[0]
    for neighbor in neighbors:
        cur_pathLength= pathLength(neighbor)
        if cur_pathLength<shortestPath:
            shortestPath=cur_pathLength
            opt_n= neighbor
    return opt_n,shortestPath

def hillClimbing(p):
    cur_Solution = randomSolution(p)
    cur_pathLength= pathLength(cur_Solution)
    neighbors= Neighbor(cur_Solution)
    #print(cur_Solution)
    #print(neighbors)
    #print(cur_pathLength)
    
    opt_n, shortest_n_Path= Opt_n(neighbors)
    print(opt_n,shortest_n_Path)
    while shortest_n_Path < cur_pathLength:
        cur_Solution= opt_n
        cur_pathLength = shortest_n_Path
        neighbors= Neighbor(cur_Solution)
        #print(cur_pathLength)
        opt_n, shortest_n_Path= Opt_n(neighbors)
        print(opt_n,shortest_n_Path)
    print("\nAnwser: ",cur_Solution,cur_pathLength)

hillClimbing(citys)
#print('pathLength=', pathLength(path))
