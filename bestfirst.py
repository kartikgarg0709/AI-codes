import copy
def deque(q):
    new=[]
    for i in q:
        new.append(i[1])
    new.sort()
    for i in q:
        if(i[1]==new[0]):
            elem=i[0]
            break
    q.remove((elem,i[1]))
    return elem,new[0]
       
def heru(mat,goal):
    d=0
    for i in range(3):
        for j in range(3):
            if mat[i][j]!=goal[i][j]:
                d+=1
    return d
def empty(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j]==0:
                return i,j
def moveup(mat):
    mat1=copy.deepcopy(mat)
    i,j=empty(mat)
    if i!=0:
        mat1[i][j],mat1[i-1][j]=mat1[i-1][j],mat1[i][j]
        return mat1
    else:
        return mat
       
def movedown(mat):
    mat1=copy.deepcopy(mat)
    i,j=empty(mat)
    if i!=2:
        mat1[i][j],mat1[i+1][j]=mat1[i+1][j],mat1[i][j]
        return mat1
    else:
        return mat
       
def moveleft(mat):
    mat1=copy.deepcopy(mat)
    i,j=empty(mat)
    if j!=0:
        mat1[i][j],mat1[i][j-1]=mat1[i][j-1],mat1[i][j]
        return mat1
    else:
        return mat
       
def moveright(mat):
    mat1=copy.deepcopy(mat)
    i,j=empty(mat)
    if j!=2:
        mat1[i][j],mat1[i][j+1]=mat1[i][j+1],mat1[i][j]
        return mat1
    else:
        return mat
       
def best(mat,goal):
    visited=[]
    q=[]
    visited.append(mat)
    while(1):
        new=moveup(mat)
        val=heru(mat,goal)
        if new!=mat:
            if new == g:
                print("found goal")
                return
            else:
                if new not in visited:
                    q.append((new,val))
       
        new=movedown(mat)
        val=heru(mat,goal)
        if new!=mat:
            if new == g:
                print("found goal")
                return
         
            else:
                if new not in visited:
                    q.append((new,val))
       
        new=moveright(mat)
        val=heru(mat,goal)
        if new!=mat:
            if new == g:
                print("found goal")
                return
         
            else:
                if new not in visited:
                    q.append((new,val))
        new=moveleft(mat)
        val=heru(mat,goal)
        if new!=mat:
            if new == g:
                print("found goal")
                return
         
            else:
                if new not in visited:
                    q.append((new,val))
        

        if(len(q)>0):
            mat,x=deque(q)
            if mat not in visited:
                visited.append(mat)
           
           
           
s=[[4,5,2],[7,0,6],[8,1,3]]
g=[[1,6,3],[4,5,0],[2,7,8]]
best(s,g)