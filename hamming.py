#Practical -1 Implement HAMMING CODE method to correct error in frame using any programming language . 
import math

def calcParAmnt(data):
    for a in range(len(str(data))):
        if 2**a>=len(str(data))+a+1:
            return a

def arbseq(data):
    parbits = calcParAmnt(data)
    sequence = []
    count = 0
    for a in range(len(str(data))+parbits):
        if (math.log(a+1,2))%1==0:
            sequence.append('0')
        else:
            sequence.append(str(data)[count])
            count+=1
    sequence.reverse()
    return sequence

def hammer(data):
    for a in range(1,len(data)+1):
        if data[-a]=='1' or data[-a]=='2' or data[-a]=='3':
            #print("skipped")
            continue

        parityseq = 0

        if (math.log(a,2)%1==0):
            #print("started")
            for b in range(1,len(data)+1):
                if a&b!= 0:
                    #print("checked",a,b)
                    if data[-b]=='1':
                        parityseq+=1
                else:
                    continue
            if parityseq%2==0:
                #print(parityseq)
                data[-a]='0'
                #print("changed to 0")
            else:
                #print(parityseq)
                data[-a]='1'
                #print("changed to 1")
        else:
            continue

    return data

def errorcheck(data):
    for a in range(1,len(data)+1):
        parityseq = 0
        if math.log(a,2)%1==0:
            for b in range(1,len(data)+1):
                if a&b!=0:
                    if data[-b]=='1':
                        parityseq+=1
                else:
                    continue
            if parityseq%2==0:
                pass
            else:
                return "Error detected"
    return "No errors"
    


#number = int(input("Enter data:"))
number = 11111
checker = ['1','1','1','1','1','1','1','1','1']
#print(calcParAmnt(number))
print(arbseq(number))
print(hammer(arbseq(number)))
print(errorcheck(hammer(arbseq(number))))
print(errorcheck(checker))