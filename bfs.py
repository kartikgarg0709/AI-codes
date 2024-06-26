import copy
A=[[2,0,3],[1,8,4],[7,6,5]]
G=[[1,2,3],[8,0,4],[7,6,5]]
q=[]
def findzero(A):
  for i in range(3):
    for j in range(3):
      if(A[i][j]==0):
        r=i
        c=j
        return r,c

def moveleft(A,i,j):
  new=copy.deepcopy(A)
  if j!=0:
   new[i][j],new[i][j-1]=new[i][j-1],new[i][j]
  #  print(new)
   if(new!=A):
    q.append(new)


def moveright(A,i,j):
  new=copy.deepcopy(A)
  if j!=2:
   new[i][j],new[i][j+1]=new[i][j+1],new[i][j]
   if(new!=A):
    q.append(new)
   #print(new)



def moveup(A,i,j):
  new=copy.deepcopy(A)
  if i!=0:
   new[i][j],new[i-1][j]=new[i-1][j],new[i][j]
   if(new!=A):
    q.append(new)
   #print(new)


def movedown(A,i,j):
  new=copy.deepcopy(A)
  if i!=2:
   new[i][j],new[i+1][j]=new[i+1][j],new[i][j]
   if(new!=A):
    q.append(new)
   #print(new)


def movegen(A):
  i,j=findzero(A)
  moveleft(A,i,j)
  moveright(A,i,j)
  moveup(A,i,j)
  movedown(A,i,j)


def final(A,G):
  movegen(A)
  while(1):
    if(len(q)>0):
      temp=q[0]
      print(q)
      del q[0]
      if(temp==G):
        print(G)
        return
      else:
        movegen(temp)
    else:
      return

final(A,G)