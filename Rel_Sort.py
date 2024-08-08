def Rs(l1,l2):
   z=[]
   for i in range (0,len(l2)):
       x=l2[i]
       y=False
       c=i-1
       for j in range(c,-1,-1):
           if(x==l2[j]):
               print(c)
               y=True
               break
       if y:
           continue
       for k in range(0,len(l2)):
           if x==l2[k]:
               z.append(l1[k])
   return z
#testing
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i","j"]
list2 = [0,   1,   1,    0,   1,   2,   2,   0,   1,0]
print(Rs(list1,list2))