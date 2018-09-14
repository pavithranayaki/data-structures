def descending(l):
    x=0
    if len(l)==0 or len(l)==1:
        return True
    for value in range(0,len(l)):
         if l[value]>=l[value]+1:
             x=l[value]+1
             descending(l[x:len(l)])
             return True
         else:
             return False

def valley(list):
  if(len(list)==0):
    return(True)
  if(len(list)==1):
    return(False)
  if(list[0]<list[1]):
    return(False)
  for i in range(0,len(list)-1):
    if(list[i]<list[i+1]):
      pos=i
      break
    if(list[i]==list[i+1]):
      return(False) 
  else:
    return(False)
  for i in range(pos,len(list)-1):
    if(list[i]>=list[i+1]):
      return(False)
  return(True)

def transpose(m):
    p=[list(x) for x in zip(*m)]
    return p
