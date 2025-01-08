#Practical -2 Implement CRC and Check Sum protocol using any programming language. 

import math

def codegen(data,key):
    keylength = len(str(key))
    datalength = len(str(data))

    dividend = str(data)+'0'*(len(str(key))-1)
    #print(dividend)
    count=0
    quotient = ''

    for a in range(keylength,datalength+keylength):
        xorresult=''
        #print(dividend[count:keylength+count])
        if dividend[0]=='1':
            top = dividend[count:keylength+count]
            unused = dividend[keylength+count:]
            bottom = str(key)
            #print(top,bottom,unused)
            for b in range(len(top)):
                xorresult += str(eval(top[b])^eval(bottom[b]))
            xorresult = xorresult[1:]
            #print(xorresult)
            dividend = str(xorresult) + unused
            quotient += '1'
        else:
            top = dividend[count:keylength+count]
            unused = dividend[keylength+count:]
            bottom = '0'*keylength
            #print(top,bottom,unused)
            for b in range(len(top)):
                xorresult += str(eval(top[b])^eval(bottom[b]))
            xorresult = xorresult[1:]
            #print(xorresult)
            dividend = str(xorresult) + unused
            quotient += '0'

        #print(dividend)
        #count += 1
    redundancy = dividend
    return redundancy

def errorcheck(data,key):
    keylength = len(str(key))
    datalength = len(str(data))
    #print(keylength,datalength)

    #dividend = str(data)+'0'*(len(str(key))-1)
    dividend = str(data)
    #print(dividend)
    count=0
    quotient = ''

    for a in range(keylength,datalength+1):
        xorresult=''
        #print(dividend[count:keylength+count])
        if dividend[0]=='1':
            top = dividend[count:keylength+count]
            unused = dividend[keylength+count:]
            bottom = str(key)
            #print(top,bottom,unused)
            for b in range(len(top)):
                xorresult += str(eval(top[b])^eval(bottom[b]))
            xorresult = xorresult[1:]
            #print(xorresult)
            dividend = str(xorresult) + unused
            quotient += '1'
        else:
            top = dividend[count:keylength+count]
            unused = dividend[keylength+count:]
            bottom = '0'*keylength
            #print(top,bottom,unused)
            for b in range(len(top)):
                xorresult += str(eval(top[b])^eval(bottom[b]))
            xorresult = xorresult[1:]
            #print(xorresult)
            dividend = str(xorresult) + unused
            quotient += '0'

        #print(dividend)
        #count += 1
    print(dividend)
    if dividend=='0'*(keylength-1):
        return "No error"
    else:
        return "Error detected"


dataword = 10001101
keybit = 10101
print(codegen(dataword,keybit))
codeword = str(dataword) + codegen(dataword,keybit)
print(codeword)
print(errorcheck(codeword,keybit))