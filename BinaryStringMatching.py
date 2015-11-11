output=""
l=raw_input()



for i in 

        for i in range(2):
            b1,b2=raw_input().split(' ')
            assert len(b1)>=len(b2)
            if(int(b1,2)%2==0 and int(b2,2)%2==0):
               output=output+"1"+"\n"
            else:
               output=output+"0"+"\n"
        print output
        
