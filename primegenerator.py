
import sys
import math

def primeGenerator(m,k):
    
     
     arr=[x for x in range(k+1)]
     arr[1]=False
     listion=[2]
     mid=int(len(arr)**0.5)+2

     for z in range(3,mid,2):
             i=0
             while(z*i<k+1):
                            arr[z*i]=False
                            i=(2*i)+1
                           
     return arr

print primeGenerator(0,100)
'''
                            

     
     for y in range(m,len(arr)):
          if arr[y]==1:
               listion.append(y)
            
     return listion
list1=[]
y=int(sys.stdin.readline())
if y<=10:

          for x in range(y):
               input1,input2=sys.stdin.readline().split()
               list1.append(primeGenerator(int(input1),int(input2)))
               if x!=(y-1):
                    list1.append(" ")
          for y in list1:
               for z in y:
                    print z
               

  ''' 
     
     



      








