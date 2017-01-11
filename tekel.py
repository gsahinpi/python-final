boundary=600
def sumcheck(boundary,firstset,largest):
    if len(firstset)<=0:

        return  True
    mysum=sum(firstset)
    #print "mysym"+str(mysum)+" largest"+str(largest)
    if mysum+largest<=boundary:
        return True
    else:
        return False
def setsumcheck(boundary,firstset):
    if len(firstset)<=0:

        return  True
    if sum(firstset)>boundary:
        return False
    else:
        return True
fhand = open('dr_S03_2_2018_800.txt', 'r')
set0=list()
sets=[[]]
#read values and form a sorted list
for cheese in fhand:
    dummy=cheese.split(" ")
    count=0
    for s in dummy:
        count=count+1
        if s.isalnum() and count>2:
           set0.append(int(s))
 #sort the initial data
set0.sort()
index=0
print set0
#print ( sets[index][0])
while     len(set0)>0:
    #check if sets[index] is 0
         if len(sets[index])<=0:
               sets[index].append(set0[len(set0)-1])
               set0.remove(set0[len(set0)-1])

        #check for boundary
         if sum(sets[index])<=boundary:
          # dummylist=reversed(set0)
           for val in set0:
               if  sumcheck(boundary,sets[index],val):
                     sets[index].append(val)
                     set0.remove(val)
               else:
                  break

         index=index+1
         sets.append([])





print sets
print set0
print len(sets)




