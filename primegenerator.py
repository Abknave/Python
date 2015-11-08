
import sys
import math

def primeGenerator(m,k):
    
     
     arr=[int(1) for x in range(0,k+1)]
     arr[0]=0
     arr[1]=0
     listion=[]
     
     for z in range(2,int(len(arr)**0.5)+2):
             i=0
             while(((z**2)+(i*z))<(k+1)):
                            arr[((z**2)+(i*z))]=0
                            i=i+1
                            

     
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
               

     
     
     



      








