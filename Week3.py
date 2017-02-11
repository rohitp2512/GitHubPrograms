def descending(flist):
  flist2=[]
  flist2=flist[0:]
  for i in range(0,len(flist)):
    for i in range(0,(len(flist)-1)):
      if flist[i+1]>=flist[i]:
        (flist[i+1],flist[i])=(flist[i],flist[i+1])
  if flist==flist2:
    return(True)
  else:
    return(False)
  
