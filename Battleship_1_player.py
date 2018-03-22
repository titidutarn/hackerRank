import random,math

N = int(input())
grid=[]
for _ in range(N):
    grid.append(input())

def find_hyphens():
    res=[]
    for i in range(N):
        for j in range(N):
            if grid[i][j]=='-':
                res.append([i,j])
    return res

def find_h():
    res=[]
    count=0
    for i in range(N):
        for j in range(N):
            if grid[i][j]=='h':
                count+=1
                res.append([i,j])
    return count,res

def dfs_x(grid, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            try :
                if grid[vertex[0]][vertex[1]+1]=='-' and vertex[1]+1<10:
                    stack.extend([(vertex[0],vertex[1]+1)])
            except:
                pass
            try :
                if grid[vertex[0]][vertex[1]-1]=='-' and vertex[1]-1>=0:
                    stack.extend([(vertex[0],vertex[1]-1)])
            except:
                pass
    return visited

def dfs_y(grid, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            try :
                if grid[vertex[0]+1][vertex[1]]=='-' and vertex[0]+1<10:
                    stack.extend([(vertex[0]+1,vertex[1])])
            except:
                pass
            try :
                if grid[vertex[0]-1][vertex[1]]=='-' and vertex[0]-1>=0:
                    stack.extend([(vertex[0]-1,vertex[1])])
            except:
                pass
    return visited

c,l=find_h()
p=False
if c==1 :
    i,j=l[0]
    try:
        if grid[i-1][j]=='-' and p==False:
            print(i-1,j)
            p=True
    except:
        pass
    try:
        if grid[i+1][j]=='-' and p==False:
            print(i+1,j)
            p=True
    except:
        pass
    try:
        if grid[i][j-1]=='-' and p==False:
            print(i,j-1)
            p=True
    except:
        pass
    try:
        if grid[i][j+1]=='-' and p==False:
            print(i,j+1)
            p=True
    except:pass

elif c>1:
    seti,setj=[set(),set()]
    bateauEnLigne=False
    val=0
    for v in l:
        seti.add(v[0])
        setj.add(v[1])
    if len(seti)<len(setj):
        bateauEnLigne=True
        val=list(seti)[0]
    else:
        val=list(setj)[0]
    
    if bateauEnLigne:
        valj=[v[1] for v in l]
        minj=min(valj)
        maxj=max(valj)
        try:
            if grid[val][minj-1]=='-' and p==False:
                print(val,minj-1)
                p=True
        except:
            pass
        try:
            if grid[val][maxj+1]=='-' and p==False:
                print(val,maxj+1)
                p=True
        except:
            pass
    else:
        vali=[v[0] for v in l]
        mini=min(vali)
        maxi=max(vali)
        try:
            if grid[mini-1][val]=='-' and p==False:
                print(mini-1,val)
                p=True
        except:
            pass
        try:
            if grid[maxi+1][val]=='-' and p==False:
                print(maxi+1,val)
                p=True
        except:
            pass


else:
    hyphens = find_hyphens()
    count = len(hyphens)
    max_long_x_y=0
    max_x,max_y=[0,0]
    for v in hyphens:
        long_x=len(dfs_x(grid, (v[0],v[1])))
        long_y=len(dfs_y(grid, (v[0],v[1])))
        if long_x+long_y>max_long_x_y:
            max_long_x_y=long_x+long_y
            max_x,max_y=[v[0],v[1]]
    print(max_x,max_y)
