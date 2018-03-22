import random,math

N = int(input())
grid=[]
for _ in range(N):
    grid.append(input())

def find_tiret():
    res=[]
    for i in range(N):
        for j in range(N):
            if grid[i][j]=='-': 
                bol=True
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

def dfs_h(grid, start):
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

def find_middle_x(t):
    vals=dfs_x(grid, t)
    vals_y=[v[1] for v in vals]
    return math.floor(min(vals_y)+(max(vals_y)-min(vals_y))/2)

def find_middle_h(t):
    vals=dfs_h(grid, t)
    vals_x=[v[0] for v in vals]
    return math.floor(min(vals_x)+(max(vals_x)-min(vals_x))/2)

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
    tirets = find_tiret()
    count = len(tirets)
    candidates = random.sample(tirets, math.floor(count/5))
    max_long_x=0
    x_max_x,x_max_y=[0,0]
    max_long_y=0
    y_max_y,y_max_x=[0,0]
    for v in candidates:
        long_x=len(dfs_x(grid, (v[0],v[1])))
        long_y=len(dfs_x(grid, (v[0],v[1])))
        if long_x>max_long_x:
            max_long_x=long_x
            x_max_x,x_max_y=[v[0],v[1]]
        if long_y>max_long_y:
            max_long_y=long_y
            y_max_x,y_max_y=[v[0],v[1]]
    if max_long_x>max_long_y:
        print(x_max_x,find_middle_x((x_max_x,x_max_y)))
    else:
        print(find_middle_h((y_max_x,y_max_y)),y_max_y)
            